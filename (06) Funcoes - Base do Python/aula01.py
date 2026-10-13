# Aula01 - Funções: criando e reutilizando código


def calcular_area_quadrado(lado: int = 1):
   area = lado * lado

   print(f'Area: {area:.2f}')

calcular_area_quadrado(5)
calcular_area_quadrado(3)
calcular_area_quadrado(9)
calcular_area_quadrado()

def calcular_area_e_perimetro(lado):
   area = lado * lado
   perimetro = lado * 4
   return area, perimetro

area, perimetro = calcular_area_e_perimetro(5) 

print(f'Area: {area}, Perimetro: {perimetro}')