# SSC0103 - Programação Orientada a Objetos
# Lista de exercícios #1 (Python)
# Exercício 09
# 
# Ana Lívia Ruegger Saldanha (N.USP 8586691)

'''
Este programa calcula raízes da equação x^3 - x^2 - 13x + 8 através do método
de Newton-Raphson, com erro inferior a 10^(-7).
'''


def f(x):
    return pow(x,3) - pow(x,2) - (13 * x) + 8

def f_derivative(x):
    return (3 * pow(x,2)) - (2 * x) - 13

xi = float(input("Forneça um chute inicial:"))

error_coef = 0.0000001
error = 1 # Iniciando com um valor maior que o erro desejado.

i = 0
while error > error_coef:
	aux = xi
	xi = aux - (f(aux) / f_derivative(aux))
	error = abs(xi - aux)
	i = i + 1

print("A raiz", xi, "foi encontrada após", i, "iterações.")