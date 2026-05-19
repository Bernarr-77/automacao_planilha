from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from database import get_all, get_agendamentos
from typing import Optional
from relatorio import gerar_relatorio

app = FastAPI()

@app.get("/excel/buscar_todos")
def get_planilha(hora_inicial: Optional[str] = None, hora_final: Optional[str] = None):
    """Busca por hora ou por todos os dados"""
    try:
        if hora_inicial is None and hora_final is None:
            resultado = get_all()
        
        elif hora_inicial is None or hora_final is None:
            raise HTTPException(status_code=400, detail="hora_inicio e hora_fim devem ser passados juntos ou nenhum deles.")
        
        else:
            resultado = get_agendamentos(hora_inicio=hora_inicial, hora_fim=hora_final)
            
        if not resultado:
            raise HTTPException(status_code=404, detail="Nenhum dado encontrado para os critérios informados.")
            
        excel = gerar_relatorio(resultado)
        return StreamingResponse(
            excel, 
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": "attachment; filename=agendamentos.xlsx"}
        )

    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Erro interno no servidor: {str(exc)}")

