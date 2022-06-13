"""
File:   turma.py
Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
Brief:  SSC0103 - Programação Orientada a Objetos
        Exercício: Verificação dos grupos
"""

from src.aluno import Aluno
from src.grupo import Grupo


class Turma(Grupo):

    def __init__(self) -> None:
        super().__init__()
        self.grupos = []


    def aluno_esta_na_turma(self, aluno_buscado: Aluno) -> bool:
        for aluno in self.alunos:
            if aluno.num_usp == aluno_buscado.num_usp:
                return True

        return False


    def aluno_tem_grupo(self, aluno_buscado: Aluno) -> bool:
        for grupo in self.grupos:
            for aluno in grupo.alunos:
                if aluno.num_usp == aluno_buscado.num_usp:
                    return True

        return False


    def adicionar_grupo(self, novo_grupo: Grupo) -> bool:
        for aluno in novo_grupo.alunos:
            if not self.aluno_esta_na_turma(aluno):
                return False # Se algum dos alunos não está na turma, indica erro

        self.grupos.append(novo_grupo)
        return True # Grupo adicionado com sucesso


    def listar_grupos(self) -> None:
        for grupo in self.grupos:
            if grupo.get_numero_de_alunos() != 4:
                print("===== Grupo com número inválido de participantes =====")
            print(grupo)


    def get_alunos_sem_grupo(self) -> list[Aluno]:
        alunos_sem_grupo = []
        for aluno in self.alunos:
            if not self.aluno_tem_grupo(aluno):
                alunos_sem_grupo.append(aluno)

        return alunos_sem_grupo