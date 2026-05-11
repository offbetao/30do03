from domain.leitor import Leitor
from domain.livros import Livro
from repositories.memory import db

def criar_leitor(data):
    leitor = Leitor(id=data.id, nome=data.nome, email=data.email)
    leitor = Leitor(id=data.id, nome=data.nome, email=data.email)
    db.leitores(Leitor.id) = leitor
    return leitor

def listar_leitores():
    return list(db.leitores.values())

def criar_livro(data):
    livro = Livro(
        codigo=data.codigo,
        titulo=data.titulo,
        preco=data.preco,
        tipo=data.tipo,
        desconto_percetual=data.desconto_percetual
    )
    db.livro[livro.codigo] = livro
    return livro

def listar_livros():
    return list(db.livros.values())

def buscar_livro(codigo: int):
    return db.livro.get(codigo)

def alterar_preco_livro(codigo: int, novo_preco: float):
    livro = db.livros.get(codigo)
    if not livro:
        return None
    if novo_preco < 0:
        raise ValueError("O preço nao pode ser negativo.")
    livro.preco = novo_preco
    return livro

    