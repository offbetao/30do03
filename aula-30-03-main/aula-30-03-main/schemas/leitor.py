from pydantic import Basemodel, EmailStr

class LeitoCreate(BaseModel):
    id: int
    nome: str
    email: EmailStr

class LeitorOut(Basemodel):
    id: int
    nome: str
    email: EmailStr

