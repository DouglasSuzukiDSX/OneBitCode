# Aula03 - Módulos built-in (parte 2)
from collections import Counter, namedtuple, deque
from operator import itemgetter

frutas = ['Maca', 'Banana', 'Uva', 'Pera', 'Uva', 'Maca', 'Uva', 'Banana']

contador = Counter(frutas) # Conta as ocorrencia dos termos
print(contador)

# =======================================

Pessoa = namedtuple('Pessoas', ['nome', 'idade']) # Da o nome pra tupla

pessoa1 = Pessoa('James', 21)
pessoa2 = Pessoa(nome='Mike', idade=35)

# =======================================

fila = deque([10, 20, 30, 40, 50, 60]) # Permite manipulao do comeco e final da fila
fila.append(70)
fila.appendleft(70)
print(fila)
fila.popleft()
fila.popleft()
fila.pop()
print(fila)

# =======================================

estudantes = {'Pedro': 21, 'Ana': 22, 'Roberto': 32, 'Claudio': 55}
ordenador = itemgetter(0) # Seleciona a 1 key, no caso o 'nome do aluno'

estudantes_ordenados = sorted(estudantes.items(), key=lambda x:x[1]) # Faz a ordenacao
estudantes_ordenados2 = sorted(estudantes.items(), key=ordenador) # Faz a ordenacao pelo nome
print(estudantes_ordenados)
print(estudantes_ordenados2)