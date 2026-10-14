class Filme:
   def __init__(self, titulo, diretor, ano):
      self.titulo = titulo
      self.diretor = diretor
      self.ano = ano
      self.avaliacao = 0
      self.total_avaliadores = 0

   def exibir_infos(self):
      print(f'Titulo..............: {self.titulo}')
      print(f'Diretor.............: {self.diretor}')
      print(f'Ano.................: {self.ano}')
      print(f'Avaliacao ..........: {self.avaliacao}')
      print(f'Total de avaliadores: {self.total_avaliadores}')

   def avaliar(self, nota):
      nota = nota + (self.avaliacao * self.total_avaliadores)
      self.total_avaliadores += 1
      self.avaliacao = round(nota / self.total_avaliadores, 2)

filme = Filme("1984", "Michael Radford", 1984)
filme.avaliar(8.0)
filme.avaliar(10.0)
filme.exibir_infos()

print('\n ----------------')

class Biblioteca:
   def __init__(self, nome):
      self.nome = nome
      self.livros = []

   def adicionar_livro(self, titulo, autor):
      self.livros.append({'titulo': titulo, 'autor': autor})

   def remover_livro(self, titulo):
      for livro in self.livros:
         if livro['titulo'] == titulo:
           self.livros.remove(livro)
           print(f'Livro {titulo} removido')
           return

      print(f'Livro {titulo} nao encontrado')

   def buscar_livro(self, titulo):
      for livro in self.livros:
         if livro['titulo'] == titulo:
            print(f'Livro encontrrado: {livro['titulo']} - {livro['autor']}')
            return

      print(f'Livro "{titulo}" nao encontrado.')
         
   def listar_livros(self):
      print(f'\n{self.nome}')

      if not self.livros:
         print('Biblioteca vazia')

      for livro in self.livros:
         print(f'- {livro['titulo']} ({livro['autor']})')

bib = Biblioteca("Biblioteca Central")
bib.adicionar_livro("1984", "George Orwell")
bib.adicionar_livro("Dom Casmurro", "Machado de Assis")
bib.listar_livros()

bib.buscar_livro("1984")

bib.remover_livro("1984")
bib.listar_livros()

print('\n ----------------')

class Tarefa:
   def __init__(self, descricao):
      self.descricao = descricao
      self.concluida = False

   def marcar_concluida(self):
      self.concluida = True

   def exibir(self):
      status = '[x]' if self.concluida else '[ ]'
      return f'{status} {self.descricao}'

class ListaTarefas:
   def __init__(self):
      self.tarefas = []

   def adicionar(self, descricao):
      self.tarefas.append(Tarefa(descricao))


   def listar_todas(self):
      for indice, tarefa in enumerate(self.tarefas):
         print(f'{indice + 1}. {tarefa.exibir()}')

   def listar_pendentes(self):
      for indice, tarefa in enumerate(self.tarefas):
         if not tarefa.concluida:
            print(f'{indice + 1}. {tarefa.exibir()}')

   def listar_concluidas(self):
      for indice, tarefa in enumerate(self.tarefas):
         if tarefa.concluida:
            print(f'{indice + 1}. {tarefa.exibir()}')

   def marcar_concluida(self, indice):
      if indice <= 0 or indice > len(self.tarefas):
         print('O indice inrformado esta fora do intervalo de tarefas salvas.')
         return

      self.tarefas[indice - 1].marcar_concluida()

lista = ListaTarefas()
lista.adicionar("Estudar Python")
lista.adicionar("Fazer exercícios")

print(f'Todas as tarefas:')
lista.listar_todas()

lista.marcar_concluida(1)

print(f'\nTarefas pendentes:')
lista.listar_pendentes()

print(f'\nTarefas concluidas:')
lista.listar_concluidas()