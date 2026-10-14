# Aula 05 - List comprehension
numeros = [1, 2, 3, 4, 5]
'''dobrados = []

for numero in numeros:
   dobrados.append(numero * 2)

print(dobrados)'''

dobrados = [numero * 2 for numero in numeros]
pares= [numero for numero in numeros if numero % 2 == 0]
impares= [numero for numero in numeros if numero % 2 != 0]
print(dobrados)
print(pares)
print(impares)

# Flatten (desalinhar)
matriz = [ [1, 2], [3, 4], [5, 6] ]
flat = [n for linha in matriz for n in linha]
print(flat)

numeros = [1, 2, 2, 3, 3, 3]
unicos = { n for n in numeros if n % 2 == 2 }
print(unicos)

nomes = ['Joao', 'Maria', 'Pedro']
ids = { nome: i for i, nome in enumerate(nomes) }
print(ids)