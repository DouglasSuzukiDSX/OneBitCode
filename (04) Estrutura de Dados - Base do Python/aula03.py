# Aula 03 - Tuplas e sets
lista = ['Computador', 'Mouse', 'Teclado']
tupla = ('Computador', 'Mouse', 'Teclado')

print(tupla[0])
print(tupla.count('Computador'))

tupla2 = (42,)
print(tupla2)

numeros = {1, 2, 3, 3, 2, 1} # Set => Nao permite valores repetidos
numeros = set([1, 2, 3, 3, 2, 1]) # Set => Tambem converte tuple para set
print(type(numeros), numeros)

nomes = {'James'}
print(nomes)
nomes.add('John') # Adiciona um elemento
print(nomes)

ferramentas = {'Martelo', 'Serrote', 'Furadeiras', 'Chave de fendas'}
print(ferramentas)
ferramentas.update({'Serrote', 'Alicate'})
ferramentas.remove('Serrote') # Remove mas da erro se o elemento nao existir
ferramentas.discard('Serrote') # Remove sem erro caso o elemento nao existe
print(ferramentas)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

resultado = set1.union(set2) # Une sem repetir elementos
print(resultado)

resultado2 = set1.intersection(set2) # Retorna os elementos em comum
print(resultado2)

resultado3 = set1.difference(set2) # Retorna os elementos os elementos de set1 que nao estao no set2
print(resultado3)

# Dados com duplicados
emails = [
   'jhon@email.com',
   'jane@email', 
   'jhon@email.com', # Duplicado
   'max@email.com',
   'jane@email' # Duplicado
]

# Remove duplicatas
emails_unicos = set(emails)
print(emails_unicos) # => {'jane@email', 'max@email.com', 'jhon@email.com'}

# Converte de volta para lista (se precisar ordem)
emails_unicos_lista = list(emails_unicos)

# Clientes que compraram em Janeiro 
janeiro = {'John', 'Jane', 'Max', 'Cris'}

# Clientes que compraram em Fevereiro
fevereiro = {'Jane', 'Max', 'James', 'Tyler'}

# Quem compreou em janeiro mas nao em fevereiro
so_janeiro = janeiro.difference(fevereiro)
print(so_janeiro) # {'Cris', 'John'}