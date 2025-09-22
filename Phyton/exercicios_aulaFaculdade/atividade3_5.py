import sqlite3

conn = sqlite3.connect("funcionarios.db")

cursor = conn.cursor()

# Passo 6: Deletar um funcionário da tabela

id_funcionario_para_deletar = 1

cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id_funcionario_para_deletar,))

conn.commit()