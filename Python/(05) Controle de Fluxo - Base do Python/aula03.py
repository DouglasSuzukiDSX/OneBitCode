# Aula 03 - Condições com match
status_compra = 'aguardando pagamento'
compra_gratis = True

match status_compra:
   case 'aguardando pagamento' if compra_gratis == False:
      print('Faca o pagamento')
   case 'aguardando pagamento' if compra_gratis:
         print('Sua compra nao precisa de pagamento, em breve o status sera atualizado')
   case 'pago':
      print('Em breve sera enviado para a coleta')
   case 'coletado':
      print('O vendedor ja postou seu pedido')
   case 'a caminho':
      print('O pedido ja esta a caminho, chegara nos proximos dias')
   case 'rota de entrega':
      print('Pedido em rota de entrega para o seu endereco')
   case 'erro' | 'cancelado':
      print('A sua entrega foi cancelada')
   case _:
      print('Status a definir')

usuario = { 'nome': 'James', 'cargo': 'admin' }

match usuario:
   case { 'cargo': 'admin' }:
      print('Voce e admin')
   case _:
      print('Voce nao e admin')