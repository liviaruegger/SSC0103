"""
File:   main.py
Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
Brief:  SSC0103 - Programação Orientada a Objetos
        Exercício: Video Poker
"""

from sys import exit
from src.jogo import Jogo


def receber_valor(saldo_atual: int) -> int:
    entrada = input("Digite o valor da aposta ou 'F' para terminar: ")
    valor_aposta = None

    while valor_aposta == None:
        if entrada == 'F':
            print("\nJogo encerrado! Saldo final: $" + str(saldo_atual))
            exit(0)
        try:
            valor_aposta = int(entrada)
        except:
            entrada = input("Entrada inválida! Digite o valor da aposta ou 'F' para terminar: ")

    return valor_aposta


def main() -> None:
    jogo = Jogo()

    print("Jogo iniciado!\n")

    valor_aposta = None
    while jogo.get_saldo() > 0:
        print("Saldo atual: $" + str(jogo.get_saldo()))
        valor_aposta = receber_valor(jogo.get_saldo())

        while valor_aposta != None and (valor_aposta > jogo.get_saldo() or valor_aposta < 0):
            if valor_aposta > jogo.get_saldo():
                print("Saldo insuficiente!\n")
            elif valor_aposta < 0:
                print("Você não pode apostar um valor negativo!\n")
            print("Saldo atual: $" + str(jogo.get_saldo()))
            valor_aposta = receber_valor(jogo.get_saldo())

        jogo.apostar(valor_aposta)

        if jogo.get_saldo() <= 0:
            print("Você não tem mais créditos para apostar! Jogo encerrado!")


main()