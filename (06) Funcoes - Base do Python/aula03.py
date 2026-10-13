# Aula03 - Funções recursivas
def fatorial(n):
   # Caso base (para)
   if n == 0 or n == 1:
      return n

   # Caso recursivo (chama a si mesmo)
   return n * fatorial(n - 1)

print(fatorial(4))