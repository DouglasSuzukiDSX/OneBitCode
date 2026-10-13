# Aula09 - Introdução a classes e objetos
class Caneta:
   def __init__(self, cor, tipo):
      self.cor = cor
      self.tipo = tipo
      pass

   def escrever(self, texto):
      print(f'A caneta {self.cor} esta escrendo o seguinte texto.')
      print(texto)

   def __str__(self): # Metodo que chamanda quando chamamos apenas a instancia num print por exemplo
      return f'Esta e a caneta {self.cor}'

caneta_azul = Caneta('azul', 'esferografica')
caneta_preta = Caneta('preta', 'gel')

print(caneta_azul.tipo) 
print(caneta_preta.tipo) 

caneta_azul.escrever('Esta frase foi escrito com a caneta azul')
caneta_preta.escrever('Assinando documento...')

print(caneta_azul)