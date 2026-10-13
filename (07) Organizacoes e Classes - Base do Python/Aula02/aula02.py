# Aula02 - Módulos built-in (parte 1)
import webbrowser
import json
import random

# webbrowser.open('youtube.com') # => Abre a pagina

instrutor = {
   "nome": "John Doe",
   "cargo": "Lider de Comunidade",
   "tecnologias": ["Python", "Javascript"],
   "ativo": True
}

jsonString = json.dumps(instrutor, ensure_ascii=False, indent = 3)
print(jsonString)

dados_api = '{ "curso": "Python", "alunos": 1500, "ativo": true }'
dados_dict = json.loads(dados_api)
print(dados_dict['alunos'])

numero_sorteado = random.randint(1, 10)
print(numero_sorteado)

alunos = ['Mike', 'James', 'John', 'Marie']

sorteado = random.choice(alunos) # Escolhe um
sorteados = random.sample(alunos, 2) # Escolhe quantos forem informados

print(sorteado)
print(sorteado)
print(sorteados)

cartas = ['As', 'Rei', 'Valete', 'Dama']
random.shuffle(cartas) # Embaralha
print(cartas )