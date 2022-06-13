# SSC0103 - Programação Orientada a Objetos
# Lista de exercícios #1 (Python)
# Exercício 07
# 
# Ana Lívia Ruegger Saldanha (N.USP 8586691)

'''
Este programa lê vários números de ponto flutuante, um de cada vez, até que
seja digitado o valor zero; identifica e mostra qual é o menor e qual é o
maior valor dentre todos.
'''


def handles_exception():
    ''' Esta função trata exceções na leitura de um valor de ponto flutuante
    do teclado. Caso a leitura não seja válida, pede que o usuário digite
    novamente até obter um valor válido.
    '''
    read_float = False
    n = -1 # Iniciando a variável com um valor qualquer.

    while not read_float:
        try:
            n = float(input())
            read_float = True
        except:
            print("Você deve digitar um valor de ponto flutuante!\nDigite novamente, separando a parte decimal da parte inteira com um ponto.")
    
    return n

n = handles_exception()
max = n
min = n

while n != 0:
    n = handles_exception()
    if n > max:
        max = n
    elif n != 0 and n < min:
        min = n

print("Menor valor:", min)
print("Maior valor:", max)