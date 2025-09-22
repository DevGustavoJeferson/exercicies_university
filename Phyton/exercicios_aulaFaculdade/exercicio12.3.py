import sqlite3 #ATUALIZAR PRODUTOS ATRAVES DO ID

# Conectando ao banco de dados
conn = sqlite3.connect('exercicio12.db')
cursor = conn.cursor()
# Novo preço e ID do produto a ser atualizado
novo_preco = 50.00
produto_id = 3  # Suponha que queiramos atualizar o produto com ID 1
# Comando SQL para atualizar o preço do produto
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
# Executando o comando SQL de atualização
cursor.execute(atualizar_preco, (novo_preco, produto_id))
# Confirmando as alterações
conn.commit()
# Fechando a conexão
conn.close()