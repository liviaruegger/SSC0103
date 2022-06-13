# SSC0103 - Programação Orientada a Objetos
# Lista de exercícios #1 (Python)
# Exercício 05
# 
# Ana Lívia Ruegger Saldanha (N.USP 8586691)

'''
Este programa lê um número inteiro, verifica se ele é primo e, caso ele
não seja, exibe qual o seu menor divisor.
'''


def is_prime(n):
    for i in range(2, int(n/2 + 1)):
        if n % i == 0:
            print("O número", n, "é divisível por", i)
            return
    print("O número", n, "é primo")

n = int(input())
is_prime(n)