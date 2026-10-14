import sys
from pathlib import Path
import pytest

sys.path.append(str(Path(__file__).resolve().parent.parent))

from aula03 import dobro, raiz_quadrada

# Formas para rodar:
   # => python -m pytest
      # => python -m pytest -v (tras mais informacoes e com o x para no primeiro erro)
   # => pytest
class Exemplo:
   pass

class Outro(Exemplo):
   pass
instancia_exemplo = Exemplo()

def test_dobro():
   assert dobro(5) == 10
   assert dobro(0) == 0
   assert dobro(-3) == -6
   assert isinstance(2, int)  # Verifica se termo e da classe iinformada
   assert isinstance(instancia_exemplo, Exemplo)  # Verifica se termo e da classe iinformada

def test_dobro_tipo_incorreto():
   with pytest.raises(TypeError):
      dobro('2')  # Verifica se a funcao levanta o erro de tipo

def test_raiz_quadrada():
   assert raiz_quadrada(16) == 4
   assert raiz_quadrada(1) == 1

   with pytest.raises(ValueError):
      raiz_quadrada(-1)