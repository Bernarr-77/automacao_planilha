from faker import Faker
import random
from datetime import datetime,timedelta
import sqlite3
from database import start_table

fake = Faker("pt_BR")

def seedbomb(quantidade = 50):
    start_table()
    lote_de_dados = []
    status_opcoes = ["novo","em negociação", "fechado", "perdido"]
    servicos_opçoes = ["limpeza de dente", "clareamento", "botox"]
    for index in range(quantidade):
        cliente = fake.name()
        servico = random.choice(servicos_opçoes)
        hora_a_mais = timedelta(minutes=30 * index)
        data = datetime.now() + hora_a_mais
        hora_iso = data.isoformat()
        valor = random.randint(100,1000)
        status = random.choice(status_opcoes)
        lote_de_dados.append((cliente,servico,hora_iso,valor,status))

    with sqlite3.connect("agendamentos.db") as con:
        cur = con.cursor()
        sql = """
        INSERT OR IGNORE INTO agendamentos(cliente, servico, data_hora, valor,status)
        VALUES (?, ?, ?, ?, ?)
        """

        cur.executemany(sql, lote_de_dados)
        linhas_injetadas = cur.rowcount
        
    print(f"{linhas_injetadas} leads foram injetados com sucesso.")

if __name__  == "__main__":
    seedbomb()