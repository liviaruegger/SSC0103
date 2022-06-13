"""
File:   main.py
Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
Brief:  SSC0103 - Programação Orientada a Objetos
        Exercício: Verificação dos grupos
"""

from glob import glob

from src.aluno import Aluno
from src.grupo import Grupo
from src.turma import Turma


def processar_turmas() -> tuple[list[Turma], list[str]]:
    lista_arquivos_turmas = glob("data/turmas/*.csv")

    turmas = []
    arquivos_com_erros = []

    for file_name in lista_arquivos_turmas:
        nova_turma = Turma()

        try:
            f = open(file_name)
            lines = f.readlines()
        except:
            arquivos_com_erros.append(file_name)
        
        for line in lines:
            line = line.split(",")

            try:
                num_usp = int(line[0])
                aluno = Aluno(num_usp, line[1])
                nova_turma.adicionar_aluno(aluno)
            except:
                if file_name not in arquivos_com_erros:
                    arquivos_com_erros.append(file_name)

        f.close()

        if file_name not in arquivos_com_erros:
            turmas.append(nova_turma)

    return turmas, arquivos_com_erros


def processar_grupos() -> tuple[list[Grupo], list[str]]:
    lista_arquivos_grupos = glob("data/grupos/*.csv")

    grupos = []
    arquivos_com_erros = []

    for file_name in lista_arquivos_grupos:
        novo_grupo = Grupo()

        try:
            f = open(file_name)
            lines = f.readlines()
        except:
            arquivos_com_erros.append(file_name)
        
        for line in lines:
            line = line.split(",")

            try:
                num_usp = int(line[0])
                aluno = Aluno(num_usp, line[1])
                novo_grupo.adicionar_aluno(aluno)
            except:
                if file_name not in arquivos_com_erros:
                    arquivos_com_erros.append(file_name)

        f.close()

        if file_name not in arquivos_com_erros:
            grupos.append(novo_grupo)

    return grupos, arquivos_com_erros



##### PROCESSAMENTO ######################################################################

turmas, arquivos_com_erros_turmas = processar_turmas()
grupos, arquivos_com_erros_grupos = processar_grupos()

# Distribuir grupos em suas respectivas turmas
grupos_nao_distribuidos = grupos[:]
for grupo in grupos:
    for turma in turmas:
        if turma.adicionar_grupo(grupo): # Se adicionou com sucesso
            grupos_nao_distribuidos.remove(grupo)

# Buscar alunos que não tem grupo
alunos_sem_grupo = []
for turma in turmas:
    alunos_sem_grupo += turma.get_alunos_sem_grupo()
alunos_sem_grupo.sort(key=lambda aluno: aluno.nome)



##### RESULTADOS #########################################################################

print("-------------------------------------------------------------")
print("Arquivos com erros:\n")
for arquivo in arquivos_com_erros_turmas + arquivos_com_erros_grupos:
    print(arquivo)

for i in range(len(turmas)):
    print("\n-------------------------------------------------------------")
    print("Grupos da turma " + str(i + 1) + ":\n")
    turmas[i].listar_grupos()

print("\n-------------------------------------------------------------")
print("Grupos com alunos das duas turmas ou que não existem:\n")
for grupo in grupos_nao_distribuidos:
    print(grupo)
    
print("\n-------------------------------------------------------------")
print("Alunos que não aparecem em nenhum grupo: " + str(len(alunos_sem_grupo)) + "\n")
for aluno in alunos_sem_grupo:
    print(aluno)