import java.io.IOException;

/**
 * SSC0103 - Programação Orientada a Objetos
 * Lista de exercícios #1 (Java)
 * Exercício 06
 * 
 * @author Ana Lívia Ruegger Saldanha (N.USP 8586691)
 *
 */
public class Ex6 {
	
	/**
	 * Este método lê um número inteiro e exibe o primeiro número
	 * primo menor que o número informado.
	 * 
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException {
		int n = EntradaTeclado.leInt();
		for (int i = n - 1; i >= 2; i--) {
			boolean i_is_prime = true;
			for (int j = 2; j <= i/2; j++) {
				if (i % j == 0) {
					i_is_prime = false;
					break;
				}
			}
			if (i_is_prime == true) {
				System.out.print(i);
				return;
			}
		}
		System.out.printf("Não existe número primo menor que %d.", n);
	}

}
