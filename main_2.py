from db_utils import *
import sqlite3

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

# Filtragem dos estudantes que ingressaram entre 2019 e 2020 (inclusive)
filtra_por_ano_de_ingresso(conn, cursor, 2019, 2020)
conn.commit()

# # Atualização do Ano de Ingresso do aluno Pedro Mendes
atualiza_ano_de_ingresso(conn, cursor, 2019, 'Pedro Mendes')
conn.commit()

# # Apaga o estudante de ID = 1 da tabela Estudantes
apaga_estudante(conn, cursor, 1)
conn.commit()

# # Filtragem dos estudantes que ingressaram depois de 2019 cujo curso é Computação
filtra_por_ano_de_ingresso_e_curso(conn, cursor, 2020, 'Computação')
conn.commit()

# # Atualização do Ano de Ingresso para 2018 de todos os alunos que cursam Computação
atualiza_ano_de_ingresso_de_um_curso(conn, cursor, 2018, 'Computação')
conn.commit()