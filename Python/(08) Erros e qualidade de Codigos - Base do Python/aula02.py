# Aula02 - Levantando exceções com raise

def definir_idade(idade):
   if idade < 0:
      raise ValueError('Idade nao poder negativa')
   if idade > 140:
      raise ValueError('Idade deve ser realista')
   
   return idade 

try:
   print(definir_idade(-5))
except ValueError as error:
   print(f'Erro: {error}')

class ContaBancaria:
   def __init__(self, titular, saldo):
      if not titular:
         raise ValueError('Titular nao pode ser vazio')

      if saldo < 0:
         raise ValueError('Salfo nao pode ser negativo')

      self.titular = titular
      self.saldo = saldo

   def sacar(self, valor):
      if valor > self.saldo:
         raise ValueError('Saldo insuficiente')

      self.saldo -= valor

   def sacadepositar(self, valor):
         if valor <= 0:
            raise ValueError('SValor deve ser positivo')
   
         self.saldo += valor

try:
   conta = ContaBancaria('', 1000)
except ValueError as error:
   print(f'Erro: {error}')

try:
   conta = ContaBancaria('Joao', 1000)
   conta.sacar(2000)
except ValueError as error:
   print(f'Erro: {error}')

class SaldoInsuficiente(Exception):
   def __init__(self, saldo_atua, valor_solicitado):
      self.saldo_atual = saldo_atua
      self.valor_solicitado = valor_solicitado

      mensagem = f'Saldo disponivel? R$ {self.saldo_atual:.2f} solicitado: R$ {self.valor_solicitado:.2f}'

      super().__init__(mensagem)

class ContaBancaria2:
   def __init__(self, saldo):
      self.saldo = saldo

   def sacar(self, valor):
      if valor > self.saldo:
         raise SaldoInsuficiente(self.saldo, valor)

      self.saldo -= valor

      print(f'Saque de R$ {valor:.2f} realizado com sucesso!')

try:
   conta = ContaBancaria2(100)
   conta.sacar(500)
except SaldoInsuficiente as error:
   print(f'Operacao negada: {error}')
   print(f'Faltaram R$ {error.valor_solicitado - error.saldo_atual:.2f} para concluir a operacao.')

class EmailInvalidoError(Exception):
   # Levantada quando um formato de email nao cumpre as regras de validacao
   def __init__(self, email, motivo, codigo_erro):
      self.email = email
      self.motifvo = motivo
      self.codigo_erro = codigo_erro # Um identificador unico para o tipo de erro

      super().__init__(f'O email "{email}" e invalido. Motivo: {motivo} (Codigo: {codigo_erro})')

def validar_email(email):
   if not email or not email.strip():
      raise EmailInvalidoError(email, 'O endereco de email nao pode estar vazio', 'EMAIL_VAZIO')

   if '@' not in email:
      raise EmailInvalidoError(email, 'O caractere "@" esta ausente.', 'SEM_ARROBA')

   partes = email.split('@')
   if len(partes) < 2 or '.' not in partes[1]:
      raise EmailInvalidoError(email, 'O dominio apos o "@" e invalido ou nao contem um ponto.', "DOMINIO_INVALIDO")

   return email

emails = ['valido@ex.com', 'invalido', 'sem.dominio@', '']

for email in emails:
   try:
      validar_email(email)
      print(f'✅ {email} => Valido')
   except EmailInvalidoError as e:
      print(f'❌ {email} => Erro capturado: {e}')

      if e.codigo_erro == 'EMAIL_VAZIO':
         print('Informe um email')