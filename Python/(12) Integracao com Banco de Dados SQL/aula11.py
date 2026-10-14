# Aula11 - Lendo dados de uma tabela (PostgreSQL)

from conexao import get_connection

with get_connection() as connection:
   with connection.cursor() as cursor:
      cursor.execute('SELECT * FROM books ORDER BY id DESC;')

      print(cursor.fetchmany(5)[0])