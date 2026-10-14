# Aula10 - Classes: classmethod e staticmethod
class Caneta:
   def __init__(self, cor, tipo):
      self.cor = cor
      self.tipo = tipo
      self.esta_aberta = False
      pass

   def escrever(self, texto):
      if(not self.esta_aberta):
         print('A caneta esta fechada. Voce precisa abrir antes de escrever.')
         return 
      
      print(f'A caneta {self.cor} esta escrendo o seguinte texto.')
      print(texto)
      print(Caneta.verifica_tamanho_texto(texto))

   def alternar_abertura(self):
      self.esta_aberta = not self.esta_aberta

      print(f"{'Abrindo' if self.esta_aberta else 'Fechando'} a caneta")

   @staticmethod # Serve como uma funcao auxiliar
   def verifica_tamanho_texto(texto: str):
      if len(texto) > 50:
         return 'Texto muito grande'
      elif len(texto) > 25:
         return 'Texto medio'
      else:
         return 'Texto pequeno'

   @classmethod # Serve como uma alternativa para iniciar uma instancia
   def criar_por_texto(cls, texto: str):
      texto_limpo = texto.replace('caneta ', '')
      cor, tipo = texto_limpo.split(' ') 
      return cls(cor, tipo)

   def __str__(self): # Metodo que chamanda quando chamamos apenas a instancia num print por exemplo
      return f'Esta e a caneta {self.cor}'

caneta_azul = Caneta('azul', 'esferografica')
caneta_preta = Caneta('preta', 'gel')

caneta_azul.alternar_abertura()
caneta_azul.escrever('Um texto')

caneta_vermelha = Caneta.criar_por_texto('caneta vermelha esferografica')
caneta_vermelha.alternar_abertura()
caneta_vermelha.escrever('Ola')
print(caneta_vermelha)