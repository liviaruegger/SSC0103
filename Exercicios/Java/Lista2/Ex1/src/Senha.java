/**
 * SSC0103 - Programação Orientada a Objetos
 * Lista de exercícios #2
 * Exercício 01
 * 
 * @author Ana Lívia Ruegger Saldanha (N.USP 8586691)
 *
 */
public class Senha {
	
	public static void main(String[] args) {
		System.out.println("Digite N. Será gerada uma senha entre 0 e N.");
		int n = handlesExceptionInt();
		
		Random random = new Random();
		int senha = random.getIntRand(n);
		
		int tentativas = 0;
		boolean acertou = false;
		while (!acertou) {
			System.out.println("Digite um chute:");
			int chute = handlesExceptionInt();
			tentativas++;
			
			if (chute == senha) {
				System.out.println("Parabéns! Você acertou em " + tentativas + " tentativa(s)!");
				acertou = true;
			} else if (chute < senha) {
				System.out.println("O valor chutado é menor que a senha.");
			} else {
				System.out.println("O valor chutado é maior que a senha.");
			}		
		}
	}
	
	/**
	 * Este método trata exceções na leitura de um inteiro do
	 * teclado. Caso a leitura não seja válida, pede que o usuário
	 * digite novamente até obter um valor válido.
	 * 
	 * @return inteiro lido.
	 */
	public static int handlesExceptionInt() {
		boolean read_int = false;
		int n = -1; // Iniciando a variável com um valor qualquer.
		
		while (!read_int) {
			try {
				n = EntradaTeclado.leInt();
				read_int = true;
			} catch (Exception e) {
				System.out.println("Você deve digitar um inteiro!");
			}
		}
		
		return n;
	}

}
