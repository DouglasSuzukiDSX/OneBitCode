import requests
import json
from datetime import datetime

def obter_cotacoes():
   api = 'https://api.exchangerate-api.com/v4/latest/BRL'

   response = requests.get(api)

   data = response.json()
   
   return data['rates']

def salvar_json():
   data = obter_cotacoes()
   date_now = datetime.now().isoformat()
   contacoes = 'cotacoes.json'
   
   infos = {
      "timestamp": date_now,
      "moeda_base": "BRL",
      "taxas": {
         "USD": f'{data['USD']:.2f}',
         "EUR": f'{data['EUR']:.2f}',
         "GBP": f'{data['GBP']:.2f}'
      }
   }

   with open(contacoes, 'w', encoding='utf-8') as arquivo:
      data = json.dump(infos, arquivo, indent=4, ensure_ascii=False)

def ler_json(arquivo_json):
   try:
      with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
         cotacao = json.load(arquivo)

         print(cotacao)
   except FileNotFoundError:
      print(f'Nao foi possivel encontrar o arquivo {arquivo_json}')
   except Exception as error:
      print(f'Nao foi possivel ler arquivo {arquivo_json}')