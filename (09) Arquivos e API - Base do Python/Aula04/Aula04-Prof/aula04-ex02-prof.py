import json, requests
from datetime import datetime
from typing import List, Dict, Optional

def obter_cotacoes(moeda_base: str, moedas: list) -> Dict:
   url = f'https://api.exchangerate-api.com/v4/latest/{moeda_base}'

   try:
      resposta = requests.get(url, timeout=5)
      resposta.raise_for_status()

      dados = resposta.json()
      taxas = dict()

      for moeda in moedas:
         if moeda in dados['rates']:
            taxas[moeda] = dados['rates'][moeda]
         else:
            print(f'Aviso: moeda {moeda} nao enconta')

      return taxas
   
   except requests.exceptions.Timeout:
      print('Error: requisicao expirou')
      return dict()
   except requests.exceptions.ConnectionError:
      print('Erro: conexao falhou')
      return dict()
   except requests.exceptions.HTTPError as e:
      print(f'Erro HTTP: {e}')
      return dict()

def salvar_json(arquivo: str, moeda_base: str, taxas: Dict) -> None:
   dados = {
      "timestamp": str(datetime.now()),
      "moeda_base": moeda_base,
      "taxas": taxas
   }

   try:
      with open(arquivo, 'w', encoding='utf-8') as documento:
         json.dump(dados, documento, indent=4, ensure_ascii=False)

      print(f'Arquivo "{arquivo}" criado scom sucesso!')
   except IOError as error:
      print(f'Erro ao escrever arquivo: {error}')
moeda_base = 'BRL'
moedas = ['USD', 'EUR', 'GBP']
taxas = obter_cotacoes(moeda_base, moedas)

if not taxas: exit()
# print(taxas)
salvar_json('cotacoes.json', moeda_base, taxas)

for moeda, taxa in taxas.items():
   print(f'1 {moeda_base} = {taxa:.4f} {moeda}')