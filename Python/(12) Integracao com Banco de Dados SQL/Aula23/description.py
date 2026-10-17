'''
   O objetivo deste exercício é consolidar na prática os conceitos de mapeamento moderno, relacionamentos e ciclo de vida de sessões. Você deve construir um pequeno sistema de console para gerenciar Clientes e seus Pedidos.

   Modelagem Relacional (1:N):
      - Crie a tabela clientes com os campos: id (chave primária), nome (obrigatório, máximo 50 caracteres) e email (único, opcional).

      - Crie a tabela pedidos com os campos: id (chave primária), item (nome do produto, obrigatório), valor (numérico, obrigatório) e cliente_id (chave estrangeira apontando para clientes).

      - Configure o relacionamento bidirecional usando back_populates em ambas as classes.

      - Configure a exclusão em cascata (cascade="all, delete-orphan") no lado do cliente para remover automaticamente pedidos que ficarem sem dono.

   Script de Operações (CRUD):
      - Inserção: Cadastre a cliente "Mariana Souza" vinculando a ela dois pedidos: um "Notebook" de 4500.00 e um "Mouse" de 150.00. Salve tudo utilizando o commit de uma única sessão.

      - Consulta: Busque a cliente Mariana no banco utilizando o padrão select(), percorra seus pedidos associados e exiba no console o nome do cliente e os detalhes de cada item.
      
      - Exclusão de Órfão: Remova o item "Mouse" da lista de pedidos da cliente diretamente no objeto em memória e faça o commit para testar se o SQLAlchemy deleta o registro físico do banco automaticamente.
'''