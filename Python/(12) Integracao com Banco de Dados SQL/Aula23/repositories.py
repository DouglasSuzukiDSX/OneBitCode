from dataclasses import dataclass, asdict
from typing import Optional
from connection import SessionLocal
from models import Clientes, Pedidos
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy import select, and_
from sqlalchemy.orm import selectinload

@dataclass
class Client:
   nome: str
   email: Optional[str] = None

@dataclass
class Item:
   item: str
   valor: float
   cliente_id: int

class ClientRepository:
   def new_client(self, client: Client) -> Optional[int]:
      try:
         with SessionLocal() as session:
            add_client = Clientes(**asdict(client))

            session.add(add_client)

            session.commit()

            print(f'Cliente {client.nome} cadastrado. \n')

            return add_client.id
      except IntegrityError as error:
         print(f'Nao foi possível cadastrar o cliente {client.nome}. Erro de integridade: {error}\n')
      except SQLAlchemyError as error:
         print(f'Erro interno: {error}\n')
      except Exception as error:
         print(f'Erro inesperado: {error}\n')

      return None

   def search_client_and_orders(self, id) -> None:
      try:
         with SessionLocal() as session:
            stmt = (
               select(Clientes)
                  .options(selectinload(Clientes.pedidos))
                  .where(Clientes.id == id)
            )

            user = session.scalars(stmt).first()

            if not user:
               print(f'Nao foi possivel localizar o usuario de ID: {id}\n')
               return None

         print(f'\n--------------\n')
         print(f'Usuario encontrado: {user.nome} - ID: {user.id}')
         print(f'Pedidos: {len(user.pedidos)}\n')

         for order in user.pedidos:
            print(f'- Nome: {order.item}: Valor: R$ {order.valor:.2f}')

      except IntegrityError as error:
         print(f'Nao foi possível cadastrar o cliente de ID: {id}. Erro de integridade: {error}')
      except SQLAlchemyError as error:
         print(f'Erro interno X: {error}')
      except Exception as error:
         print(f'Erro inesperado: {error}')
   
class OrderRepository:
   def new_order(self, item: Item):
      try:
         with SessionLocal() as session:
            add_order = Pedidos(**asdict(item))

            session.add(add_order)

            session.commit()

            print(f'Pedido cadastrado.')

            return True
      except IntegrityError as error:
         print(f'Nao foi possível registrar o pedido. Erro de integridade: {error}')
      except SQLAlchemyError as error:
         print(f'Erro interno: {error}')
      except Exception as error:
         print(f'Erro inesperado: {error}')

      return False
      
   def remove_item(self, client_id: int, item_name: str) -> None:
      with SessionLocal() as session:
         stmt = (
            select(Pedidos)
               .where(
                  and_( 
                     Pedidos.cliente_id == client_id,
                     Pedidos.item == item_name
                  )
               )
         )

         item = session.scalars(stmt).first()

         if not item: 
            print('Item nao encontrado')

         session.delete(item)

         session.commit()

         print(f'Item {item_name} excluido')

def run():
   # Criacao dos repositories (instancia das classes para manipulacao)
   client_repo = ClientRepository() 
   order_repo = OrderRepository() 

   client = Client('Mariana Souzaa') # Cria a estrutura
   client_id = client_repo.new_client(client)

   if client_id:
      orders_data = [
         ('Notebook', 4500.00), 
         ('Mouse', 150.00)
      ]

      for name, value in orders_data:

         item = Item(name, value, client_id) # Cria a estrutura
         order_repo.new_order(item)


      client_repo.search_client_and_orders(client_id)

      order_repo.remove_item(client_id, 'Mouse')

      print(f'\nNova listagem')
      client_repo.search_client_and_orders(client_id)

run()