import java.io.IOException;

/**
 * SSC0103 - Programação Orientada a Objetos
 * Lista de exercícios #1 (Java)
 * Exercício 08
 * 
 * @author Ana Lívia Ruegger Saldanha (N.USP 8586691)
 *
 */
public class Ex8 {
	
	/**
	 * Este método calcula raízes da equação x^3 - x^2 - 13x + 8
	 * através do método da bisseção, com erro inferior a 10^(-7).
	 * 
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException {
		double error_coef = 0.0000001;
		double a, b;

		System.out.println("Forneça os extremos do intervalo [a,b]:");
		a = EntradaTeclado.leDouble();
		b = EntradaTeclado.leDouble();

		while (f(a) * f(b) >= 0) {
			System.out.println("Os valores de a e b devem ser tais que f(a) * f(b) < 0");
			System.out.println("Forneça novos valores para os extremos do intervalo [a,b]:");
			a = EntradaTeclado.leDouble();
			b = EntradaTeclado.leDouble();
		}
		
		boolean found_root = false;
		int i = 1;
		
		while (!found_root) {
			double c = (a + b) / 2;
			if (f(c) == 0 || Math.abs(b - a) < error_coef) {
				System.out.printf("A raiz %.7f foi encontrada após %d iterações.", c, i);
				found_root = true;
			} else if (f(c) * f(a) < 0) {
				b = c;
			} else {
				a = c;
			}
			i++;
		}		
	}
	
	/**
	 * Calcula a função f(x) = x^3 - x^2 - 13x + 8
	 * para o x recebido como parâmetro.
	 * 
	 * @param x
	 * @return f(x)
	 */
	public static double f(double x) {
		return Math.pow(x,3) - Math.pow(x,2) - (13 * x) + 8; 
	}

}
