from conexao_sqlalchemy import SessionLocal
from modelos import Usuario
from sqlalchemy import select, or_, func, desc, asc, Integer, case, distinct
from sqlalchemy.orm import selectinload, joinedload

with SessionLocal() as session:
   ''' # Aqui retornar um tupla 
   stmt = select(Usuario.id, Usuario.nome, Usuario.email)
   resultado = session.execute(stmt)

   for linha in resultado:
      print(f'ID: {linha.id}, Nome: {linha.nome}, Email: {linha.email}')
      print(linha)'''

   # Aqui e a maneira pra retornar um o campo da tupla
   # stmt = select(Usuario).where(Usuario.email.ilike('%1%')) # Que tenha 1 no email
   # stmt = select(Usuario).where(or_(Usuario.email.is_not(None), Usuario.nome.like('James'))) 
   # stmt = select(func.count(Usuario.id)) # Contar os usuarios
   # stmt = select(Usuario).order_by(desc(Usuario.id)) # Ordenar por id decrescente
   '''stmt = select(
      Usuario.id,
      case(
         (Usuario.id < 18, 'Menor de idade'),
         (Usuario.id < 60, 'Adulto'),
         else_='Idoso'
      ).label('faixa_etaria')
   ) # Realiza as comparacoes'''
   '''stmt = select(distinct(Usuario.telefone)) # Seleciona os telefones distintos
   resultado = session.scalars(stmt).all()

   for linha in resultado:
      print(linha)'''

   # retultado2 = session.scalar(stmt)
   # print(retultado2)

   stmt = select(Usuario).options(selectinload(Usuario.enderecos)) # Retorna os enderecos do usuario
   resultado = session.scalars(stmt).all()

   for linha in resultado:
      print(linha.enderecos)