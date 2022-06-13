# SSC0103 - Programação Orientada a Objetos
# Lista de exercícios #1 (Python)
# Exercício 06
# 
# Ana Lívia Ruegger Saldanha (N.USP 8586691)

'''
Este programa lê um número inteiro e exibe o primeiro número primo menor
que o número informado.
'''


def nearest_prime(n):
    for i in range(n - 1, 1, -1):
        i_is_prime = True
        for j in range(2, int(i/2 + 1)):
            if i % j == 0:
                i_is_prime = False
                break
        
        if i_is_prime == True:
            print(i)
            return

    print("Não existe número primo menor que", n)

n = int(input())
nearest_prime(n)