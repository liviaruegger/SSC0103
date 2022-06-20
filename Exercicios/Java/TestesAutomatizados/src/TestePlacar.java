import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class TestePlacar {
	
	private Placar pl;
	
	@Before
	public void setup() {
		pl = new Placar();
	}
	
	@After
	public void tearDown() {
		pl = null;
	}
	
	@Test
	public void testPlacarVazio() {
		int k = pl.getScore();
		assertEquals(0, k);
		
		String placar_vazio = "(1)    |   (7)    |   (4) \n" +
		                      "--------------------------\n" +
				              "(2)    |   (8)    |   (5) \n" +
		                      "--------------------------\n" +
				              "(3)    |   (9)    |   (6) \n" +
		                      "--------------------------\n" +
				              "       |   (10)   |\n"        +
		                      "       +----------+\n";
		String placar_vazio_teste = pl.toString();
		assertEquals(placar_vazio, placar_vazio_teste);
	}
	
	@Test
	public void testPlacarCheio() {	
		pl.add(1, new int[] {1, 1, 1, 1, 1});
		int k = pl.getScore();
		assertEquals(5, k);
		
		pl.add(2, new int[] {2, 2, 2, 2, 2});
		k = pl.getScore();
		assertEquals(15, k);		

		pl.add(3, new int[] {3, 3, 3, 3, 3});
		k = pl.getScore();
		assertEquals(30, k);

		pl.add(4, new int[] {4, 4, 4, 4, 4});
		k = pl.getScore();
		assertEquals(50, k);
		
		pl.add(5, new int[] {5, 5, 5, 5, 5});
		k = pl.getScore();
		assertEquals(75, k);
		
		pl.add(6, new int[] {6, 6, 6, 6, 6});
		k = pl.getScore();
		assertEquals(105, k);
		
		// Full hand (7) 
		pl.add(7, new int[] {1, 1, 2, 2, 2});
		k = pl.getScore();
		assertEquals(120, k);
		
		// Sequencia (8)
		pl.add(8, new int[] {1, 2, 3, 4, 5});
		k = pl.getScore();
		assertEquals(140, k);
		
		// Quadra (9)
		pl.add(9, new int[] {1, 2, 2, 2, 2});
		k = pl.getScore();
		assertEquals(170, k);
		
		// Quina (10)
		pl.add(10, new int[] {2, 2, 2, 2, 2});
		k = pl.getScore();
		assertEquals(210, k);
		
		String placar_cheio = "5      |   15     |   20  \n" +
                              "--------------------------\n" +
	                          "10     |   20     |   25  \n" +
                              "--------------------------\n" +
	                          "15     |   30     |   30  \n" +
                              "--------------------------\n" +
	                          "       |   40     |\n"        +
                              "       +----------+\n";
		String placar_cheio_teste = pl.toString();
		assertEquals(placar_cheio, placar_cheio_teste);
	}
	
	@Test
	public void testPosicaoIlegal() {
		assertThrows(IllegalArgumentException.class, () -> pl.add(11, new int[] {1, 2, 3, 4, 5}));
		assertThrows(IllegalArgumentException.class, () -> pl.add(0, new int[] {1, 2, 3, 4, 5}));
	}
	
	@Test
	public void testPosicaoOcupada() {
		pl.add(1, new int[] {2, 3, 4, 5, 6});
		assertThrows(IllegalArgumentException.class, () -> pl.add(1, new int[] {1, 2, 3, 4, 5}));
	}
	
	@Test
	public void testFullHand() {
		pl.add(7, new int[] {1, 2, 3, 4, 6});
		int k = pl.getScore();
		assertEquals(0, k);
		
		pl = null;
		pl = new Placar();
		pl.add(7, new int[] {1, 1, 3, 4, 6});
		k = pl.getScore();
		assertEquals(0, k);
		
		pl = null;
		pl = new Placar();
		pl.add(7, new int[] {1, 1, 3, 3, 6});
		k = pl.getScore();
		assertEquals(0, k);
		
		pl = null;
		pl = new Placar();
		pl.add(7, new int[] {1, 1, 1, 4, 6});
		k = pl.getScore();
		assertEquals(0, k);
		
		pl = null;
		pl = new Placar();
		pl.add(7, new int[] {1, 1, 1, 4, 4});
		k = pl.getScore();
		assertEquals(15, k);
	}
	
	@Test
	public void testQuadra() {
		pl.add(9, new int[] {1, 1, 1, 1, 2});
		int k = pl.getScore();
		assertEquals(30, k);
		
		pl = null;
		pl = new Placar();
		pl.add(9, new int[] {1, 1, 2, 3, 4});
		k = pl.getScore();
		assertEquals(0, k);
		
		pl = null;
		pl = new Placar();
		pl.add(9, new int[] {1, 1, 1, 3, 4});
		k = pl.getScore();
		assertEquals(0, k);
		
		pl = null;
		pl = new Placar();
		pl.add(9, new int[] {1, 2, 2, 3, 4});
		k = pl.getScore();
		assertEquals(0, k);
		
		pl = null;
		pl = new Placar();
		pl.add(9, new int[] {1, 2, 2, 2, 4});
		k = pl.getScore();
		assertEquals(0, k);
	}
	
	@Test
	public void testQuina() {
		pl.add(10, new int[] {1, 2, 3, 4, 5});
		int k = pl.getScore();
		assertEquals(0, k);		

		pl = null;
		pl = new Placar();
		pl.add(10, new int[] {2, 2, 3, 4, 5});
		k = pl.getScore();
		assertEquals(0, k);
		
		pl = null;
		pl = new Placar();
		pl.add(10, new int[] {2, 2, 2, 4, 5});
		k = pl.getScore();
		assertEquals(0, k);
		
		pl = null;
		pl = new Placar();
		pl.add(10, new int[] {2, 2, 2, 2, 5});
		k = pl.getScore();
		assertEquals(0, k);
	}
	
	@Test
	public void testSequencia() {
		pl.add(8, new int[] {2, 3, 4, 5, 6});
		int k = pl.getScore();
		assertEquals(20, k);
	
		pl = null;
		pl = new Placar();
		pl.add(8, new int[] {1, 6, 6, 6, 6});
		k = pl.getScore();
		assertEquals(0, k);
		
		pl = null;
		pl = new Placar();
		pl.add(8, new int[] {1, 2, 6, 6, 6});
		k = pl.getScore();
		assertEquals(0, k);
		
		pl = null;
		pl = new Placar();
		pl.add(8, new int[] {1, 2, 3, 5, 6});
		k = pl.getScore();
		assertEquals(0, k);
		
		pl = null;
		pl = new Placar();
		pl.add(8, new int[] {1, 2, 3, 6, 6});
		k = pl.getScore();
		assertEquals(0, k);	
		
		pl = null;
		pl = new Placar();
		pl.add(8, new int[] {1, 2, 3, 4, 6});
		k = pl.getScore();
		assertEquals(0, k);
	}
}
