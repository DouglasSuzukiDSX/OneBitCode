# Aula 02 - Listas: métodos essenciais

frutas = ['maca', 'banana']

print(frutas)
frutas.append('laranja') # Insere no final da lista
frutas.insert(2, 'morango') # Insere o elemento na posicao informada
# frutas.remove('laranja') # Remove o elemento
# frutas.pop(1) # Remove o elemento na posicao informada

print(frutas)
# index = int(input('Qual index deseja remover? '))
# fruta_removida = frutas.pop(index) # Remove o elemento na posicao informada
# print(f'A fruta que seja removida sera? {fruta_removida}')

numeros = [4, 5, 2, 9, 7, 1]
numeros.sort(reverse=True)
print(numeros)

print(frutas.index('banana'))

frutas_texto = ' e '.join(frutas)
print(frutas_texto)

frutas2 = 'maca, banana, laranja'
print(frutas2.split(', '))

frutas_verdes = ['limao']
frutas_vermelhas = ['maca', 'morango']
frutas_lista = frutas_verdes + frutas_vermelhas
print(frutas_lista)