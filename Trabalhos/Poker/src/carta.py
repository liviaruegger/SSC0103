"""
File:   carta.py
Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
Brief:  SSC0103 - Programação Orientada a Objetos
        Exercício: Video Poker
"""

from src.utils import *


class Carta:

    def __init__(self, valor, naipe: str) -> None:
        self.valor = valor
        self.naipe = naipe


    def __str__(self) -> str:
        valor_str = str(self.valor)
        if self.valor != 10:
            valor_str += " "

        borda = "+-----+\n"
        vazio = "|     |\n"
        centro = "| " + valor_str + self.naipe + " |\n"
        
        return (borda + vazio + centro + vazio + borda)