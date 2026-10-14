# Aula06 - Resolução (Professor): conta letras | verifica par e ímpar | transforma lista

'''
   Problema 1: Contar letras

   Enunciado:
      Crie uma função que conta quantas letras (ignorando espaços e pontuações) uma palavra ou frase tem.

   Exemplo:
      contar_letras("Olá Mundo!") # 8
      contar_letras("Python")     # 6
      contar_letras("A B C")      # 3
'''

def contar_letras(texto: str):
   contador = 0

   for letra in texto:
      if(letra.isalpha()): contador += 1

   return contador

print(contar_letras("Olá Mundo!")) # 8
print(contar_letras("Python"))     # 6
print(contar_letras("A B C"))      # 3

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

def eh_par(numero: int) -> bool:
   return numero % 2 == 0

def filtra_pares(numeros: list) -> list:
   return [numero for numero in numeros if eh_par(numero)]

def filtra_impares(numeros: list) -> list:
   return [numero for numero in numeros if not eh_par(numero)]

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(filtra_pares(numeros))
print(filtra_impares(numeros))

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

produtos = [
   {"nome": "Notebook", "preco": 2500},
   {"nome": "Mouse", "preco": 50},
   {"nome": "Teclado", "preco": 150},
   {"nome": "Monitor", "preco": 800}
]

def aplicar_desconto(preco: int, desconto_pct: float = 20.0) -> float:
   preco_reduzido = preco * (1 - desconto_pct / 100)

   return preco_reduzido

produtos_com_desconto = []

for produto in produtos:
   produto_com_desconto = produto
   produto_com_desconto.update({ 'preco': aplicar_desconto(produto_com_desconto['preco']) })
   produtos_com_desconto.append(produto_com_desconto)

print(produtos_com_desconto)

'''
   Dificuldades?
      Problema 1: Itere pela string, use isalpha() para verificar se é letra.
      Problema 2: Use % (módulo) para verificar par/ímpar, use list comprehension.
      Problema 3: Use função que aplica desconto, ou list comprehension, desconto de 20% = preco * 0.8.
'''