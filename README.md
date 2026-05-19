# Projeto 1 — Gerador de Relatório Excel via API

## 🎯 Objetivo
Construir uma API FastAPI que recebe um período (data início e data fim) via query params, consulta um banco SQLite com dados de agendamentos, e devolve um arquivo `.xlsx` formatado profissionalmente para download direto.

## 🛠️ Stack
- **FastAPI** — Criação e roteamento da API.
- **openpyxl** — Geração e formatação do Excel (com cores, larguras de coluna e cálculos automáticos).
- **SQLite** — Banco local para o projeto de estudo.
- **Uvicorn** — Servidor ASGI.

### Instalação de dependências:
```bash
pip install fastapi uvicorn openpyxl
```

## 🗂️ Estrutura de Pastas
```javascript
projeto_excel/
├── main.py        ← rotas FastAPI
├── database.py    ← conexão e queries SQLite
├── relatorio.py   ← lógica openpyxl
└── seed.py        ← popula banco com dados fictícios
```

## 🗺️ Roadmap de Desenvolvimento

### Fase 1 — Banco e Seed
- [x] Criar `database.py` com `start_bank()` que cria tabela `agendamentos` (Colunas: `id`, `cliente`, `servico`, `data_hora`, `valor`, `status`).
- [x] Criar `seed.py` para popular o banco de dados.
- [x] Criar função `get_agendamentos(data_inicio, data_fim)` que filtra por período.

### Fase 2 — Excel com openpyxl
- [x] Criar `relatorio.py` com `gerar_relatorio(dados)`.
- [x] Escrever cabeçalho: Cliente, Serviço, Data/Hora, Valor, Status.
- [x] Aplicar cor no cabeçalho com `PatternFill` (verde escuro, texto branco).
- [x] Escrever dados linha por linha a partir da linha 2.
- [x] Formatar coluna Valor como moeda brasileira.
- [x] Ajustar largura das colunas manualmente.
- [x] Adicionar linha de totais no final (soma do valor).
- [x] Salvar em `BytesIO` (em memória, sem tocar no disco).

### Fase 3 — Rota com Download
- [x] Criar endpoint `GET` que recebe parâmetros opcionais de data.
- [x] Chamar a função do banco de dados e validar o retorno (lança `HTTPException 404` se vazio).
- [x] Retornar `StreamingResponse` contendo o Excel gerado.

## ⚠️ Aprendizados e Armadilhas Evitadas
- **Não salvar em disco:** Utilizar `BytesIO` sempre em APIs.
- **`seek(0)`:** Lembrar de usar `.seek(0)` no `BytesIO` antes do `StreamingResponse` para evitar que o arquivo saia vazio.
- **Largura das Colunas:** A largura da coluna não é automática no `openpyxl`, calculada/setada manualmente via `column_dimensions`.
- **Datas:** As datas do SQLite vêm como string, sendo necessário convertê-las para `datetime` antes de formatá-las no Excel.

## ✅ Como Executar

1. Crie e ative seu ambiente virtual.
2. Instale as dependências: `pip install fastapi uvicorn openpyxl`
3. Execute as migrations/seed se for a primeira vez: `python database.py` e `python seed.py`
4. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```
5. Acesse a documentação em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) e teste a geração da planilha.
