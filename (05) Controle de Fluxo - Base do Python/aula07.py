# Aula 07 - Resolução: lançamento de foguete | tabuada | filtro de dados

'''
   Problema 1: Contador regressivo (Lançamento de foguete)
   Enunciado:

      Faça um programa que faz contagem regressiva de 10 até 0 e depois imprime "🚀 LANÇAMENTO!".

      Exemplo de saída:

      10
      9
      8
      7
      6
      5
      4
      3
      2
      1
      0
      🚀 LANÇAMENTO!
'''

def launch():
   counter = 10

   while counter >= 0:
      print(counter)

      if counter == 0:
         print('🚀 LANÇAMENTO!')
         exit()
   
      counter -= 1

# launch()

'''
   Problema 2: Tabuada
   Enunciado:

      Leia um número (1-10) e imprima sua tabuada de 1 até 10.

   Exemplo de entrada e saída:

   Digite número: 7

   Tabuada do 7:
   1 x 7 = 7
   2 x 7 = 14
   3 x 7 = 21
   4 x 7 = 28
   5 x 7 = 35
   6 x 7 = 42
   7 x 7 = 49
   8 x 7 = 56
   9 x 7 = 63
   10 x 7 = 70
'''

def mult_table():
   num = int(input('Digite um numero de 1 a 10 para imprimir sua tabuada: '))
   index = 1

   while index <= 10:
      print(f'{num} * {index} = {num * index}')
      index += 1

# mult_table()

'''
   Problema 3: Filtro de dados
   Enunciado:

      Dada uma lista de produtos com preço, filtre os que custam menos de R$ 100 e imprima:

   Nome
   Preço
   Total com imposto (10%)

   Dados:

   produtos = [
      {"nome": "Mouse", "preco": 50},
      {"nome": "Teclado", "preco": 150},
      {"nome": "Monitor", "preco": 300},
      {"nome": "Webcam", "preco": 80},
      {"nome": "Mousepad", "preco": 30}
   ]

   Exemplo de saída:

   Produtos abaixo de R$ 100:
   - Mouse: R$ 50.00 (com imposto: R$ 55.00)
   - Webcam: R$ 80.00 (com imposto: R$ 88.00)
   - Mousepad: R$ 30.00 (com imposto: R$ 33.00)

   Total de produtos: 3
'''

def filteredData():
   produtos = [
      {"nome": "Mouse", "preco": 50},
      {"nome": "Teclado", "preco": 150},
      {"nome": "Monitor", "preco": 300},
      {"nome": "Webcam", "preco": 80},
      {"nome": "Mousepad", "preco": 30}
   ]

   filteredProducts = []

   for produto in produtos:
      if(produto['preco'] < 100):
         filteredProducts.append(produto)

   print('Produtos abaixo de R$ 100:\n')

   for pdt in filteredProducts:
      pdtName = pdt['nome']
      pdtPrice= pdt['preco']
      tax = pdt['preco'] * 0.10
      pdtTax = pdtPrice + tax

      print(f'- {pdtName}: R$ {pdtPrice:.2f} (com imposto: R$ {pdtTax:.2f})')

   print(f'\nTotal de produtos: {len(filteredProducts)}')

# filteredData()

'''
   Dificuldades?
      Problema 1: Use range(10, -1, -1) ou while com contador decrescente
      Problema 2: for i in range(1, 11): depois print(f"{i} x {numero} = {i * numero}")
      Problema 3: Itere produtos, filtre com if, calcule imposto
'''

# Resolucao do prof
print('Contagem regressiva')

for numero in range(10, -1, -1):
   print(numero)

print('🚀 LANÇAMENTO!')

numero = int(input('Digite um numero (1-10): '))

# ==============================

if numero > 10 or numero < 1:
   print('Numero invalido. Insira um numero entre 1 e 10')
   exit()

print(f'Tabuada do {numero}: ')

for i in range(1,11):
   resultado = numero * i
   print(f'{i} x {numero} = {resultado}')

# ==============================

produtos = [
   {"nome": "Mouse", "preco": 50},
   {"nome": "Teclado", "preco": 150},
   {"nome": "Monitor", "preco": 300},
   {"nome": "Webcam", "preco": 80},
   {"nome": "Mousepad", "preco": 30}
]

print('Produtos abaixo de R$ 100: ')

for produto in produtos:
   if produto['preco'] <= 100:
      preco_imposto = produto['preco'] * 1.1

      print(f'- {produto['nome']}: R$ {produto['preco']:.2f} (com imposto> R$ {preco_imposto:.2f})')