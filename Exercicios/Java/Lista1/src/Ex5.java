import java.io.IOException;

/**
 * SSC0103 - Programação Orientada a Objetos
 * Lista de exercícios #1 (Java)
 * Exercício 05
 * 
 * @author Ana Lívia Ruegger Saldanha (N.USP 8586691)
 *
 */
public class Ex5 {
	
	/**
	 * Este método lê um número inteiro, verifica se ele é primo e,
	 * caso ele não seja, exibe qual o seu menor divisor.
	 * 
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException {
		int n = EntradaTeclado.leInt();
		for (int i = 2; i <= n/2; i++) {
			if (n % i == 0) {
				System.out.printf("O número %d é divisível por %d.\n", n, i);
				return;
			}
		}
		System.out.printf("O número %d é primo.\n", n);
	}

}
