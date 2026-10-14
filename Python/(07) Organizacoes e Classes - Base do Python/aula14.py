# Aula14 - Resolução: classe filmes | biblioteca | sistema de tarefas
'''
   Problema 1: Classe de filme
      Enunciado:
         Crie uma classe Filme com:
            Atributos: titulo, diretor, ano, avaliacao, total_avaliadores
            Avaliação e total de avaliadores não devem ser passados na criação, mas atribuídos diretamente em init.
            Método: exibir_info() que mostra todas as informações
            Método: avaliar(nota) que valida nota (0-10) e atualiza avaliação
            A nota (avaliação total) é a média das notas pela quantidade de avaliadores.

      Exemplo:
         filme = Filme("1984", "Michael Radford", 1984)
         filme.exibir_info()
         # Título: 1984
         # Diretor: Michael Radford
         # Ano: 1984
         # Avaliação: 0.0
         # Total de avaliadores: 0

      filme.avaliar(8.0)
      filme.avaliar(10.0)
      filme.exibir_info()
      # Avaliação: 9.0
      # Total de avaliadores: 2
'''
class Filme:
   def __init__(self, titulo, diretor, ano):
      self.titulo = titulo
      self.diretor = diretor
      self.ano = ano
      self.avaliacao = 0
      self.total_avaliadores = 0

   def exibir_info(self):
      media = self.avaliacao / self.total_avaliadores

      print(
         f'Titulo..............: {self.titulo}\n'
         f'Diretor.............: {self.diretor}\n'
         f'Ano.................: {self.ano}\n'
         f'Avaliacao ..........: {media}\n'
         f'Total de avaliadores: {self.total_avaliadores}'
      )

   def avaliar(self, nota: int):
      self.avaliacao += nota
      self.total_avaliadores += 1
      
def ex01():
   filme = Filme("1984", "Michael Radford", 1984)
   filme.avaliar(8.0)
   filme.avaliar(10.0)
   filme.exibir_info()

ex01()

'''
   Problema 2: Biblioteca
      Enunciado:
         Crie uma classe Biblioteca que gerencia livros:
            Atributos: nome, livros (lista)
            Método: adicionar_livro(titulo, autor) que adiciona livro
            Método: remover_livro(titulo) que remove livro
            Método: listar_livros() que mostra todos
            Método: buscar_livro(titulo) que procura e mostra informações

      Exemplo:
         bib = Biblioteca("Biblioteca Central")
         bib.adicionar_livro("1984", "George Orwell")
         bib.adicionar_livro("Dom Casmurro", "Machado de Assis")
         bib.listar_livros()
         # Biblioteca Central
         # - 1984 (George Orwell)
         # - Dom Casmurro (Machado de Assis)

      bib.buscar_livro("1984")
      # Livro encontrado: 1984 - George Orwell

      bib.remover_livro("1984")
      bib.listar_livros()
      # Biblioteca Central
      # - Dom Casmurro (Machado de Assis)
'''

class Biblioteca:
   def __init__(self, nome):
      self.nome = nome
      self.livros = []

   def adicionar_livro(self, titulo, autor):
      adc_livro = {'titulo': titulo, 'autor': autor}

      self.livros.append(adc_livro)

   def remover_livro(self, titulo):
      for livro in self.livros:
         if livro['titulo'] == titulo:
           self.livros.remove(livro)
         
   def listar_livros(self):
      lista_livros = []

      for livro in self.livros:
         lista_livros.append(f'- {livro['titulo']} ({livro['autor']})')
      
      listas_livros_formatados = '\n'.join(lista_livros)

      print(
         f'{self.nome}\n'
         f'{listas_livros_formatados}'
      )

   def buscar_livro(self, titulo):
      for l in self.livros:
         if l['titulo'] == titulo:
            print(f'Livro encontrado: {l['titulo']} ({l['autor']}) \n')
            return 
      
      print('Livro nao encontrado')
      
def ex02():
   bib = Biblioteca("Biblioteca Central")
   bib.adicionar_livro("1984", "George Orwell")
   bib.adicionar_livro("Dom Casmurro", "Machado de Assis")
   bib.listar_livros()

   bib.buscar_livro("1984")

   bib.remover_livro("1984")
   bib.listar_livros()

print('\n------------------------------------------------------------\n')

ex02()

print('\n------------------------------------------------------------\n')

'''
   Problema 3: Sistema de tarefas
      Enunciado:
         Crie classe Tarefa e ListaTarefas:

         Classe Tarefa:
            Atributos: descricao, concluida (False por padrão)
            Método: marcar_concluida()
            Método: exibir() mostra "[X] descricao" ou "[ ] descricao"

         Classe ListaTarefas:
            Atributos: tarefas (lista)
            Método: adicionar(descricao)
            Método: listar_todas()
            Método: listar_pendentes() - mostra não concludas
            Método: listar_concluidas() - mostra concludas
            Método: marcar_concluida(indice)

      Exemplo:
         lista = ListaTarefas()
         lista.adicionar("Estudar Python")
         lista.adicionar("Fazer exercícios")
         lista.adicionar("Revisar aula")

      lista.listar_todas()
      # 1. [ ] Estudar Python
      # 2. [ ] Fazer exercícios
      # 3. [ ] Revisar aula

      lista.marcar_concluida(1)
      lista.listar_pendentes()
      # 2. [ ] Fazer exercícios
      # 3. [ ] Revisar aula

      lista.listar_concluidas()
      # 1. [X] Estudar Python
'''

class Tarefa:
   def __init__(self, descricao):
      self.descricao = descricao
      self.concluido = False

   def marcar_concluida(self):
      self.concluido = True

   def exibir(self):
      status = '[x]' if self.concluido else '[ ]'
      return f'{status} {self.descricao}'
      
class ListaTarefas():
   def __init__(self):
      self.tarefas = []

   def adicionar(self, descricao):
      adc_tarefa = Tarefa(descricao)
      self.tarefas.append(adc_tarefa)

   def listar_todas(self):
      for i, tarefa in enumerate(self.tarefas):
         print(f'{i + 1}. {tarefa.exibir()}')

   def listar_pendentes(self):
      # for i, tarefa in enumerate(self.tarefas, start = 1):
      #    if not tarefa.concluido:
      #       tarefa.exibir(i)
      [print(f'{i + 1}. {tarefa.exibir()}') for i, tarefa in enumerate(self.tarefas) if not tarefa.concluido]
      
   def listar_concluidas(self):
      # for i,tarefa in enumerate(self.tarefas, start = 1):
      #    if tarefa.concluido:
      #       tarefa.exibir(i)
      [print(f'{i + 1}. {tarefa.exibir()}') for i, tarefa in enumerate(self.tarefas) if tarefa.concluido]

   def marcar_concluida(self, indice):
      index = indice - 1
      self.tarefas[index].marcar_concluida()

      
def ex03():
   lista = ListaTarefas()
   lista.adicionar("Estudar Python")
   lista.adicionar("Fazer exercícios")
   lista.adicionar("Revisar aula")

   lista.listar_todas()
   print('---')

   lista.marcar_concluida(1)
   lista.listar_pendentes()
   print('---')

   lista.listar_concluidas()

ex03()

'''
   Dificuldades?
   Problema 1: 
      Para calcular a nova média:
         multiplique a nota a ser adicionada pela quantidade de avaliadores atuais
         some o valor obtido com a nota atual
         aumente a quantidade de avaliadores em 1
         divida a soma pela nova quantidade de avaliadores
         atualize o valor do campo “avaliacao”.

   Problema 2: 
      Use lista interna para armazenar, cada livro pode ser dict {"titulo": ..., "autor": ...} e valide se livro existe antes de remover.

   Problema 3:
      Use enumerate(tarefas) para iterar por tarefas com seu índice.
      O método adicionar da ListaTarefas deve fazer um append em seu atributo “tarefas”
      Lembre se somar 1 no índice na hora de exibir, mas subtrair 1 no momento de excluir
      Para listar tarefas pendentes e concluídas, utilize list comprehension
      Para marcar a tarefa como concluída, identifique ela a partir do índice na lista (usando tarefa = tarefas.index(indice - 1), por exemplo) e depois chame o método tarefa.marcar_concluida().
'''