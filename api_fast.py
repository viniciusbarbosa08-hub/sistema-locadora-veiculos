from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="API de Gestão da Locadora de Veículos",
    version="0.1.0"
)

# Modelo de dados esperado pela API
class Locacao(BaseModel):
    veiculos_id: int
    clientes_id: int
    data_inicio: str
    data_fim: str
    valor_total: float

@app.get("/locacoes")
def listar_locacoes():
    return {"mensagem": "Lista de locações", "dados": []}

@app.post("/locacoes")
def criar_locacao(locacao: Locacao):
    return {"mensagem": "Locação criada com sucesso!", "dados": locacao}

@app.get("/locacoes/{id}")
def obter_locacao(id: int):
    return {"mensagem": f"Buscando locação de ID {id}"}

@app.put("/locacoes/{id}")
def atualizar_locacao(id: int, locacao: Locacao):
    return {"mensagem": f"Locação {id} atualizada"}

@app.delete("/locacoes/{id}")
def excluir_locacao(id: int):
    return {"mensagem": f"Locação {id} excluída"}