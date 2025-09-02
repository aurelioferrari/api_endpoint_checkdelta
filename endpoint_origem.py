from pydantic import BaseModel

class Geral(BaseModel):
    id: int
    nome: str


dados_origem = [
    Geral(id=1, nome="Opção 1"),
    Geral(id=2, nome="Opção 2"),
    Geral(id=3, nome="Opção 3")
]