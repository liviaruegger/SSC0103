import java.io.IOException;

/**
 * SSC0103 - Programação Orientada a Objetos
 * Lista de exercícios #1 (Java)
 * Exercício 03
 * 
 * @author Ana Lívia Ruegger Saldanha (N.USP 8586691)
 *
 */
public class Ex3 {
    
	/**
	 * Este método lê um número inteiro n e apresenta uma "árvore"
	 * de altura n com a seguinte forma (exemplo para n = 3):
	 *     
	 *     ***
	 *     **
	 *     *
	 * 
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException {
		int n = EntradaTeclado.leInt();
		for (int i = 0; i < n; i++) {	
			for (int j = 0; j < n - i; j++) {
				System.out.print("*");				
			}
			System.out.println();
		}
	}
	
}
