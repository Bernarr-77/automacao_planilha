from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font
from typing import List
from datetime import datetime 
from database import get_all

def gerar_relatorio(dados: List ):
    wb = Workbook()

    planilha = wb.active

    planilha.append(['Cliente', 'Serviço', 'Data/Hora', 'Valor', 'Status'])

    for celula in planilha[1]:
        fundo_verde = PatternFill(start_color="006400", end_color="006400", fill_type="solid")
        texto_branco = Font(color="FFFFFF", bold=True)
    celula.fill = fundo_verde
    celula.font = texto_branco

    for _, cliente, servico, data_texto, valor, status in dados:
        data_convertida = datetime.fromisoformat(data_texto)
        planilha.append([cliente, servico, data_convertida, valor, status])
    wb.save("test.xlsx")

if __name__ == "__main__":
    todos_dados = get_all()
    gerar_relatorio(todos_dados)