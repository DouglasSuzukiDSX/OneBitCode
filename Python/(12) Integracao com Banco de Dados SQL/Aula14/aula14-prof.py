from conexao import get_connection
from typing import Literal, List, Dict, Any, Optional

Nivel = Literal["INICIANTE", "INTERMEDIARIO", "AVANCADO"]

def criar_tabela():
	query = """
		CREATE TABLE IF NOT EXISTS cursos (
			id SERIAL PRIMARY KEY,
			titulo TEXT NOT NULL,
			instrutor TEXT NOT NULL,
			duracao_horas INT NOT NULL CHECK (duracao_horas > 0),
			nivel TEXT NOT NULL CHECK (nivel IN ('INICIANTE', 'INTERMEDIARIO', 'AVANCADO'))
		);
	"""

	with get_connection() as connection:
		with connection.cursor() as cursor:
			cursor.execute(query)

def cadastrar_curso(titulo: str, instrutor: str, duracao_horas: int, nivel: Nivel):
	query = """
		INSERT INTO cursos (titulo, instrutor, duracao_horas, nivel)
		VALUES (%s, %s, %s, %s)
		RETURNING id;
	"""

	with get_connection() as connection:
		with connection.cursor() as cursor:
			cursor.execute(query, (titulo, instrutor, duracao_horas, nivel))
			resultado = dict(cursor.fetchone() or {})
			return resultado["id"]

def listar_cursos_por_nivel(nivel: Nivel) -> List[Dict[str, Any]]:
	query = """
		SELECT *
		FROM cursos
		WHERE nivel = %s
		ORDER BY titulo ASC;
	"""

	with get_connection() as connection:
		with connection.cursor() as cursor:
			cursor.execute(query, (nivel,))

			return cursor.fetchall() # type: ignore

def atualizar_duracao(curso_id: int, novas_horas: int) -> bool:
	query = """
		UPDATE cursos
		SET duracao_horas = %s
		WHERE id = %s;
	"""

	with get_connection() as connection:
		with connection.cursor() as cursor:
			cursor.execute(query, (novas_horas, curso_id))
			return cursor.rowcount > 0

def remover_curso(curso_id: int) -> Optional[Dict[str, Any]]:
	query = """
		DELETE FROM cursos
		WHERE id = %s
		RETURNING titulo, instrutor;
	"""

	with get_connection() as connection:
		with connection.cursor() as cursor:
			cursor.execute(query, (curso_id,))
			return cursor.fetchone() #type: ignore

if __name__ == '__main__':
	criar_tabela()

	print("--- 1. Cadastrando Cursos ---")
	id1 = cadastrar_curso("Python para Iniciantes", "Ana Paula", 20, "INICIANTE")
	id2 = cadastrar_curso("Estruturas de Dados com Python", "Carlos Lima", 40, "INTERMEDIARIO")
	id3 = cadastrar_curso("Introdução ao SQL", "Ana Paula", 15, "INICIANTE")

	print(f"Curso 1 criado com ID: #{id1}")
	print(f"Curso 2 criado com ID: #{id2}")
	print(f"Curso 3 criado com ID: #{id3}")

	print("\n--- 2. Listando Cursos de Nível 'INICIANTE' ---")
	iniciantes = listar_cursos_por_nivel("INICIANTE")
	for curso in iniciantes:
			print(f"• [#{curso['id']}] {curso['titulo']} | Instrutor(a): {curso['instrutor']} | Duração: {curso['duracao_horas']}h")

	print(f"\n--- 3. Atualizando Carga Horária do Curso #{id1} ---")
	sucesso_atualizacao = atualizar_duracao(id1, 25)
	print(f"Duração atualizada com sucesso? {sucesso_atualizacao}")

	print(f"\n--- 4. Removendo o Curso #{id2} ---")
	removido = remover_curso(id2)
	if removido:
			print(f"Curso excluído: '{removido['titulo']}' ministrado por {removido['instrutor']}.")
	else:
			print("Curso não encontrado para exclusão.")

	print("\n--- 5. Testando Atualização de ID Inexistente (#999) ---")
	sucesso_invalido = atualizar_duracao(999, 50)
	print(f"Atualização em ID inexistente foi bem sucedida? {sucesso_invalido}")