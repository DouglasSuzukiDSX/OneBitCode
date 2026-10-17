import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker
from save.modelos import Base, Usuario

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter as variáveis de ambiente
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

# Criar a URL de conexão com o banco de dados PostgreSQL
DATABASE_URL = f'postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

def obter_engine():
   # Criar a engine do SQLAlchemy
   engine = create_engine(DATABASE_URL, echo=False) # Para mostra as queries rodando basta mudar pra True

   return engine

engine = obter_engine()

with Session(engine) as session:
   pass 
   # Manipulação de dados
   session.commit()

SessionLocal = sessionmaker(engine) # Session padrao, importar em arquivos de manipulacao de dados