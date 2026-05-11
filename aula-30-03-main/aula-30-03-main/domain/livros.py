class Livro:
    def __int__(self, codigo: int, titulo: str, preco: float, tipo: int, desconto_percetual: float= 0 ):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        if desconto_percetual < 0 or desconto_percetual > 100:
            raise ValueError("O desconto deve está entre 0 e 100")
        if tipo not in [1, 2]:
             raise ValueError("Tipo invalido. Use 1 para gratuito e 2 para pago.")

        self.codigo = codigo
        self.titulo = titulo
        self.preco = preco
        self.tipo = tipo
        self.desconto_percetual = desconto_percetual

    def preco_final(self) -> float:
        if self.tipo == 1:
            return 0.0
        desconto = self.preco * (self.desconto_percetual / 100)
        return round(self.preco - desconto, 2)