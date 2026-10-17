import subprocess
from pathlib import Path
from connection import DATABASE_URL  # <-- Puxa direto da sua conexão existente!

def configure_alembic_ini():
   """Atualiza automaticamente o sqlalchemy.url no alembic.ini usando a URL do connection.py"""
   alembic_ini_path = Path("alembic.ini")
   
   if not alembic_ini_path.exists():
      print("⚠️ Arquivo alembic.ini não encontrado.")
      return

   print(f"⚙️ Configurando url do banco no alembic.ini: {DATABASE_URL}")

   # Lê o conteúdo atual do alembic.ini
   content = alembic_ini_path.read_text(encoding="utf-8")

   # Substitui a linha do sqlalchemy.url antiga pela URL real do PostgreSQL
   new_content = []
   for line in content.splitlines():
      if line.startswith("sqlalchemy.url ="):
         new_content.append(f"sqlalchemy.url = {DATABASE_URL}")
      else:
         new_content.append(line)

   alembic_ini_path.write_text("\n".join(new_content), encoding="utf-8")
   print("✅ alembic.ini configurado com sucesso!")


def configure_env_py():
   """Garante que o alembic/env.py importe a Base do seu projeto"""
   env_py_path = Path("alembic/env.py")
   
   if not env_py_path.exists():
      return

   content = env_py_path.read_text(encoding="utf-8")
   
   if "from models import Base" in content:
      return

   print("⚙️ Configurando o target_metadata no alembic/env.py...")

   # Ajuste o caminho doimport de acordo com onde está a sua Base (ex: models)
   new_content = content.replace(
      "target_metadata = None",
      "from models import Base\ntarget_metadata = Base.metadata"
   )

   env_py_path.write_text(new_content, encoding="utf-8")
   print("✅ alembic/env.py configurado com sucesso!")


def inittialize_alembic(message: str):
   alembic_path = Path("alembic")

   if not alembic_path.exists():
      print('📁 Pasta "alembic" não encontrada. Iniciando configuração automática...')
      
      try:
         print('Executando: alembic init alembic')
         subprocess.run(["alembic", "init", "alembic"], check=True)

         configure_alembic_ini()
         configure_env_py()
         migrate(message)
         
      except subprocess.CalledProcessError as error:
         print(f"❌ Erro ao inicializar o Alembic: {error}")
   else:
      print('✅ Pasta "alembic" já existe. Pulando inicialização.')

def migrate(message: str):
   try:
      print(f'Executando: alembic revision --autogenerate -m "{message}"')
      subprocess.run(["alembic", "revision", "--autogenerate", "-m", message], check=True)

      alembic_upgrade()
        
   except subprocess.CalledProcessError as error:
      print(f"❌ Erro ao executar a migração: {error}")
   except Exception as error:
      print(f"❌ Erro inesperado na migração: {error}")

def alembic_upgrade():
   try:
      print("Executando: alembic upgrade head")
      subprocess.run(["alembic", "upgrade", "head"], check=True)

      print("✨ Migrações configuradas e aplicadas com sucesso!")
        
   except subprocess.CalledProcessError as error:
      print(f"❌ Erro ao executar o alembic upgrade: {error}")
   except Exception as error:
      print(f"❌ Erro inesperado no alembic upgrade: {error}")

if __name__ == "__main__":
   # inittialize_alembic("criando tabelas iniciais") # Para criar as configuracoes iniciais
   # migrate('test') # Para rodar migrate
   alembic_upgrade() # Restrutura as tables em caso de exclusao