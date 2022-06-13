"""
File:   grupo.py
Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
Brief:  SSC0103 - Programação Orientada a Objetos
        Exercício: Verificação dos grupos
"""

from src.aluno import Aluno


class Grupo:

    def __init__(self) -> None:
        self.alunos = []

    
    def __str__(self) -> None:
        saida = ""
        for aluno in self.alunos:
            saida += aluno.__str__() + "\n"
        
        return saida

    
    def adicionar_aluno(self, novo_aluno: Aluno) -> None:
        self.alunos.append(novo_aluno)
        self.alunos.sort(key=lambda aluno: aluno.nome)


    def get_numero_de_alunos(self) -> int:
        return len(self.alunos)