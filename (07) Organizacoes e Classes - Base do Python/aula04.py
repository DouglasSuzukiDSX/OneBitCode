# Aula04 - Módulos built-in (parte 3)
import re
   # Regex 
      # \d => Apenas numeros
      # \D => Tudo que nao seja numeros
      # [a-z] => Apenas letras minusculas 
      # [a-z]{4} => Apenas 4 letras minusculas
   
texto = 'Codigo 123 da OneBitCode 456'
padrao = r'\d+' # Pega os numeros que estao com ele

resultado_match = re.match(padrao, texto) # Verifica se comeca com o padrao
# print(resultado_match.group()) # Aqui gera um erro porque ele procura o padra estabelecido no comeco da string. 

resultado_fullmatch = re.fullmatch(padrao, texto) # Verifica se toda a string comeca com o padrao
# print(resultado_fullmatch.group()) # Aqui gera um erro porque ele procura o padrao estabelecido em toda string.

# =======================================

resultado_search = re.search(padrao, texto)
print(resultado_search.group())

# =======================================

texto_pedido = 'Peido 1052 enviado, pedido 9823 em processamento, pedido 112 cancelado'
resultado_findall = re.findall(padrao, texto_pedido)
print(resultado_findall)

# =======================================

documento = 'O CPF do aluno e 123.456.789-00'
documento_mascarado = re.sub(r'\d', 'X', documento)
print(documento_mascarado)

# =======================================

padrao_data = re.compile(r'\d{2}/\d{2}/\d{4}')
anuncio_1 = 'Evento sero no dia 15/10/2026 no Rio'
anuncio_2 = 'Mentoria confirmada para 22/11/2026 online'

print(padrao_data.search(anuncio_1).group())
print(padrao_data.search(anuncio_2).group())