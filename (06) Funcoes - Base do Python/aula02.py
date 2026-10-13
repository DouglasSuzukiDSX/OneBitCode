# Aula02 - Argumentos avançados: *args e kwargs

def somar(nome, *numeros): #*args
   return sum(numeros)

print(somar(1, 2, 3))

def criar(**usuario):
   print(type(usuario))
   print(usuario)

   for chave, valor in usuario.items():
      print(f'{chave}: {valor}')

criar(idade = 2, nome = 'James')

def funcao_completa(a, b, *args, chave1 = 10, **kwargs):
   # Funcao com todos os tipos de argumentos
   print(f'a = {a}, b = {b}')
   print(f'args = {args}')
   print(f'chave1 = {chave1}')
   print(f'kwargs = {kwargs}')

funcao_completa(1, 2, 3, 4, 5, chave1 = 20, nome = 'James', idade = 25)

# * => Faz uma copia raza dos argumentos
frutas = ['laranja', 'maca', {'abc': 123}]
novas_frutas = [*frutas, 'abacaxi']
novas_frutas[2].update({'def': 456})
print(frutas)
print(novas_frutas)

def exemplo(lista: list):
   lista.append(123)

lista2 = [4, 5, 6]
exemplo(lista2)
print(lista2)