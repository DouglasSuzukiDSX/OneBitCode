# Aula06 - Pip e módulos externos
import requests

resposta = requests.get('https://jsonplaceholder.typicode.com/users/1')

print(f'Status da requisicao: {resposta.status_code}')

if resposta.status_code != 200:
   print('Erro ao fazer a requisicao')
   exit()

dados_usuario = resposta.json()

print('\n --- Dados do Usuario ---')
print(f'Nome    : {dados_usuario['name']}')
print(f'Username: {dados_usuario['username']}')
print(f'Email   : {dados_usuario['email']}')
print(f'Cidade  : {dados_usuario['address']['city']}')
