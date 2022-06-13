import java.io.IOException;

/**
 * SSC0103 - Programação Orientada a Objetos
 * Lista de exercícios #1 (Java)
 * Exercício 09
 * 
 * @author Ana Lívia Ruegger Saldanha (N.USP 8586691)
 *
 */
public class Ex9 {
	
	/**
	 * Este método calcula raízes da equação x^3 - x^2 - 13x + 8
	 * através do método de Newton-Raphson, com erro inferior a
	 * 10^(-7).
	 * 
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException {
		System.out.println("Forneça um chute inicial:");
		double xi = EntradaTeclado.leDouble();
		
		double error_coef = 0.0000001;
		double error = 1; // Iniciando com um valor maior que o erro desejado.

		int i = 0;
		while (error > error_coef) {
			double aux = xi;
			xi = aux - (f(aux) / f_derivative(aux));
			error = Math.abs(xi - aux);
			i++;
		}		
		
		System.out.printf("A raiz %.7f foi encontrada após %d iterações.", xi, i);
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
	
	/**
	 * Calcula a função f'(x) = 3x^2 + 2x - 13
	 * para o x recebido como parâmetro.
	 * 
	 * @param x
	 * @return f'(x)
	 */
	public static double f_derivative(double x) {
		return (3 * Math.pow(x,2)) - (2 * x) - 13; 
	}

}
