from pydantic import BaseModel

class LivroCreate(BaseModel):
    codigo: int
    titulo: str
    preco: float
    tipo: int
    desconto_percetual: float = 0

class LivroOut(BaseModel):
    codigo: int
    titulo: str
    preco: float
    tipo: int
    desconto_percetual: float = 0
    

