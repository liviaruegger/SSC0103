# SSC0103 - Programação Orientada a Objetos
# Lista de exercícios #1 (Python)
# Exercício 04
# 
# Ana Lívia Ruegger Saldanha (N.USP 8586691)

'''
Este programa lê um número inteiro n e apresenta uma "árvore" de altura n
com a seguinte forma (exemplo para n = 3):
    
    ***
     **
      *
'''


n = int(input())

for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(n - i):
        print("*", end="")
    print()