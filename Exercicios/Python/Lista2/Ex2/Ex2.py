# SSC0103 - Programação Orientada a Objetos
# Lista de exercícios #2
# Exercício 02
# 
# Ana Lívia Ruegger Saldanha (N.USP 8586691)


from random import Random


class Adivinha:
    ''' Classe para adivinhar o número em que o usuário pensou.
    '''

    def chutar(self, min, max):
        rand = Random()
        chute = rand.get_int_rand(max - min) + min
        return chute

    def adivinhar(self, n):
        acertou = False
        min = 0
        max = n

        while not acertou:
            chute = self.chutar(min, max)

            print("Meu chute é ", chute)
            resposta = str(input("Acertei? Responda 'maior', 'menor' ou 'acertou': "))

            while resposta != 'maior' and resposta != 'menor' and resposta != 'acertou':
                print("Responda no formato correto!")
                resposta = str(input("Digite 'maior', 'menor' ou 'acertou': "))

            if resposta == "acertou":
                print("Eba! Sou muito bom nisso!")
                acertou = True
            elif resposta == "menor":
                max = chute - 1
            elif resposta == "maior":
                min = chute + 1


def main():
    input_correto = False
    while not input_correto:
        try:
            n = int(input("Digite o valor de N e pense em um número entre 0 e N: "))
            input_correto = True
        except:
            print("Você deve digitar um inteiro!")
    

    adivinhador = Adivinha()
    adivinhador.adivinhar(n)


main()