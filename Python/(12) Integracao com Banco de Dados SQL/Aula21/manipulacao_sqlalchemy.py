from conexao_sqlalchemy import SessionLocal
from modelos import Usuario, Endereco
from sqlalchemy import select

# Insert
'''with SessionLocal() as session:
   novo_usuario = Usuario(
      nome='Ana Silva', 
      email='ana@example.com',
      telefone=123,
      enderecos=[Endereco(rua='Av. Paulista, 1000')] 
   )

   session.add(novo_usuario)

   session.commit()'''

# Update
'''with SessionLocal() as session:
   stmt = select(Usuario).where(Usuario.email == 'ana@example.com')
   usuario = session.scalars(stmt).first()

   if not usuario: exit()

   usuario.nome = 'Ana S. Santos'

   session.commit()'''

# Delete
with SessionLocal() as session:
   stmt = select(Usuario).where(Usuario.email == 'ana@example.com')
   usuario = session.scalars(stmt).first()

   if not usuario: exit()

   session.delete(usuario)
   session.commit()