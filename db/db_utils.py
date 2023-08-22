import sqlite3

# Funções

def filtra_por_ano_de_ingresso(conn, cursor, ano1, ano2):
    query = "SELECT * FROM Estudantes WHERE (AnoIngresso >= ? and AnoIngresso <= ?))"

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

