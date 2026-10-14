# Aula10 - Criando a tabela e inserindo dados (PostgreSQL)
import psycopg
from conexao import get_connection

create_table = '''
   CREATE TABLE books(
      id SERIAL PRIMARY KEY,
      title TEXT NOT NULL,
      author TEXT NOT NULL,
      price NUMERIC(10,2) NOT NULL
   );
'''

# with get_connection() as connection:
#    with connection.cursor() as cursor:
#       cursor.execute('''
#          CREATE TABLE books(
#             id SERIAL PRIMARY KEY,
#             title TEXT NOT NULL,
#             author TEXT NOT NULL,
#             price NUMERIC(10,2) NOT NULL
#          );
#    ''')

query = '''
   INSERT INTO books(title, author, price) VALUES (%s, %s, %s);
'''

try:
   with get_connection() as connection:
      with connection.cursor() as cursor:
         cursor.execute(query, ('Dom Casmurro', 'Machado de Assis', 39.90))
         print('Livro criado com sucesso')
except psycopg.Error as e:
   pass