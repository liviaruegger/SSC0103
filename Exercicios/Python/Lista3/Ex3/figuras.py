"""
File:   figuras.py
Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
Brief:  SSC0103 - Programação Orientada a Objetos
        Exercícios sobre herança e polimorfismo
        Exercício 03: Figuras geométricas
"""


import math


"""
Implemente classes para representar as figuras geométricas: círculo, retângulo e
quadrado. Para todas elas devem ser implementados métodos para retornar a área e
o perímetro. O círculo possui um raio e as outras classes os tamanhos dos lados.
Além disso as figuras possuem uma cor, definida por um atributo string e um
atributo “filled” que diz se a figura é preenchida pela cor ou se é vazia.
"""


class Figura:

    def __init__(self, cor: str, filled: bool) -> None:
        self.cor = cor
        self.filled = filled

    def get_info(self) -> None:
        print("Cor: " + self.cor)
        print("Preenchida: ", end="")
        if self.filled == True:
            print("sim")
        else:
            print("não")


class Circulo(Figura):

    def __init__(self, cor: str, filled: bool, raio: int) -> None:
        super().__init__(cor, filled)
        self.raio = raio
    
    def area(self) -> float:
        return math.pi * (self.raio ** 2)

    def perimetro(self) -> float:
        return 2 * math.pi * self.raio


class Quadrado(Figura):

    def __init__(self, cor: str, filled: bool, lado: int) -> None:
        super().__init__(cor, filled)
        self.lado = lado

    def area(self) -> int:
        return self.lado ** 2

    def perimetro(self) -> int:
        return 4 * self.lado


class Retangulo(Figura):

    def __init__(self, cor: str, filled: bool, a: int, b: int) -> None:
        super().__init__(cor, filled)
        self.a = a
        self.b = b
    
    def area(self) -> int:
        return self.a * self.b

    def perimetro(self) -> int:
        return 2 * self.a + 2 * self.b