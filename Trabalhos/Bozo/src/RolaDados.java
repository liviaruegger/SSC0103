/**
 * Esta é uma classe auxiliar que permite gerenciar um conjunto de vários dados
 * simultaneamente. Operações como rolar alguns dos dados ou exibir o resultado
 * de todos eles são implementadas.
 * 
 * @author Ana Lívia Ruegger Saldanha (N.USP 8586691)
 *
 */
public class RolaDados {
	private int n_dados;
	private Dado[] dados;
	
	public RolaDados(int n) {
		n_dados = n;
		dados = new Dado[n_dados];
		
		for (int i = 0; i < n_dados; i++) {
			dados[i] = new Dado();
		}
	}
	
	/**
	 * Rola todos os dados.
	 * 
	 * @return Retorna o valor de cada um dos dados.
	 */
	public int[] rolar() {
		int[] resultado = new int[n_dados];
		for (int i = 0; i < n_dados; i++) {
			resultado[i] = dados[i].rolar();
		}
		
		return resultado;
	}
	
	/**
	 * Rola alguns dos dados.
	 * 
	 * @param quais É um array de booleanos que indica quais dados devem ser rolados.
	 * Cada posição representa um dos dados. Ou seja, a posição 0 do array indica se
	 * o dado 1 deve ser rolado ou não, e assim por diante.
	 * @return Retorna o valor de cada um dos dados, inclusive os que não foram rolados.
	 * Nesse caso, o valor retornado é o valor anterior que ele já possuia.
	 */
	public int[] rolar(boolean[] quais) {
		int[] resultado = new int[n_dados];
		for (int i = 0; i < n_dados; i++) {
			if (quais[i] == true) {				
				resultado[i] = dados[i].rolar();
			} else {
				resultado[i] = dados[i].getLado();
			}
		}
		
		return resultado;
	}
	
	/**
	 * Rola alguns dos dados.
	 * 
	 * @param s É um String que possui o número dos dados a serem rolados. Por exemplo,
	 * "1 4 5" indica que os dados 1, 4 e 5 devem ser rolados. Os números devem ser
	 * separados por espaços. Se o valor passado no string estiver fora do intervalo
	 * válido, ele é ignorado simplesmente.
	 * @return Retorna o valor de cada um dos dados, inclusive os que não foram rolados.
	 * Nesse caso, o valor retornado é o valor anterior que ele já possuia.
	 */
	public int[] rolar(java.lang.String s) {
		String[] tokens = s.split(" ");
		for (String t : tokens) {
			int i = Integer.parseInt(t);
			if (i > 0 && i <= n_dados) {
				dados[i - 1].rolar();
			}
		}
		
		int[] resultado = new int[n_dados];
		for (int i = 0; i < n_dados; i++) {
			resultado[i] = dados[i].getLado();
		}
		
		return resultado;
	}
	
	/**
	 * Usa a representação em string dos dados para mostrar o valor de todos os dados
	 * do conjunto. Exibe os dados horizontalmente.
	 */
	public java.lang.String toString() {
		String[][] dados_split = new String[n_dados][];
		for (int i = 0; i < n_dados; i++) {
			String s = dados[i].toString();
			String[] tokens = s.split("\n");
			dados_split[i] = tokens;
		}
		
		String saida = "";
			
		// Primeira linha
		for (int i = 0; i < n_dados; i++) {
			saida += " ";
			saida += Integer.toString(i + 1);
			saida += "         ";
		}
		saida += "\n";
		
		// Dados
		for (int k = 0; k < 5; k++) {
			for (int i = 0; i < n_dados; i++) {
				saida += dados_split[i][k];
				saida += "    ";
			}
			saida += "\n";
		}
		
		return saida;
	}
	
	/**
	 * Método utilizado apenas para testes.
	 * @param args
	 */
	public static void main(java.lang.String[] args) {
		RolaDados teste = new RolaDados(5);
		teste.rolar();
		System.out.print(teste.toString());
		
		boolean[] quais = {true, false, true, false, true};
		teste.rolar(quais);
		System.out.print(teste.toString());
		
		teste.rolar("2 4");
		System.out.print(teste.toString());
	}
}
