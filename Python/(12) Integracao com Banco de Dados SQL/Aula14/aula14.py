import psycopg
from conexao import get_connection
from typing import Optional, Any, Literal, TypeAlias, Union
from enum import Enum

class Nivel(Enum):
   INICIANTE = 'INICIANTE'
   INTERMEDIARIO = 'INTERMEDIARIO'
   AVANCADO = 'AVANCADO'

curso_params: TypeAlias = tuple[str, str, int, Nivel]
query_params: TypeAlias = Union[tuple[curso_params], list[curso_params], int, Nivel, None]
Fetch = Literal['one', 'all', 'rowcount']

class Cursos:
   def __init__(self):
      self._cursor = None

      query = '''CREATE TABLE IF NOT EXISTS cursos (    
         id SERIAL PRIMARY KEY,
         titulo TEXT NOT NULL,
         instrutor TEXT NOT NULL,
         duracao_horas INT NOT NULL CHECK (duracao_horas > 0),
         nivel TEXT NOT NULL CHECK (nivel IN ('INICIANTE', 'INTERMEDIARIO', 'AVANCADO'))
      );'''

      self.__executar_query(query)

      print(f'🗄️  Banco de dados iniciado. 🗄️')

   def __executar_query(self, query, params: query_params = None, fetch: Fetch | None = None) -> Any:
      try:
         with get_connection() as connection:
            with connection.cursor() as cursor:

               if isinstance(params, list):
                  cursor.executemany(query, params) 
               elif isinstance(params, (int, Nivel)):
                  cursor.execute(query, (params,))
               else: 
                  cursor.execute(query, params)

               resultado = None

               if fetch == 'one':
                  row = cursor.fetchone()
                  resultado = row if row else None
               elif fetch == 'all':
                  rows = cursor.fetchall()
                  resultado = rows if rows else []
               else:
                  resultado = cursor.rowcount # Útil para UPDATE/DELETE (quantas linhas foram afetadas)

               return resultado
     
      except psycopg.Error as error:
         if error.sqlstate == '42P07':
            print('Tabela disponivel')
         else:
            print(f'Nao foi possivel executrar a query: {error}')

   def cadastrar_curso(self, titulo: str, instrutor: str, duracao_horas: int, nivel: Nivel) -> int:
      # Retorno: O id numérico gerado pelo PostgreSQL para o curso (RETURNING id).
      query = 'INSERT INTO cursos (titulo, instrutor, duracao_horas, nivel) VALUES (%s, %s, %s, %s) RETURNING id;'

      resultado = self.__executar_query(query, (titulo, instrutor, duracao_horas, nivel), 'one')

      return resultado['id'] if resultado else 0

   def cadastrar_cursos(self, cursos: list[curso_params]) -> int:
         # Retorno: O id numérico gerado pelo PostgreSQL para o curso (RETURNING id).
         query = 'INSERT INTO cursos (titulo, instrutor, duracao_horas, nivel) VALUES (%s, %s, %s, %s)'
   
         resultado = self.__executar_query(query, cursos, 'rowcount')
   
         return resultado if resultado else 0
   
   def listar_cursos_por_nivel(self, nivel: str) -> list[dict]:
      # Consulta os cursos filtrando pelo nível informado (ex.: buscar apenas cursos 'INICIANTE') e ordenando alfabeticamente pelo título.
      query = 'SELECT * FROM cursos WHERE nivel = %s ORDER BY titulo;'
      
      return self.__executar_query(query, nivel, 'all')
   
   def atualizar_duracao(self, curso_id: int, novas_horas: int) -> bool:
      # Atualiza a carga horária do curso correspondente ao curso_id.
      query = 'UPDATE cursos SET duracao_horas = %s WHERE id = %s;'

      resultado = self.__executar_query(query, (novas_horas, curso_id))

      return True if resultado else False
   
   def remover_curso(self, curso_id: int) -> dict | None:
      query = 'DELETE FROM cursos WHERE id = %s RETURNING titulo, instrutor;'

      return self.__executar_query(query, (curso_id,), 'one')

   def excluir_tabela(self) -> str:
      query = 'DROP TABLE cursos;'

      self.__executar_query(query)

      return 'Tabela cursos excluida. Ela sera criada quando rodar o programa novamente.'
   
curso_unico: curso_params = ('Engenharia Social', 'Jeferson Nascimento', 20, Nivel.AVANCADO)
lista_cursos: list[query_params] = [
   ('Defesa Pessoal', 'Jinbei', 35, Nivel.INICIANTE),
   ('Sommolier de bebibdas', 'Roronoa Zoro', 18, Nivel.INICIANTE),
   ('Tecnicas Culinarias', 'Sanji Vinsmoke', 22, Nivel.INTERMEDIARIO),
]

curso = Cursos()
print(curso.cadastrar_curso(*curso_unico))
print(curso.cadastrar_cursos(lista_cursos))
# print(curso.listar_cursos_por_nivel(Nivel.AVANCADO))
# print(curso.atualizar_duracao(1, 45))
# print(curso.remover_curso(37))
# print(curso.excluir_tabela())