from fastapi import APIRouter
from schemas.leitor import  LeitoCreate, LeitorOut
from services.biblioteca_services import criar_leitor, listar_leitores

router = APIRouter(prefix="/Leitores", tags=["Leitores"])

@router.post("", response_model=LeitorOut)
def post_leitor(data: LeitoCreate):
    return criar_leitor(data)

@router.get("", response_model=[LeitorOut])
def get_leitores():
    return listar_leitores()