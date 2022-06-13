"""
File:   baralho.py
Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
Brief:  SSC0103 - Programação Orientada a Objetos
        Exercício: Video Poker
"""

from random import shuffle
from src.carta import Carta
from src.utils import *


class Baralho:

    def __init__(self) -> None:
        self.cartas = []
        for naipe in naipes:
            for valor in valores:
                self.cartas.append(Carta(valor, naipe))


    def shuffle(self) -> None:
        shuffle(self.cartas)