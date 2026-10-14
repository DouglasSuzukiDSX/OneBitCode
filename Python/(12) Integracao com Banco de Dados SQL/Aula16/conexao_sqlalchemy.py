import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def obter_engine():
   # Obter as variáveis de ambiente
   db_name = os.getenv('DB_NAME')
   db_user = os.getenv('DB_USER')
   db_password = os.getenv('DB_PASSWORD')
   db_host = os.getenv('DB_HOST')
   db_port = os.getenv('DB_PORT')

   # Criar a URL de conexão com o banco de dados PostgreSQL
   DATABASE_URL = f'postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

   # Criar a engine do SQLAlchemy
   engine = create_engine(DATABASE_URL, echo=True)

   return engine

engine = obter_engine()

if __name__ == "__main__":
   with engine.connect() as connection:
      query = text("SELECT 'Olá do SQLAlchemy 2.0 Moderno!' AS mensagem")

      resultado = connection.execute(query)
      mensagem = resultado.scalar()

      print('\n' + "="*55)
      print(f'Sucesso na Integracao! Retorno do Banco: {mensagem}')
      print('\n' + "="*55)

