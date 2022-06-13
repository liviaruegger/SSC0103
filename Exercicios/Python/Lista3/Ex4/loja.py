"""
File:   loja.py
Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
Brief:  SSC0103 - Programação Orientada a Objetos
        Exercícios sobre herança e polimorfismo
        Exercício 04: Loja
"""


from produtos import Produto, Livro, CD, DVD


"""
Crie uma hierarquia de classes para representar os produtos de uma loja:
livros, CDs e DVDs. Um produto é identificado unicamente pelo seu código
de barras. Implemente, também, uma classe Loja que permite que sejam
armazenados os produtos e que permita que possam ser adicionados produtos
(numa certa quantidade), possam ser buscados produtos por código de barras
ou por nome e possam ser vendidos produtos, dado seu código de barras. É
desejável, também, uma funcionalidade que permita verificar todo o estoque
da loja, mostrando o número de itens por produto e por categoria.
"""


class Loja:

    def __init__(self) -> None:
        self.produtos = []


    def adicionar_produto(self, produto: Produto) -> None:
        self.produtos.append(produto)


    def buscar(self, chave) -> None:
        for produto in self.produtos:
            if type(chave) == int:
                if produto.get_codigo() == chave:
                    produto.imprimir_info()
            elif type(chave) == str:
                if produto.get_nome() == chave:
                    produto.imprimir_info()


    def vender(self, chave) -> None:
        vendido = False
        for produto in self.produtos:
            if type(chave) == int:
                if produto.get_codigo() == chave:
                    if produto.estoque > 0:
                        produto.estoque = produto.estoque - 1
                        vendido = True
            elif type(chave) == str:
                if produto.get_nome() == chave:
                    if produto.estoque > 0:
                        produto.estoque = produto.estoque - 1
                        vendido = True
        if vendido == True:
            print("Compra realizada com sucesso")
        else:
            print("Produto não encontrado ou esgotado.")


    def verificar_estoque(self) -> None:
        for produto in self.produtos:
            if type(produto) == Livro:
                print("Categoria: livro")
            elif type(produto) == CD:
                print("Categoria: CD")
            elif type(produto) == DVD:
                print("Categoria: DVD")
            produto.imprimir_info()
            print()



##### TESTES #####

loja = Loja()
loja.adicionar_produto(Livro(12345, "Orlando", 50, 5, "Virginia Woolf", "Ficção", 350))
loja.adicionar_produto(CD(12346, "SAWAYAMA", 40, 10, "Rina Sawayama", 13))
loja.adicionar_produto(DVD(12347, "Carol", 60, 2, "Todd Haynes", "Drama", 118))

#loja.buscar("SAWAYAMA")
#loja.buscar(12345)
#loja.vender("SAWAYAMA")

loja.verificar_estoque()