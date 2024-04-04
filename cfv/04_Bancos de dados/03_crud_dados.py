import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')

cursor = conexao.cursor()

try:
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")

    # Insere um registro de exemplo na tabela clientes
    cursor.execute("INSERT INTO clientes (nome, email) VALUES ('João', 'joao@example.com')")
    cursor.execute("INSERT INTO clientes (nome, email) VALUES ('Maria', 'maria@example.com')")
    cursor.execute("INSERT INTO clientes (nome, email) VALUES ('Pedro', 'pedro@example.com')")
    dados = ('Pedro', 'pedro@email.com')
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)

    # Inserindo vários registros
    varios_dados = [('Pedro', 'pedro@email.com'),('Filipe', 'filipe@email.com'),('Arthur', 'arthur@email.com')]
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", varios_dados)


    # Atualiza o email do cliente com o nome 'João'
    cursor.execute("UPDATE clientes SET email = 'joao.novo@example.com' WHERE nome = 'João'")

    # Consulta todos os registros da tabela clientes
    cursor.execute("SELECT * FROM clientes")
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)

    # Consultando no formato de dicionário
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes WHERE id = 1")
    result = cursor.fetchone()
    print(dict(result))

    # Remove o cliente com o nome 'João'
    cursor.execute("DELETE FROM clientes WHERE nome = 'Pedro'")

    # Commit para aplicar as mudanças
    conexao.commit()

except Exception as e:
    print(f'Ocorreu o erro: {e}')
    conexao.rollback()

# Fecha a conexão
conexao.close()
