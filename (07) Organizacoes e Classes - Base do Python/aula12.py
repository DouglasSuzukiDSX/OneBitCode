# Aula12 - Encapsulamento e propriedades
class Conta:
   def __init__(self, titular, saldo):
      self.__saldo = saldo

   def printar(self):
      print(self.__saldo)

   def depositar(self, valor):
      if valor > 0:
         self.__saldo += valor

   def sacar(self, valor):
      if 0 < valor <= self.__saldo:
         self.__saldo -= valor

   def obter_saldo(self):
      return self.__saldo

conta = Conta('Joao', 1000)
# conta.__saldo = -9999 # Usuario pode naguncar os dados
# print(conta.__saldo) # -9999 invalido
# conta.printar()
conta.depositar(500)
print(conta.obter_saldo()) # 1500
conta.sacar(200)
print(conta.obter_saldo()) # 1300

class Conta2:
   def __init__(self, titular, saldo):
      self.__saldo = saldo

   @property
   def saldo(self):
      return self.__saldo

   @saldo.setter
   def saldo(self, valor):
      if(valor > 0):
         self.__saldo += valor
      elif valor <= self.__saldo:
         self.__saldo += valor

conta = Conta2('John', 1000)
conta.saldo = 2000
print(conta.saldo)
conta.saldo = -1500
print(conta.saldo)