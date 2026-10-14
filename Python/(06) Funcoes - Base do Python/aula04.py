# Aula04 - Funções lambda e funções de ordem superior

# Lambda => Funcao anonima
def dobro(x):
   return x * 2

dobro2 = lambda x: x * 2

print(dobro(4))
print(dobro2(4))

pessoas = [
   { 'nome': 'Shanks', 'idade': 25 },
   { 'nome': 'Kaido', 'idade': 30 },
   { 'nome': 'BigMom', 'idade': 20 }
]

resultado = sorted(pessoas, key = lambda p: p['idade'])

print(resultado)

numeros = [1, 2, 3, 4, 5]

resultado = list(map(lambda x: x * 2, numeros))
print(resultado)

# High Order Funcion (Funcao de Ordem superior) => Funcao que recebe outra funcao como parametro
def aplicar_operacao(a: int, b: int, operacao: function) -> int:
   return(operacao(a, b))

resultado_soma = aplicar_operacao(4, 6, lambda num1, num2: num1 + num2)
resultado_multiplicacao = aplicar_operacao(4, 6, lambda num1, num2: num1 * num2)
print(resultado_soma)
print(resultado_multiplicacao)