"""
File:   produtos.py
Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
Brief:  SSC0103 - Programação Orientada a Objetos
        Exercícios sobre herança e polimorfismo
        Exercício 04: Loja
"""


"""
Crie uma hierarquia de classes para representar os produtos de uma loja:
livros, CDs e DVDs. Um produto é identificado unicamente pelo seu código
de barras.
"""


class Produto:

    def __init__(self, codigo_de_barras: int, nome: str, preco: int, 
    estoque: int) -> None:
        self.codigo_de_barras = codigo_de_barras
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def get_codigo(self) -> int:
        return self.codigo_de_barras

    def get_nome(self) -> str:
        return self.nome

    def info(self) -> None:
        return ("Nome do produto: " + self.nome +
        "\nPreço: R$" + str(self.preco) +
        "\nQuantidade em estoque: " + str(self.estoque) +
        "\nCódigo de barras: " + str(self.codigo_de_barras))


class Livro(Produto):

    def __init__(self, codigo_de_barras: int, nome: str, preco: int,
    estoque: int, autor: str, genero: str, paginas: int) -> None:
        super().__init__(codigo_de_barras, nome, preco, estoque)
        self.genero = genero
        self.paginas = paginas
        self.autor = autor

    def imprimir_info(self) -> None:
        print(self.info())
        print("Autor: " + self.autor)
        print("Gênero: " + self.genero)
        print("Número de páginas: " + str(self.paginas))


class CD(Produto):

    def __init__(self, codigo_de_barras: int, nome: str, preco: int, 
    estoque: int, artista: str, faixas: int) -> None:
        super().__init__(codigo_de_barras, nome, preco, estoque)
        self.artista = artista
        self.faixas = faixas

    def imprimir_info(self) -> None:
        print(self.info())
        print("Artista: " + self.artista)
        print("Número de faixas: " + str(self.faixas))


class DVD(Produto):

    def __init__(self, codigo_de_barras: int, nome: str, preco: int,
    estoque: int, direcao: str, genero: str, duracao: int) -> None:
        super().__init__(codigo_de_barras, nome, preco, estoque)
        self.direcao = direcao
        self.genero = genero
        self.duracao = duracao

    def imprimir_info(self) -> None:
        print(self.info())
        print("Direção: " + self.direcao)
        print("Gênero: " + self.genero)
        print("Duração: " + str(self.duracao) + " minutos")