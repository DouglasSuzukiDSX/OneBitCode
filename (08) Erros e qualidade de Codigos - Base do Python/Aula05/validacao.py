# Resolucao do exercicios - Prof
import re
def validar_idade(idade: int) -> None:
   if not isinstance(idade, int):
      raise TypeError('A idade deve ser do tipo inteito (int)')
   if idade < 0:
      raise ValueError('A idade nao pode ser negativa')
   if idade > 150:
      raise ValueError('A idade deve ser realista')

def validar_senha(senha: str) -> None:
   letra_pattern = r'[a-zA-Z]{1}'
   numero_pattern = r'\d'

   if not isinstance(senha, str):
      raise TypeError('A senha deve ser do tipo string (str)')
   if not senha:
      raise ValueError('A senha nao pode ser vazia')
   if len(senha) < 8:
      raise ValueError('A senha deve ter pelo menos 8 caracteres')
   if not re.search(letra_pattern, senha) or not re.search(numero_pattern, senha):
      raise ValueError('A senha deve ter no minimo 1 letra e 1 numero')

try:
   # validar_idade(25)  # OK (retorna None)
   # validar_idade(-2)  # ValueError

   # validar_senha('12345678')
   # validar_senha('1234567')
   validar_senha('abc12345')
except ValueError as error:
   print(f'Erro: {error}')