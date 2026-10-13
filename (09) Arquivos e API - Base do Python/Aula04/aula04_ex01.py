import csv

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

def ler_csv(arquivo_csv, print_item = True):
   items = []

   try:
      with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
         reader = csv.reader(arquivo)
         # next(reader, None)  # Pula o cabeçalho (nome, preco, quantidade)

         print(f'---------- Arquivo {arquivo_csv} ----------') if print_item else ''

         for item in reader:
            items.append(item)

            if print_item:
               print(item)

         print(f'---------- Fim do arquivo {arquivo_csv} ----------\n') if print_item else ''

      return items
   except FileNotFoundError:
      print(f'Nao foi possivel encontrar o arquivo {arquivo_csv}') 
   except:
      print(f'Nao foi possivel ler arquivo {arquivo_csv}')

def calcular_totais(arquivo_csv):
   dados_totais = [
      ['nome','preco','quantidade', 'total']
   ]
   
   try:
      items = ler_csv(arquivo_csv, False)
      for item in items:
         if not item or item[0] == 'nome':  # Pula linhas vazias ou cabeçalhos que tenham sobrado
            continue

         total = float(item[1]) * int(item[2])

         dados_totais.append([*item, total])

      return dados_totais
   except FileNotFoundError:
      print(f'Nao foi possivel encontrar o arquivo {arquivo_csv}')
   except Exception as error:
      print(f'Erro ao processar os dados do arquivo {arquivo_csv}: {error}')

def escrever_csv(nome_csv, dados):
   nome_arquivo = f'{nome_csv}'

   try:
      with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
         writer = csv.writer(arquivo)
         writer.writerows(dados)

      print(f'Dados escritos no arquivo {nome_arquivo}\n')
   except Exception as error:
      print(f'Erro escrever no arquivo csv {nome_arquivo}: {error}\n')
