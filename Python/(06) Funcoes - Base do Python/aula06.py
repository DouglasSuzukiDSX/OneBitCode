# Aula06 - Resolução: conta letras | verifica par e ímpar | transforma lista

'''
   Problema 1: Contar letras

   Enunciado:
      Crie uma função que conta quantas letras (ignorando espaços e pontuações) uma palavra ou frase tem.

   Exemplo:
      contar_letras("Olá Mundo!") # 8
      contar_letras("Python")     # 6
      contar_letras("A B C")      # 3
'''

# Minha resolucao
'''def contar_letras(content: str):
   content = content.replace(' ', '').strip()

   if not content.isalpha():
      return print('O conteudo fornecido nao e uma string')
   
   return print(len(content))

contar_letras("Olá Mundo!") # 8
contar_letras("Python")     # 6
contar_letras("A B C")      # 3
'''


# =====================================

'''
   Problema 2: Verifica par e ímpar

   Enunciado:
      Crie funções que verificam se um número é par ou ímpar, filtrando-os.

   Exemplo:
      numeros = [1, 2, 3, 4, 5, 6, 7, 8]
      filtra_pares(numeros)  # [2, 4, 6, 8]
      filtra_impares(numeros) # [1, 3, 5, 7]
'''

def filterNumbers(numbers):
   evenList = []
   oddList = []

   for num in numbers:
      evenList.append(num) if num % 2 == 0 else oddList.append(num)

   filtra_pares(evenList)
   filtra_impares(oddList)
         
def filtra_pares(numbers):
   return print(f'Pares: {numbers}')

def filtra_impares(numbers):
      return print(f'Impares: {numbers}')

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
filterNumbers(numeros)

# =====================================

'''
   Problema 3: Transforma lista

   Enunciado:
      Dada uma lista de produtos com preço, aplique desconto de 20% e crie nova lista com preços reduzidos.

   Dados:
      produtos = [
         {"nome": "Notebook", "preco": 2500},
         {"nome": "Mouse", "preco": 50},
         {"nome": "Teclado", "preco": 150},
         {"nome": "Monitor", "preco": 800}
      ]

   Saída esperada:
      [
         {"nome": "Notebook", "preco": 2000.0},
         {"nome": "Mouse", "preco": 40.0},
         {"nome": "Teclado", "preco": 120.0},
         {"nome": "Monitor", "preco": 640.0}
      ]
'''
def listTransform():
   produtos = [
      {"nome": "Notebook", "preco": 2500},
      {"nome": "Mouse", "preco": 50},
      {"nome": "Teclado", "preco": 150},
      {"nome": "Monitor", "preco": 800}
   ]

   productsWithDiscount = []

   for pdt in produtos:
      priceWithDisccount = pdt['preco'] * 0.8

      prdFormatted = {"nome": pdt['nome'], "preco": priceWithDisccount}

      productsWithDiscount.append(prdFormatted)

   print(productsWithDiscount)

listTransform()

'''
   Dificuldades?
      Problema 1: Itere pela string, use isalpha() para verificar se é letra.
      Problema 2: Use % (módulo) para verificar par/ímpar, use list comprehension.
      Problema 3: Use função que aplica desconto, ou list comprehension, desconto de 20% = preco * 0.8.
'''