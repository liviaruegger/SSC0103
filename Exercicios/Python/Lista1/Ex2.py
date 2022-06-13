# SSC0103 - Programação Orientada a Objetos
# Lista de exercícios #1 (Python)
# Exercício 02
# 
# Ana Lívia Ruegger Saldanha (N.USP 8586691)

'''
Este programa lê do teclado os coeficientes de uma equação de segundo grau
e apresenta sua solução.
'''


import math

def handles_exception():
    ''' Esta função trata exceções na leitura de um valor inteiro do teclado.
    Caso a leitura não seja válida, pede que o usuário digite novamente até
    obter um valor válido.
    '''
    read_int = False
    n = -1 # Iniciando a variável com um valor qualquer.

    while not read_int:
        try:
            n = int(input())
            read_int = True
        except:
            print("Você deve digitar um valor inteiro!\nDigite novamente.")
    
    return n

print("Digite os coeficientes da equação de segundo grau:")
a = handles_exception()
b = handles_exception()
c = handles_exception()

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Esta equação não possui raízes reais.")
else:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    if delta == 0:
        print("A raiz dupla desta equação é", x1)
    else:
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("As raízes da equação são", x1, "e", x2)