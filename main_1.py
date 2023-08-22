import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

# Criação da tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoIngresso INTEGER
);
""")

# Lista de tuplas para registrar os estudantes
estudantes = [
    ("Ana Silva", "Computação", 2019),
    ("Pedro Mendes", "Física", 2021),
    ("Carla Souza", "Computação", 2020),
    ("João Alves", "Matemática", 2018),
    ("Maria Oliveira", "Química", 2022)
]

# Insere vários registros de uma vez.
# Ele toma uma consulta SQL e uma lista de tuplas como parâmetros.
###
# cursor.executemany("""
# INSERT INTO Estudantes (Nome, Curso, AnoIngresso)
# VALUES (?, ?, ?);
# """, estudantes)

# Filtragem dos estudantes que ingressaram entre 2019 e 2020 (inclusive)
cursor.execute("SELECT * FROM Estudantes WHERE (AnoIngresso = 2019 or AnoIngresso = 2020)")
print(cursor.fetchall())
conn.commit()

# Atualização do Ano de Ingresso do aluno Pedro Mendes
cursor.execute("UPDATE Estudantes SET AnoIngresso = 2023 WHERE Nome = 'Pedro Mendes'")
conn.commit()

# Apaga o estudante de ID = 1 da tabela Estudantes
cursor.execute("DELETE FROM Estudantes WHERE ID = 1")
conn.commit()

# Filtragem dos estudantes que ingressaram depois de 2019 cujo curso é Computação
cursor.execute("SELECT * FROM Estudantes WHERE AnoIngresso > 2019 AND Curso = 'Computação'")
print(cursor.fetchall())
conn.commit()

# Atualização do Ano de Ingresso para 2018 de todos os alunos que cursam Computação
cursor.execute("UPDATE Estudantes SET AnoIngresso = 2018 WHERE Curso = 'Computação'")
conn.commit()