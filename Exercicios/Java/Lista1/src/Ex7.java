/**
 * SSC0103 - Programação Orientada a Objetos
 * Lista de exercícios #1 (Java)
 * Exercício 07
 * 
 * @author Ana Lívia Ruegger Saldanha (N.USP 8586691)
 *
 */
public class Ex7 {
	
	/**
	 * Este método lê vários números de ponto flutuante, um de cada
	 * vez, até que seja digitado o valor zero; identifica e mostra
	 * qual é o menor e qual é o maior valor dentre todos.
	 * 
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) {
		double n = handlesExceptionDouble();
		double max = n;
		double min = n;
		
		while (n != 0) {
			n = handlesExceptionDouble();
			if (n > max) {
				max = n;
			} else if (n != 0 && n < min) {
				min = n;
			}
		}
			
		System.out.printf("Menor valor: %f\n", min);
		System.out.printf("Maior valor: %f\n", max);
	}
	
	/**
	 * Este método trata exceções na leitura de um valor de ponto
	 * flutuante do teclado. Caso a leitura não seja válida, pede
	 * que o usuário digite novamente até obter um valor válido.
	 * 
	 * @return valor de ponto flutuante lido.
	 */
	public static double handlesExceptionDouble() {
		boolean read_double = false;
		double n = -1; // Iniciando a variável com um valor qualquer.
		
		while (!read_double) {
			try {
				n = EntradaTeclado.leDouble();
				read_double = true;
			} catch (Exception e) {
				System.out.println("Você deve digitar um valor de ponto flutuante!");
				System.out.println("Digite novamente, separando a parte decimal da parte inteira com um ponto.");
			}
		}
		
		return n;
	}
	
}
