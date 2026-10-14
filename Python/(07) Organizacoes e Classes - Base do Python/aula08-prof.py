import random
from collections import Counter
import re
import json

QTD_SORTEIOS = 10

def sortear_e_contar(brindes: list) -> Counter:
   resultados = [random.choice(brindes) for _ in range(QTD_SORTEIOS)]

   return Counter(resultados)

brindes_disponiveis = ["Camiseta", "Caneca", "Adesivo", "Chaveiro"]
sorteio = sortear_e_contar(brindes_disponiveis)

print(dict(sorteio))

# =======================================

texto_compras = "Cupom de 20% usado: PY2024. Tentei usar o cupom antigo JS10, mas expirou. O novo é WEB9988 e o VIP é VP2026."
padrao = r"\b[A-Z]{2}[0-9]{4}\b"

def filtrar_cupons(texto: str):
   return re.findall(padrao, texto)

print(filtrar_cupons(texto_compras))

# =======================================

dados_alunos = '''[
   {"nome": "Arthur", "tecnologias": ["Python", "JavaScript"]},
   {"nome": "Ana", "tecnologias": ["Java", "C#"]},
   {"nome": "Léo", "tecnologias": ["React", "TypeScript", "Python"]},
   {"nome": "Beatriz", "tecnologias": ["Ruby"]}
]'''

alunos = json.loads(dados_alunos)
alunos_python = [aluno['nome'] for aluno in alunos if aluno['tecnologias'].count('Python') != 0]
alunos_pythonV2 = [aluno['nome'] for aluno in alunos if 'Python' in aluno['tecnologias']]
print(alunos_python)
print(alunos_pythonV2)