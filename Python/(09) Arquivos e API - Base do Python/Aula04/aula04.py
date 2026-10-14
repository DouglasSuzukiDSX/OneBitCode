# Aula04 - Resolução: processador de arquivos | consultor de API

from aula04_ex01 import escrever_csv, calcular_totais, ler_csv
from aula04_ex02 import salvar_json, ler_json

'''
Problema 1: Processador de CSV
   Enunciado:
      Crie um programa que:
         - Lê arquivo CSV com dados de produtos (nome, preço, quantidade)
         - Calcula valor total (preço * quantidade) para cada produto
         - Escreve novo CSV com coluna de total
         - Funções: ler_csv(), calcular_totais(), escrever_csv()

      Arquivo entrada: produtos.csv
         nome,preco,quantidade
         Notebook,2500,2
         Mouse,50,10
         Teclado,150,5

      Arquivo saída esperada: produtos_totais.csv
         nome,preco,quantidade,total
         Notebook,2500,2,5000
         Mouse,50,10,500
         Teclado,150,5,750
'''

def ex01():
   produtos = 'produtos.csv'
   produtos_totais = 'produtos_totais.csv'

   dados = [
      ['nome','preco','quantidade'],
      ['Notebook',2500,2],
      ['Mouse',50,10],
      ['Teclado',150,5]
   ]

   escrever_csv(produtos, dados)
   escrever_csv(produtos_totais, calcular_totais(produtos))

   ler_csv(produtos)
   ler_csv(produtos_totais)

ex01()

'''
   Problema 2: Consultor de API de cotação
      Enunciado:
         Crie um programa que:
            Aceita lista de moedas (ex: ["USD", "EUR", "GBP"])
            Faz requisição para API de cotação
            Salva resultado em JSON com timestamp
            Funções: obter_cotacoes(), salvar_json()

      **API: https://api.exchangerate-api.com/v4/latest/BRL**

      Saída esperada: cotacoes.json
         {
            "timestamp": "2026-06-30T18:50:00.123456",
            "moeda_base": "BRL",
            "taxas": {
               "USD": 0.19,
               "EUR": 0.18,
               "GBP": 0.15
            }
         }
'''

def ex02():
   salvar_json()
   ler_json('cotacoes.json')
   
ex02()

'''
   Dificuldades?
      Problema 1:
         Use csv.DictReader para ler
         Use csv.DictWriter para escrever
         Converta preço/quantidade para número
         Trate erros de arquivo

      Problema 2:
         Use requests.get() com timeout
         Verifique status_code
         Extraia do JSON a taxa para cada moeda
         Use datetime.now().isoformat()
         Trate erros de conexão
'''