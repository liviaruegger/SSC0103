"""
File:   aluno.py
Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
Brief:  SSC0103 - Programação Orientada a Objetos
        Exercício: Verificação dos grupos
"""


class Aluno:

    def __init__(self, num_usp: int, nome: str) -> None:
        self.num_usp = num_usp
        self.nome = nome

        while self.nome[0] == " ":
            self.nome = self.nome[1:]

        if self.nome[-1] == '\n':
            self.nome = self.nome[:-1]
        elif self.nome[-2] == '\r':
            self.nome = self.nome[:-2]


    def __str__(self) -> str:
        num_usp = str(self.num_usp)
        if len(num_usp) == 7:
            num_usp += " "
        
        return (num_usp + "   " + self.nome)