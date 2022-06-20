import unittest as ut
from Placar import Placar


class TestePlacar(ut.TestCase):

    def testPlacarVazio(self):
        pl = Placar()
        k = pl.getScore()
        self.assertEqual(0, k)

        self.assertEqual("Ones", pl.getName(0))
        self.assertEqual("Twos", pl.getName(1))
        self.assertEqual("Threes", pl.getName(2))
        self.assertEqual("Fours", pl.getName(3))
        self.assertEqual("Fives", pl.getName(4))
        self.assertEqual("Sixes", pl.getName(5))
        self.assertEqual("Full", pl.getName(6))
        self.assertEqual("Sequence", pl.getName(7))
        self.assertEqual("Four of a kind", pl.getName(8))
        self.assertEqual("General", pl.getName(9))

        placar_vazio_str = ("(1)    |   (7)    |  (4) \n"  +
		                    "-------|----------|-------\n" +
				            "(2)    |   (8)    |  (5) \n"  +
		                    "-------|----------|-------\n" +
				            "(3)    |   (9)    |  (6) \n"  +
		                    "-------|----------|-------\n" +
				            "       |   (10)   |\n"        +
		                    "       +----------+\n")
        placar_vazio_str_teste = pl.__str__()
        self.assertEqual(placar_vazio_str, placar_vazio_str_teste)


    def testPlacarCheio(self):
        pl = Placar()

        pl.add(1, [1, 1, 1, 1, 1])
        self.assertEqual(5, pl.getScore(0))
        self.assertEqual(5, pl.getScore())

        pl.add(2, [2, 2, 2, 2, 2])
        self.assertEqual(10, pl.getScore(1))
        self.assertEqual(15, pl.getScore())
        
        pl.add(3, [3, 3, 3, 3, 3])
        self.assertEqual(15, pl.getScore(2))
        self.assertEqual(30, pl.getScore())

        pl.add(4, [4, 4, 4, 4, 4])
        self.assertEqual(20, pl.getScore(3))
        self.assertEqual(50, pl.getScore())

        pl.add(5, [5, 5, 5, 5, 5])
        self.assertEqual(25, pl.getScore(4))
        self.assertEqual(75, pl.getScore())

        pl.add(6, [6, 6, 6, 6, 6])
        self.assertEqual(30, pl.getScore(5))
        self.assertEqual(105, pl.getScore())

        pl.add(7, [1, 1, 2, 2, 2])
        self.assertEqual(15, pl.getScore(6))
        self.assertEqual(120, pl.getScore())

        pl.add(8, [1, 2, 3, 4, 5])
        self.assertEqual(20, pl.getScore(7))
        self.assertEqual(140, pl.getScore())

        pl.add(9, [1, 2, 2, 2, 2])
        self.assertEqual(30, pl.getScore(8))
        self.assertEqual(170, pl.getScore())

        pl.add(10, [2, 2, 2, 2, 2])
        self.assertEqual(40, pl.getScore(9))
        self.assertEqual(210, pl.getScore())

        placar_cheio_str = (" 5     |    15    |   20 \n"  +
		                    "-------|----------|-------\n" +
				            " 10    |    20    |   25 \n"  +
		                    "-------|----------|-------\n" +
				            " 15    |    30    |   30 \n"  +
		                    "-------|----------|-------\n" +
				            "       |    40    |\n"        +
		                    "       +----------+\n")
        placar_cheio_str_teste = pl.__str__()
        self.assertEqual(placar_cheio_str, placar_cheio_str_teste)


    def testPosicaoIlegal(self):
        pl = Placar()
        self.assertRaises(IndexError, pl.add, 11, [1, 2, 3, 4, 5])
        self.assertRaises(IndexError, pl.add, 0, [1, 2, 3, 4, 5])

    
    def testPosicaoOcupada(self):
        pl = Placar()
        pl.add(1, [2, 3, 4, 5, 6])
        self.assertTrue(pl.getTaken(0))
        self.assertRaises(ValueError, pl.add, 1, [1, 2, 3, 4, 5])


    def testFullHand(self):
        pl = Placar()
        pl.add(7, [1, 2, 3, 4, 6])
        k = pl.getScore()
        self.assertEqual(0, k)

        pl = Placar()
        pl.add(7, [1, 1, 3, 4, 6])
        k = pl.getScore()
        self.assertEqual(0, k)

        pl = Placar()
        pl.add(7, [1, 1, 3, 3, 6])
        k = pl.getScore()
        self.assertEqual(0, k)

        pl = Placar()
        pl.add(7, [1, 1, 1, 4, 6])
        k = pl.getScore()
        self.assertEqual(0, k)

        pl = Placar()
        pl.add(7, [1, 1, 1, 4, 4])
        k = pl.getScore()
        self.assertEqual(15, k)


    def testQuadra(self):
        pl = Placar()
        pl.add(9, [1, 1, 1, 1, 2])
        k = pl.getScore()
        self.assertEqual(30, k)

        pl = Placar()
        pl.add(9, [1, 1, 2, 3, 4])
        k = pl.getScore()
        self.assertEqual(0, k)

        pl = Placar()
        pl.add(9, [1, 1, 1, 3, 4])
        k = pl.getScore()
        self.assertEqual(0, k)

        pl = Placar()
        pl.add(9, [1, 2, 2, 3, 4])
        k = pl.getScore()
        self.assertEqual(0, k)

        pl = Placar()
        pl.add(9, [1, 2, 2, 2, 4])
        k = pl.getScore()
        self.assertEqual(0, k)


    def testQuina(self):
        pl = Placar()
        pl.add(10, [1, 2, 3, 4, 5])
        k = pl.getScore()
        self.assertEqual(0, k)

        pl = Placar()
        pl.add(10, [2, 2, 3, 4, 5])
        k = pl.getScore()
        self.assertEqual(0, k)

        pl = Placar()
        pl.add(10, [2, 2, 2, 4, 5])
        k = pl.getScore()
        self.assertEqual(0, k)

        pl = Placar()
        pl.add(10, [2, 2, 2, 2, 5])
        k = pl.getScore()
        self.assertEqual(0, k)


    def testSequencia(self):
        pl = Placar()
        pl.add(8, [2, 3, 4, 5, 6])
        k = pl.getScore()
        self.assertEqual(20, k)

        pl = Placar()
        pl.add(8, [1, 6, 6, 6, 6])
        k = pl.getScore()
        self.assertEqual(0, k)

        pl = Placar()
        pl.add(8, [1, 2, 6, 6, 6])
        k = pl.getScore()
        self.assertEqual(0, k)

        pl = Placar()
        pl.add(8, [1, 2, 3, 5, 6])
        k = pl.getScore()
        self.assertEqual(0, k)

        pl = Placar()
        pl.add(8, [1, 2, 3, 6, 6])
        k = pl.getScore()
        self.assertEqual(0, k)

        pl = Placar()
        pl.add(8, [1, 2, 3, 4, 6])
        k = pl.getScore()
        self.assertEqual(0, k)


if __name__ == "__main__":
    ut.main()
