# Aula 05 - Principais métodos de strings
texto = 'python'

print(texto.upper()) # Maiusculo
print(texto.lower()) # Minusculo

email = 'email@email.com        '
print(email.strip()) # Remove espaços em branco no inicio e no final

texto2 = 'Hello World'
print(texto2.replace('World', 'Python')) # Substitui uma palavra por outra
print(texto2.find('o')) # Retorna a posição da primeira ocorrência de uma letra ou palavra
print(texto2.count('o')) # Retorna a quantidade de ocorrências de uma letra ou palavra

print('123'.isdigit()) # True (so numeros)
print('abc'.isdigit()) # False
print('abc'.isalpha()) # True (so letras)
print('abc123'.isalpha()) # False
print('abc123'.isalnum()) # True (so letras ou numeros)
print('abc 123'.isalnum()) # False 
