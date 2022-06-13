import java.io.IOException;

/**
 * Simula um dado de número de lados variados. Ao criar o objeto é possível
 * estabelecer o número de lados. A rolagem do dado é feita por meio de um
 * gerador de números aleatórios (Random).
 * 
 * @author Ana Lívia Ruegger Saldanha (N.USP 8586691)
 *
 */
public class Dado {
	private int n_lados;
	private int cima;
	
	/**
	 * Cria um dado com 6 lados (um cubo).
	 */
	public Dado() {
		n_lados = 6;
	}
	
	/**
	 * Cria objeto com um número qualquer de lados.
	 * 
	 * @param n Número de lados do dado.
	 */
	public Dado(int n) {
		n_lados = n;
	}
	
	/**
	 * Recupera o último número selecionado.
	 * 
	 * @return o número do último lado selecionado.
	 */
	public int getLado() {
		return cima;
	}
	
	/**
	 * Simula a rolagem do dado por meio de um gerador aleatório. O número
	 * selecionado pode posteriormente ser recuperado com a chamada getLado().
	 * 
	 * @return o número que foi sorteado.
	 */
	public int rolar() {
		Random rd = new Random();
		
		try {
			Thread.sleep(5);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		cima = rd.getIntRand(n_lados) + 1;
		
		return cima;
	}
	
	/**
	 * Transforma a representação do dado em String. É mostrada uma representação
	 * do lado do dado que está para cima. Note que só funciona corretamente para
	 * dados de 6 lados.
	 */
	public java.lang.String toString() {
		if (n_lados != 6)
			return "";
		
		String dado = "";
		
		String borda    = "+-----+\n";
		String vazio    = "|     |\n";
		String esquerda = "|*    |\n";
		String meio     = "|  *  |\n";
		String direita  = "|    *|\n";
		String laterais = "|*   *|\n";
		
		switch(cima) {
		  case 1:
			  dado = borda + vazio + meio + vazio + borda;
			  break;
		  case 2:
			  dado = borda + esquerda + vazio + direita + borda;
			  break;
		  case 3:
			  dado = borda + esquerda + meio + direita + borda;
			  break;
		  case 4:
			  dado = borda + laterais + vazio + laterais + borda;
			  break;
		  case 5:
			  dado = borda + laterais + meio + laterais + borda; 
			  break;
		  case 6:
			  dado = borda + laterais + laterais + laterais + borda;
			  break;
		}
				
		return dado;
	}
	
	/**
	 * Método utilizado apenas para testes.
	 * @param args
	 */
	static public void main(String args[]) throws IOException {
		Dado teste = new Dado();
		int cmd = 1;
		while (cmd == 1) {
			cmd = EntradaTeclado.leInt();
			teste.rolar();
			System.out.println(teste.getLado());
			System.out.println(teste.toString());
		}		
	}

}
