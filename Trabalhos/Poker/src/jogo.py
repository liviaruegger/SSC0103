"""
File:   jogo.py
Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
Brief:  SSC0103 - Programação Orientada a Objetos
        Exercício: Video Poker
"""

from src.mao import Mao


class Jogo:

    def __init__(self, creditos=200) -> None:
        self.saldo = creditos


    def get_saldo(self) -> int:
        return self.saldo


    def apostar(self, aposta=0) -> None:
        self.saldo -= aposta
        self.mao_atual = Mao(aposta)
        print(self.mao_atual)

        trocar = input("Digite os números das cartas que você deseja trocar, separados por espaços: ")
        self.mao_atual.trocar(trocar)
        print(self.mao_atual)

        trocar = input("Digite os números das cartas que você deseja trocar, separados por espaços: ")
        self.mao_atual.trocar(trocar)
        print(self.mao_atual)

        pontuacao = self.mao_atual.pontuar()
        if pontuacao > 0:
            self.saldo += pontuacao
            print("Parabéns! Você acrescentou $" + str(pontuacao) + " ao seu saldo.\n")
        else:
            print("Que pena! Você não ganhou nada nessa rodada.\n")