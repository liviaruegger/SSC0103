"""
File:   pessoa.py
Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
Brief:  SSC0103 - Programação Orientada a Objetos
        Exercícios sobre herança e polimorfismo
        Exercício 02: Agenda de contatos
"""


class Pessoa:

    def __init__(self, CPF: int, nome: str, endereco: str, data_de_nasc: str, 
    email: str, estado_civil: str) -> None:
        self.id = CPF
        self.nome = nome
        self.endereco = endereco
        self.data_de_nasc = data_de_nasc
        self.email = email
        self.estado_civil = estado_civil

    def get_id(self) -> int:
        return self.id

    def get_nome(self) -> str:
        return self.nome

    def imprimir(self) -> None:
        print("CPF: " + str(self.id))
        print("Nome: " + self.nome)
        print("Endereço: " + self.endereco)
        print("Data de nascimento: " + self.data_de_nasc)
        print("Email: " + self.email)
        print("Estado civil: " + self.estado_civil)


class PessoaJuridica(Pessoa):

    def __init__(self, CNPJ: int, nome: str, endereco: str, email: str,
    inscricao: str, razao_social: str) -> None:
        self.id = CNPJ
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.inscricao = inscricao
        self.razao_social = razao_social
        
    def imprimir(self) -> None:
        print("CNPJ: " + str(self.id))
        print("Nome: " + self.nome)
        print("Endereço: " + self.endereco)
        print("Email: " + self.email)
        print("Inscrição estadual: " + self.inscricao)
        print("Razão social: " + self.razao_social)