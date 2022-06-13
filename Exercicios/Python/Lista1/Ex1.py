# SSC0103 - Programação Orientada a Objetos
# Lista de exercícios #1 (Python)
# Exercício 01
# 
# Ana Lívia Ruegger Saldanha (N.USP 8586691)

'''
Este programa calcula, a partir de um chute inicial x_0, a raiz quadrada de
um número lido do teclado.
'''


x = float(input("Digite o número cuja raiz quadrada será calculada: "))
xi = float(input("Digite um chute inicial para a raiz quadrada: "))

error_coef = 0.00000001
error = 1; # Iniciando com um valor maior que o erro desejado.

while error > error_coef:
    aux = xi
    xi = (aux + (x / aux)) / 2
    error = abs(xi - aux)

print("A raiz quadrada de", x, "é", xi)