# Aula 04 - Laço for e while
frutas = ['maca', 'banana', 'laranja']

for fruta in frutas:
   print(fruta)

# for numero in range(0, 1001, 100): # start (default 0), final -1, steps
for numero in range(6): 
   if numero == 3:
      # break # Para
      continue

   print(numero)

for index, fruta in enumerate(frutas): # Retorna o index com o elemento
   print(index, fruta)

##############################################

contador = 1
while contador < 10:
   print(contador)
   contador += 1