import sqlite3

conn = sqlite3.connect("funcionarios.db")

cursor = conn.cursor()

# Passo 5: Atualizar informações de um funcionário

atualizacao = ("João Silva", 5500.00, 1)

cursor.execute("UPDATE funcionarios SET nome = ?, salario = ? WHERE id = ?", atualizacao)

conn.commit()