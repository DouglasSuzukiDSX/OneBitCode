# Aula 04 - Dicionários
nome = 'John'
idade = 25
email = 'john@email.com'
cidade = 'Sao Paulo'

pessoa = {'nome': 'John', 'idade': 25, 'email': 'john@email.com', 'cidade': 'Sao Paulo'}
# pessoa = dict(nome = 'John', idade = 25)

print(pessoa['nome'])
print(pessoa.get('documento', 'Nao encontrado')) # Busca o valor da chave, e caso nao encontrar ele retorna a mensagem de fallback

print(pessoa)
pessoa['nome'] = 'James' # Atualiza o dado
pessoa.update({email: 'james@email.com', 'company': 'fck'}) # Atualiza os dados
# del pessoa['idade'] # Deleta o dado
print(pessoa.pop('idade')) # Deleta o dado
print(pessoa)

print(pessoa.keys()) # Retorna todas as keys
print(pessoa.values()) # Retorna todos os valores

dados_lista = list(pessoa.items()) # Retorna os valores em tuplas
print(dados_lista[0][1]) 

print('nome' in pessoa)

usuario = {
   'nome': 'John', 
   'idade': 25,
   'endereco': {
      'rua': 'Rua A',
      'numero': 123,
      'cidade': 'Sao Paulo'
   }
}

loja = {
   'nome': 'Minha loja',
   'produtos': [
      { 'nome': 'Notebook', 'preco': 2500 },
      { 'nome': 'Mouse', 'preco': 50 },
      { 'nome': 'Teclado', 'preco': 120 },
   ]
}

print(loja['produtos'][0]['nome'])