# Aula 07 - Resolução: Informações de pedidos

'''
   Problema: Uma loja online recebeu os seguintes pedidos durante o dia

   pedidos = [    
      {"id": 1, "produto": "Notebook", "quantidade": 1, "preco": 2500},
      {"id": 2, "produto": "Mouse", "quantidade": 2, "preco": 50},
      {"id": 3, "produto": "Teclado", "quantidade": 1, "preco": 120},
      {"id": 0, "produto": "Outros", "quantidade": 0, "preco": 0},  # Remover
      {"id": 4, "produto": "Monitor", "quantidade": 1, "preco": 800},
      {"id": 0, "produto": "Outros", "quantidade": 0, "preco": 0},  # Remover
      {"id": 5, "produto": "Webcam", "quantidade": 3, "preco": 150}
   ]

   Tarefa 1: Remover pedidos incorretos
      Alguns pedidos foram enviados com “id”: 0 e “produto”: “Outros”. Você deve remover eles da sua lista de pedidos através dos métodos de lista.

   Tarefa 2: Informações de um produto
      Os funcionários da empresa ficaram sabendo que a sua remoção de produtos incorretos deu certo. Agora eles estão solicitando a implementação da seguinte funcionalidade:

      Dado um index de produto (posição dele dentro da lista, 0 até len - 1), retorne as informações daquela compra: produto - quantidade - preço unitário - preço total.

      Esperado:
         "Pedido index 1: Mouse - 2x - R$50 - Total: R$100"
   
   Dificuldades?
      Tarefa 1: Use pop e index de cada elemento.
      Tarefa 2: Acesse via pedidos[index]
'''

pedidos = [    
   {"id": 1, "produto": "Notebook", "quantidade": 1, "preco": 2500},
   {"id": 2, "produto": "Mouse", "quantidade": 2, "preco": 50},
   {"id": 3, "produto": "Teclado", "quantidade": 1, "preco": 120},
   {"id": 0, "produto": "Outros", "quantidade": 0, "preco": 0},  # Remover
   {"id": 4, "produto": "Monitor", "quantidade": 1, "preco": 800},
   {"id": 0, "produto": "Outros", "quantidade": 0, "preco": 0},  # Remover
   {"id": 5, "produto": "Webcam", "quantidade": 3, "preco": 150}
]


# My resolution
def removeProducts():
   for p in pedidos:
      if p["id"] == 0:
         id = pedidos.index(p)
         pedidos.pop(id)

   print(f'Lista de Pedidos: {pedidos}')
# removeProducts()

def showProduct():
   pdtIndex = int((input('Informe o index do elemento: ')))
   # print(pdtIndex)

   product = pedidos[pdtIndex]
   # print(product)

   pdtName = product["produto"]
   pdtQtd = product["quantidade"]
   pdtPrice = product["preco"]
   pdtTotal = pdtQtd * pdtPrice
   # print(pdtTotal)

   product_formatted = f'Pedido index {pdtIndex}: {pdtName} - {pdtQtd}x - R${pdtPrice} - Total: R${pdtTotal}'
   print(product_formatted)
# showProduct()

print('=' * 50)
print('Informacoes de Pedidos')
print('=' * 50)

pedidos.pop(-4)
pedidos.pop(-2)
print(pedidos)

pedido_index = int(input('Informe o index do pedido que deseja obter informacoes: '))
pedido = pedidos[pedido_index]

print(f'Pedido index {pedido_index}: {pedido['produto']} - {pedido['quantidade']}x - R$ {pedido['preco']} - Total: R$ {pedido['quantidade'] * pedido['preco']}')