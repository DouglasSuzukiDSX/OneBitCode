# Aula 07 - Resolução: antecessor e sucessor | média de notas | manipulação de string
# Exercício: Antecessor e sucessor | Média de notas | Manipulação de string

# Neste exercício você vai praticar tudo que aprendeu: tipos, input, operadores, strings, métodos.

'''
   Problema 1: Antecessor e Sucessor
   Enunciado:

   Leia um número inteiro e imprima:

   O número
   Seu antecessor (n - 1)
   Seu sucessor (n + 1)
   Exemplo de entrada e saída:

   Digite um número: 5

   Número: 5
   Antecessor: 4
   Sucessor: 6
'''

def ex01():
   num = int(input('Digite um numero: '))

   print(f'O antecessor de {num} e: {num - 1}')
   print(f'O sucessor de {num} e: {num + 1}')

# ex01()

#########################################################

'''
   Problema 2: Média de 3 notas
   Enunciado:

   Leia 3 notas de um aluno (valores entre 0 e 10) e calcule a média.

   Exemplo de entrada e saída:

   Nota 1: 7.5
   Nota 2: 8.0
   Nota 3: 6.5

   Média: 7.33
'''

def ex02():
   note1 = float(input('Digite a note 1: '))
   note2 = float(input('Digite a note 2: '))
   note3 = float(input('Digite a note 3: '))

   avg = (note1 + note2 + note3) / 3

   print(f'A medias da notas e: {avg:.2f}') 

# ex02()

#########################################################

'''
   Problema 3: Manipulação de string
   Enunciado:

   Leia um nome completo e:

   Imprima em MAIÚSCULA
   Imprima em minúscula
   Contar quantas letras tem
   Extrair e imprimir as 3 primeiras letras
   Extrair e imprimir as 3 últimas letras
   Substituir espaços por underscore
   Exemplo de entrada e saída:

   Nome: João Silva

   MAIÚSCULA: JOÃO SILVA
   minúscula: joão silva
   Quantidade de letras: 10
   Primeiras 3: Joã
   Últimas 3: lva
   Com underscore: João_Silva
'''

def ex03():
   name = input('Digite um nome com sobrenome: ')

   nameUpper = name.upper()
   nameLower = name.lower()
   nameLength = len(name)
   firstTreeLetters = name[0:3]
   lastTreeLetters = name[-3:]
   withUnderscore = name.replace(' ', '_')

   print(f'MAIÚSCULA: {nameUpper}')
   print(f'minúscula: {nameLower}')
   print(f'Quantidade de letras: {nameLength}')
   print(f'Primeiras 3: {firstTreeLetters}')
   print(f'Últimas 3: {lastTreeLetters}')
   print(f'Com underscore: {withUnderscore}')

ex03()

'''
Dificuldades?
Problema 1: Use input() e converta com int()
Problema 2: float() pra notas com casas decimais e use :.2f pra formatação
Problema 3: .upper(), .lower() , len() pra contar, Slicing [0:3] e [-3:] , .replace()
'''