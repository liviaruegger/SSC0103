/**
 * SSC0103 - Programação Orientada a Objetos
 * Lista de exercícios #1 (Java)
 * Exercício 02
 * 
 * @author Ana Lívia Ruegger Saldanha (N.USP 8586691)
 *
 */
public class Ex2 {
	
	/**
	 * Este método lê do teclado os coeficientes de uma equação de
	 * segundo grau e apresenta sua solução.
	 * 
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println("Digite os coeficientes da equação:");
		int a, b, c;
		
		a = handlesExceptionInt();
		b = handlesExceptionInt();
		c = handlesExceptionInt();
		
		int delta = (int)(Math.pow(b, 2)) - 4 * a * c;
		
		if (delta < 0) {
			System.out.println("Esta equação não possui raízes reais.");
		} else {
			double x1 = (-b - Math.sqrt(delta)) / (2 * a);
			if (delta == 0) {
				System.out.printf("A raiz dupla desta equação é %f\n", x1);
			} else {
				double x2 = (-b + Math.sqrt(delta)) / (2 * a);
				System.out.printf("As raízes da equação são %f e %f\n", x1, x2);
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
