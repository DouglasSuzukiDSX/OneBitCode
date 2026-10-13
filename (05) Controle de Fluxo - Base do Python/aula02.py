# Aula 02 - Condições com if, elif e else
idade = int(input('Digite sua idade: '))

'''if idade >= 18:
   print('Voce pode dirigir')
elif idade >= 16:
   print('Esta perto de dirigir, mas ainda nao pode')
else:
   print('Voce nao pode dirigir')'''

if idade < 18:
   print('Nao pode tirar carteira')
   exit() # Encerra oo programa

print('Emitindo CNH ...') # Codigo principal deve seguir pora da condicao

pode_dirigir = print('Sim') if idade >= 18 else print('Nao')