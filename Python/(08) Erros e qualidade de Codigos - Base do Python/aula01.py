# Aula01 - Try/except - tratamento de erros
try:
   numeros = [1, 2, 3]
   print(numeros[1])
except IndexError as error:
   print(f'Esse index nao existe {error}')
except ValueError:
   print('Valor nao permitido')
except ZeroDivisionError:
   print('Voce nao pode dividir por zero')
except Exception:
   print('Erro desconhecido')
else:
   print('passou')
finally:
   print('Sempre executa')

print('Continua')

def converter_int(valor):
   try:
      return int(valor)
   except ValueError:
      print(f'"{valor}" nao e numero')
   except TypeError:
      print(f'Tipo {type(valor)} nao pode ser convertido')
      return None

print(converter_int('123'))
print(converter_int('abc'))
print(converter_int(None))