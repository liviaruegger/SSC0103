"""
File:   mao.py
Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
Brief:  SSC0103 - Programação Orientada a Objetos
        Exercício: Video Poker
"""

from src.baralho import Baralho


class Mao:

    def __init__(self, aposta=0) -> None:
        self.aposta = aposta

        self.baralho = Baralho()
        self.baralho.shuffle()

        self.cartas = []
        for i in range(5):
            self.cartas.append(self.baralho.cartas.pop())

        self.contagem = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    

    def __str__(self) -> str:
        cartas_split = []
        for i in range(5):
            carta_str = self.cartas[i].__str__()
            tokens = carta_str.split("\n")
            cartas_split.append(tokens)

        saida = "\n"

        for i in range(5):
            for j in range(5):
                saida += cartas_split[j][i] + " "
            saida += "\n"

        for i in range(5):
            saida += "  (" + str(i + 1) + ")   "
        saida += "\n"

        return saida

    
    def __contar(self) -> None:
        for carta in self.cartas:
            if type(carta.valor) == int:
                self.contagem[carta.valor - 2] += 1
            elif carta.valor == 'J':
                self.contagem[9] += 1
            elif carta.valor == 'Q':
                self.contagem[10] += 1
            elif carta.valor == 'K':
                self.contagem[11] += 1
            elif carta.valor == 'A':
                self.contagem[12] += 1


    def __flush(self) -> bool:
        for carta in self.cartas:
            if carta.naipe != self.cartas[0].naipe:
                return False
        return True


    def __straight(self) -> bool:
        streak = 0
        for i in range(13):
            if self.contagem[i] == 1:
                streak += 1
            elif streak < 5:
                streak = 0
        if streak == 5:
            return True
        return False


    def __royal_straight_flush(self) -> bool:
        if not self.__flush():
            return False
        for i in range(9,13):
            if self.contagem[i] != 1:
                return False
        return True


    def __straight_flush(self) -> bool:
        if not self.__flush():
            return False
        if not self.__straight():
            return False
        return True


    def __quadra(self) -> bool:
        cont4 = self.contagem.count(4)
        return cont4 == 1


    def __full_hand(self) -> bool:
        cont2 = self.contagem.count(2)
        cont3 = self.contagem.count(3)
        return (cont2 == 1 and cont3 == 1)


    def __trinca(self) -> bool:
        cont3 = self.contagem.count(3)
        return cont3 == 1


    def __dois_pares(self) -> bool:
        cont2 = self.contagem.count(2)
        return cont2 == 2
    

    def trocar(self, quais: str) -> None:
        index = None
        while index == None:
            if quais == "":
                return

            try:
                index = quais.split(" ")
                for i in range(index.__len__()):
                    index[i] = int(index[i]) - 1
            except:
                index = None
                quais = input("Formato incorreto! Digite os números das cartas que você deseja trocar, separados por espaços: ")
        
        for i in index:
            if i >= 0 and i < 5:
                self.baralho.cartas.append(self.cartas[i])
                self.baralho.shuffle()
                self.cartas[i] = self.baralho.cartas.pop()


    def pontuar(self) -> int:
        multiplicador = 0
        self.__contar()

        if self.__royal_straight_flush():
            multiplicador = 200
        elif self.__straight_flush():
            multiplicador = 100
        elif self.__quadra():
            multiplicador = 50
        elif self.__full_hand():
            multiplicador = 20
        elif self.__flush():
            multiplicador = 10
        elif self.__straight():
            multiplicador = 5
        elif self.__trinca():
            multiplicador = 2
        elif self.__dois_pares():
            multiplicador = 1

        return (multiplicador * self.aposta)