# Aula01 - Lendo e escrevendo arquivos
import json
import csv
import glob

'''arquivo = open('nomes.txt')  # Abre o arquivo 
conteudo = arquivo.read()  # Lê o conteúdo do arquivo
print(conteudo)

arquivo.close()  # Fecha o arquivo'''

def readFile():
   with open('nomes.txt', 'r', encoding='utf-8') as arquivo:
      # conteudo = arquivo.read()  
      # print(conteudo) 

      # linhas = arquivo.readlines()  # Lê todas as linhas do arquivo e retorna uma lista
      # print(linhas)

      for linha in arquivo:
         print(linha.strip())  # Lê o arquivo linha por linha e remove espaços em branco no início e no final
# readFile()

def writeFile():
   with open('nomes.txt', 'w', encoding='utf-8') as arquivo: # Caso o arquivo não exista, ele será criado. Caso exista, o conteúdo será sobrescrito
      arquivo.write('Novo conteudo')
# writeFile()

def appendFile():
   with open('nomes.txt', 'a', encoding='utf-8') as arquivo: # Caso o arquivo não exista, ele será criado. Caso exista, o conteúdo será adicionado ao final do arquivo
      arquivo.write('\nTonho')

# appendFile()

def contar_linhas(arquivo):
   with open(arquivo) as f:
      return len(f.readlines())

def filtrar_palavras(arquivo, palavra):
   resultado = []

   with open(arquivo) as f:
      for linha in f:
         if palavra.lower() in linha.lower():
            resultado.append(linha.strip())   

   return resultado

# print(filtrar_palavras('nomes.txt', 'tonho'))

def write_json():
   with open('nomes.json', 'w', encoding='utf-8') as arquivo:
      dados = {
         'nome': 'Joao',
         'idade': 25,
         'skills': ['Python', 'Javascript']
      }

      json.dump(dados, arquivo, indent=4, ensure_ascii=False)  # Escreve o dicionário no arquivo em formato JSON
# write_json()

def read_json():
   with open('nomes.json', 'r', encoding='utf-8') as arquivo:
      usuario = json.load(arquivo)  # Lê o conteúdo do arquivo e retorna um dicionário

      print(usuario)
      print(type(usuario))
# read_json()

def write_csv():
   with open('nomes.csv', 'w', encoding='utf-8', newline='') as arquivo:
      dados = [
         ['Nome', 'Idade', 'Cidade'],
         ['Joao', 25, 'SP'],
         ['Maria', 30, 'RJ'],
         ['Pedro', 28, 'MG']
      ]

      writer = csv.writer(arquivo)
      writer.writerows(dados)  # Escreve as linhas no arquivo CSV
# write_csv()

def read_csv():
   with open('nomes.csv', 'r', encoding='utf-8') as arquivo:
      reader = csv.reader(arquivo)

      for linha in reader:
         print(linha)  # Lê o arquivo CSV linha por linha e retorna uma lista
read_csv()

def read_csv_2():  # Lê o arquivo CSV linha por linha e retorna um dicionário
   with open('nomes.csv', 'r', encoding='utf-8') as arquivo:
      reader = csv.DictReader(arquivo)

      for linha in reader:
         print(linha)  # Lê o arquivo CSV linha por linha e retorna um dicionário
# read_csv_2()

def write_csv_2():  # Escreve um arquivo CSV a partir de uma lista de dicionários
   with open('nomes.csv', 'a', encoding='utf-8', newline='') as arquivo:
      writer = csv.DictWriter(arquivo, fieldnames=['Nome', 'Idade', 'Cidade'])
      writer.writeheader()  # Escreve o cabeçalho do arquivo CSV
      writer.writerows([{'Nome': 'Max', 'Idade': 21, 'Cidade': 'TO'}])  # Escreve as linhas no arquivo CSV
# write_csv_2()

def show_files():
   for nome_arquivo in glob.glob('*.txt') + glob.glob('*.json'):  # Lista todos os arquivos .txt e .json do diretório atual
      print(nome_arquivo)
# show_files()

try:
   with open('nomes.txt', 'r', encoding='utf-8') as arquivo:
      pass
except FileNotFoundError as error:
   print(f'Error: {error}')
except IOError:
   print('Erro ao ler o arquivo')