import sqlite3

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
