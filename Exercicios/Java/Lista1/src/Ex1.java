import java.io.IOException;

/**
 * SSC0103 - Programação Orientada a Objetos
 * Lista de exercícios #1 (Java)
 * Exercício 01
 * 
 * @author Ana Lívia Ruegger Saldanha (N.USP 8586691)
 *
 */
public class Ex1 {
	
	/**
	 * Este método calcula, a partir de um chute inicial x_0, a raiz
	 * quadrada de um número lido do teclado.
	 * 
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException {
		System.out.print("Digite o número cuja raiz quadrada será calculada: ");
		double x = EntradaTeclado.leDouble();
		
		System.out.print("Digite um chute inicial para a raiz quadrada: ");
		double xi = EntradaTeclado.leDouble();
		
		double error_coef = 0.00000001;
		double error = 1; // Iniciando com um valor maior que o erro desejado.
		
		while (error > error_coef) {
			double aux = xi; 
			xi = (aux + (x / aux)) / 2; 			
			error = Math.abs(xi - aux);
		}
		
		System.out.printf("A raiz quadrada de %.8f é %.8f\n", x, xi);
	}

}
