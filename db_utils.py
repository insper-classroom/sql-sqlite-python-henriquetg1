import sqlite3

# Funções

def cria_tabela_estudantes(conn, cursor):
    query = """
        CREATE TABLE IF NOT EXISTS Estudantes (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Curso TEXT NOT NULL,
            AnoIngresso INTEGER NOT NULL
        );
    """

    cursor.execute(query)

def insere_novo_registro(conn, cursor, estudantes, nome, curso, ano_de_ingresso):
    query = ("""
        INSERT INTO Estudantes (Nome, Curso, AnoIngresso)
        VALUES (?, ?, ?);
    """, estudantes)

    cursor.execute(query, (nome, curso, ano_de_ingresso))

def filtra_por_ano_de_ingresso(conn, cursor, ano1, ano2):
    query = "SELECT * FROM Estudantes WHERE (AnoIngresso >= ? and AnoIngresso <= ?)"

    cursor.execute(query, (ano1, ano2))
    print(cursor.fetchall())

def atualiza_ano_de_ingresso(conn, cursor, novo_ano_de_ingresso, nome):
    query = "UPDATE Estudantes SET AnoIngresso = ? WHERE Nome = ?"

    cursor.execute(query, (novo_ano_de_ingresso, nome))
    if cursor.rowcount > 0:
        conn.commit()
        print(f"Ano de ingresso atualizado!")
    else:
        print("Dado não alterado.")

def apaga_estudante(conn, cursor, id):
    query = "DELETE FROM Estudantes WHERE ID = ?"

    cursor.execute(query, (id,))
    conn.commit()

def filtra_por_ano_de_ingresso_e_curso(conn, cursor, ano_de_ingresso, curso):
    query = "SELECT * FROM Estudantes WHERE AnoIngresso > ? AND Curso = ?"

    cursor.execute(query, (ano_de_ingresso, curso))
    print(cursor.fetchall())

def atualiza_ano_de_ingresso_de_um_curso(conn, cursor, novo_ano_de_ingresso, curso):
    query = "UPDATE Estudantes SET AnoIngresso = ? WHERE Curso = ?"

    cursor.execute(query, (novo_ano_de_ingresso, curso))
    conn.commit()

