import csv
from typing import List, Dict

def ler_csv(arquivo: str) -> List[Dict]:
   try:
      with open(arquivo, 'r', encoding='UTF-8') as documento:
         reader = csv.DictReader(documento)

         return list(reader)
   except FileNotFoundError:
      print(f'Erro: aquivo "{arquivo}" nao foi encontrado')
      return []

print(ler_csv('produtoss.csv'))

def calcular_totais(produtos: List[Dict]) -> List[Dict]:
   resultado = [
      {
         **produto,
         # 'total': float(produto['preco']) * int(produto['quantidade'])
         'total': float(produto.get('preco') or 0) * int(produto.get('quantidade') or 0)
      } 
      for produto in produtos
   ]

   return resultado

def escrever_csv(arquivo: str, produtos: List[Dict]) -> None:
   if not produtos:
      print('Nenhum produto para escrever')
      return

   campos = ['nome', 'preco', 'quantidade', 'total']

   try:
      with open(arquivo, 'w', encoding='utf-8') as documento:
         writer = csv.DictWriter(documento, fieldnames=campos)
         writer.writeheader()
         writer.writerows(produtos)

         print(f'Arquivo "{arquivo}" criado com sucesso!')
   except IOError as error:
      print(f'Error ao escrever arquivo: {error}')

produtos = ler_csv('produtos.csv')
produtos_com_totais = calcular_totais(produtos)
escrever_csv('produtos_totais.csv', produtos_com_totais)