import sys
from pathlib import Path
import pytest

sys.path.append(str(Path(__file__).resolve().parent.parent))

from aula05 import validar_idade, validar_senha

class Usuario:
   def __init__(self, idade, senha):
      self.idade = idade
      self.senha = senha

@pytest.fixture
def usuario():
   return Usuario(30, 'senha123')

@pytest.fixture
def usuario2():
   return Usuario(-30, 'senha')

def test_idade_valida(usuario):
   assert validar_idade(usuario.idade) is None

def test_idade_negativa(usuario2):
   with pytest.raises(ValueError):
      validar_idade(usuario2.idade)

def test_validar_senha_valida(usuario):
   assert validar_senha(usuario.senha) is None

def test_validar_senha_invalida(usuario2):
   with pytest.raises(ValueError):
      validar_senha(usuario2.senha)