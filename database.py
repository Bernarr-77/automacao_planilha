import sqlite3
from typing import List

def start_table():
    con = sqlite3.connect("agendamentos.db")
    cur = con.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS agendamentos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT NOT NULL,
    servico TEXT NOT NULL,
    data_hora TEXT NOT NULL,
    valor FLOAT NOT NULL,
    status TEXT NOT NULL)
    """
    cur.execute(sql)
    con.commit()
    con.close()

def get_agendamentos(hora_inicio: str, hora_fim: str) -> List:
    with sqlite3.connect("agendamentos.db") as con:
        cur = con.cursor()
        sql = """
        SELECT * FROM agendamentos WHERE data_hora >= ? AND data_hora <= ?
        """
        cur.execute(sql, (hora_inicio, hora_fim))
        return cur.fetchall()
