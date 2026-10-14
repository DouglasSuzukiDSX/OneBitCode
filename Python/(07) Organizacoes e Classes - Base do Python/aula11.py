# Aula11 - Herança e polimorfismo
class Animal:
   def __init__(self, nome):
      self.nome = nome

   def pular(self):
      print(f'{self.nome} pulou')

   def fazer_som(self) -> str:
      return ''

class Cachorro(Animal):
   def __init__(self, nome):
      super().__init__(nome) # Chama o init da classe pai

   def fazer_som(self): # Poliformismo, aqui sobre escreve o metodo da classe pai
      return 'Au au'

class Gato(Animal):
   def __init__(self, nome):
         super().__init__(nome) # Chama o init da classe pai
   
   def fazer_som(self): # Poliformismo, aqui sobre escreve o metodo da classe pai
      return 'Miau'

   def atacar(self):
      return 'O gato esta arranhando'

cachorro = Cachorro('Amendoim')
cachorro.pular()
print(cachorro.fazer_som())

gato = Gato('Snowball')
print(gato.fazer_som())
print(gato.atacar())

# ===============================

class Funcionario:
   def __init__(self, nome, salario):
      self.nome = nome
      self.salario = salario

   def calcular_bonus(self):
      return self.salario * 0.1 # 10%

class Gerente(Funcionario):
   def calcular_bonus(self):
      return self.salario * 0.2 # 20% (diferente)

class Desenvelvedor(Funcionario):
   def calcular_bonus(self):
      return self.salario * 0.15 # 15% (diferente)

# Mesmo metodo, resultados diferentes
func = Funcionario('Joao', 3000)
ger = Gerente('Maria', 5000)
dev = Desenvelvedor('Pedro', 4000)

print(f'Funtionario...: R$ {func.calcular_bonus():.2f}') # $ 300.00
print(f'Gerente.......: R$ {ger.calcular_bonus():.2f}') # $ 1000.00
print(f'Desenvolvefdor: R$ {dev.calcular_bonus():.2f}') # $ 600.00

# ===============================

class MetodoPagamento:
   def processar_pagamento(self, valor):
      pass

class CartaoCredito(MetodoPagamento):
   def processar_pagamento(self, valor):
      taxa = valor * 0.003 # 3%

      return valor + taxa

class Pix(MetodoPagamento):
   def processar_pagamento(self, valor):
      return valor # Sem taxa

class Boleto(MetodoPagamento):
   def processar_pagamento(self, valor):
      taxa = 5.00 # Taxa fixa

      return valor + taxa

# Polimorfismo
metodos = [
   CartaoCredito(),
   Pix(),
   Boleto()
]

valor_original = 100

for metodo in metodos:
   final = metodo.processar_pagamento(valor_original)
   print(f'{metodo.__class__.__name__}: R$ {final:.2f}')
