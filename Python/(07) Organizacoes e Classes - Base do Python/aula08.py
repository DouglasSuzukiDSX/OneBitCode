# Aula08 - Resolução: módulos
import random
from collections import Counter
import re
import json

'''
   Problema 1: Sorteador de Brindes e Frequência

      Enunciado:
         Em um evento da OneBitCode, precisamos sortear 10 brindes de forma aleatória a partir de uma lista de opções disponíveis. Crie uma função que realize esses 10 sorteios e, no final, retorne um contador mostrando quantas vezes cada brinde foi sorteado.

      Exemplo:
         brindes_disponiveis = ["Camiseta", "Caneca", "Adesivo", "Chaveiro"]
         # O resultado deve rodar 10 sorteios aleatórios e totalizar

      sortear_e_contar(brindes_disponiveis)
         # Exemplo de Saída: {'Camiseta': 4, 'Adesivo': 3, 'Caneca': 2, 'Chaveiro': 1}
'''

brindes_disponiveis = ["Camiseta", "Caneca", "Adesivo", "Chaveiro"]

def sortear_e_contar(brindesLista: list):
   brindes = []
   brindes_qtt = 10

   while brindes_qtt != 0:
      brindes.append(random.choice(brindesLista))
      brindes_qtt -= 1

   # print(brindes)
   brindes_distribuidos = Counter(brindes)

   print(brindes_distribuidos)

sortear_e_contar(brindes_disponiveis)

'''
   Problema 2: Validador de Cupons com Regex
      Enunciado:
         Crie uma função que receba um texto contendo vários códigos de cupons de desconto e extraia apenas os cupons que seguem o padrão correto da empresa: 2 letras maiúsculas seguidas de exatamente 4 números (Exemplo: ONEBIT10 é inválido, mas PY1024 é válido).

      Exemplo:
         texto_compras = "Cupom de 20% usado: PY2024. Tentei usar o cupom antigo JS10, mas expirou. O novo é WEB9988 e o VIP é VP2026."
      pattern = r"\b[A-Z]{2}[0-9]{4}\b"

      filtrar_cupons(texto_compras)
      # Saída esperada: ['PY2024', 'VP2026']
'''

texto_compras = "Cupom de 20% usado: PY2024. Tentei usar o cupom antigo JS10, mas expirou. O novo é WEB9988 e o VIP é VP2026."

def filtrar_cupons(texto: str):
   pattern = r"\b[A-Z]{2}[0-9]{4}\b"

   txt = re.findall(pattern, texto)

   print(txt)

filtrar_cupons(texto_compras)

'''
   Problema 3: Filtro de Desenvolvedores JSON

      Enunciado:
         Você recebeu uma string em formato JSON contendo uma lista de alunos e as tecnologias que eles dominam. Converta essa string para estruturas nativas do Python e filtre o relatório para retornar apenas os nomes dos alunos que têm "Python" na sua lista de tecnologias.

      Dados:
         dados_alunos = [
            {"nome": "Arthur", "tecnologias": ["Python", "JavaScript"]},
            {"nome": "Ana", "tecnologias": ["Java", "C#"]},
            {"nome": "Léo", "tecnologias": ["React", "TypeScript", "Python"]},
            {"nome": "Beatriz", "tecnologias": ["Ruby"]}
         ]
         
      Saída esperada:
         ["Arthur", "Léo"]
'''

dados_alunos = '''[
      {"nome": "Arthur", "tecnologias": ["Python", "JavaScript"]},
      {"nome": "Ana", "tecnologias": ["Java", "C#"]},
      {"nome": "Léo", "tecnologias": ["React", "TypeScript", "Python"]},
      {"nome": "Beatriz", "tecnologias": ["Ruby"]}
]'''

def verificar():
   dados = json.loads(dados_alunos)

   alunos = []

   for aluno in dados:
      for tec in aluno['tecnologias']:
         if tec == 'Python':
            alunos.append(aluno['nome'])

   print(alunos)

verificar()

'''
   Dificuldades?
      Problema 1: Use um laço de repetição (for) que rode 10 vezes. Dentro dele, use random.choice() para escolher o brinde. Armazene os resultados em uma lista e, no final, passe essa lista para o Counter().

      Problema 2: Use o módulo re com a função re.findall(). Para o padrão (pattern), lembre-se que letras maiúsculas podem ser representadas por [A-Z] e a quantidade exata de dígitos por {4}.
      
      Problema 3: Use json.loads() para transformar a string tripla em uma lista de dicionários Python. Depois, itere sobre essa lista e use uma estrutura condicional (if) para checar se "Python" in aluno["tecnologias"].  
'''