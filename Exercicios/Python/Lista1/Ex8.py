# SSC0103 - Programação Orientada a Objetos
# Lista de exercícios #1 (Python)
# Exercício 08
# 
# Ana Lívia Ruegger Saldanha (N.USP 8586691)

'''
Este programa calcula raízes da equação x^3 - x^2 - 13x + 8 através do método
da bisseção, com erro inferior a 10^(-7).
'''


def f(x):
    return pow(x,3) - pow(x,2) - (13 * x) + 8

error_coef = 0.0000001
print("Forneça os extremos do intervalo [a,b]:")

a = float(input())
b = float(input())

while f(a) * f(b) >= 0:
    print("Os valores de a e b devem ser tais que f(a) * f(b) < 0")
    print("Forneça novos valores para os extremos do intervalo [a,b]:")
    a = float(input())
    b = float(input())

found_root = False
i = 1

while not found_root:
    c = (a + b) / 2
    if f(c) == 0 or abs(b - a) < error_coef:
        print("A raiz", c, "foi encontrada após", i, "iterações.")
        found_root = True
    elif f(c) * f(a) < 0:
        b = c
    else:
        a = c
    i = i + 1