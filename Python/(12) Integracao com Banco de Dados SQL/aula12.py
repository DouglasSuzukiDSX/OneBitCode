# Aula12 - Atualizando e removendo dados de uma tabela (PostgreSQL)
from conexao import get_connection

def atualiza_preco_livro(livro_id: int, novo_preco: float):
   query = 'UPDATE books SET price = %s WHERE id = %s RETURNING title;'

   with get_connection() as connection:
      with connection.cursor() as cursor:
         cursor.execute(query, (novo_preco, livro_id))

         if cursor.rowcount < 0:
            print(f'Nenhum livro encontrado com o ID #{livro_id}')
            return

         book = dict(cursor.fetchone() or {})
         print(f'Livro {book['title']} #{livro_id} atualizado para R$ {novo_preco:.2f}')

def excluir_livro(livro_id: int):
   query = 'DELETE FROM books WHERE id = %s;'

   with get_connection() as connection:
      with connection.cursor() as cursor:
         cursor.execute(query, (livro_id,))

         if cursor.rowcount < 0:
            print(f'Nenhum livro encontrado com o ID #{livro_id}')
            return

         print(f'Livro #{livro_id} excluido com sucesso.')


# atualiza_preco_livro(1, 49.90)
excluir_livro(1)