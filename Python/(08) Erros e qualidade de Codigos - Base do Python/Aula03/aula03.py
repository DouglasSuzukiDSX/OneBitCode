# Aula03 - Testes unitários com pytest
import math
import pytest

def dobro(numero: int) -> int:
   if not isinstance(numero, int):
      raise TypeError('Tipo invalido')
   
   return numero * 2

def raiz_quadrada(numero: int):
   return math.sqrt(numero)

print(dobro(5))

class ContaBancaria:
   def __init__(self, titular, saldo_inicial=0):
      self.titular = titular
      self._saldo = saldo_inicial

   def depositar(self, valor):
      if valor <= 0:
         raise ValueError("O valor do depósito deve ser positivo.")
      self._saldo += valor

   def sacar(self, valor):
      if valor > self._saldo:
         raise ValueError("Saldo insuficiente para o saque.")
      self._saldo -= valor

   @property
   def saldo(self):
      return self._saldo

# Fixture que prepara o ambiente para os testes abaixo
@pytest.fixture
def conta():
   return ContaBancaria("João", 1000)

# Testes limpos e focados, recendo a conta configurada (faz o teste e reseta)
def test_depositar_valido(conta):
   conta.depositar(500)
   assert conta.saldo == 1500

def test_depositar_negativo_levanta_erro(conta):
   with pytest.raises(ValueError):
      conta.depositar(-100)

def test_sacar_valido(conta):
   conta.sacar(200)
   assert conta.saldo == 800

def test_sacar_mais_que_saldo(conta):
   with pytest.raises(ValueError):
      conta.sacar(2000)

def test_saldo_inicial(conta):
   assert conta.saldo == 1000