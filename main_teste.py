from fastapi import FastAPI
from endpoint_origem import dados_origem, Geral
import uvicorn


app = FastAPI()

@app.get('/opcoes')
async def pega_opcao():
    return dados_origem

@app.post('/opcoes')
async def add_opcao(nova_opcao: Geral):
    dados_origem.append(nova_opcao)
    return nova_opcao

if __name__ == "__main__":
    uvicorn.run("main_teste:app", host="0.0.0.0", port=8000)