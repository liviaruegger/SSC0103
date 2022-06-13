import java.util.Arrays;

/**
 * Esta classe representa o placar de um jogo de Bozó. Permite que combinações de dados
 * sejam alocadas às posições e mantém a pontuação de um jogador.
 * 
 * @author Ana Lívia Ruegger Saldanha (N.USP 8586691)
 *
 */
public class Placar {
	private static final int FULL_HAND = 7;
	private static final int SEQUENCIA = 8;
	private static final int QUADRA = 9;
	private static final int QUINA = 10;
	
	private int[] posicoes;
	
	public Placar() {
		posicoes = new int[10]; // Por padrão da linguagem, inicializa o array com zeros.
		Arrays.fill(posicoes, -1); // Preenche as posições desocupadas com -1.
	}
	
	/**
	 * Adiciona uma sequencia de dados em uma determinada posição do placar. Após a
	 * chamada, aquela posição torna-se ocupada e não pode ser usada uma segunda vez.
	 * 
	 * @param posicao Posição a ser preenchida. As posições 1 a 6 correspondem às
	 * quantidades de uns até seis, ou seja, as laterais do placar. As outas posições
	 * são: 7 - full hand; 8 - sequencia; 9 - quadra; e 10 - quina
	 * @param dados Um array de inteiros, de tamanho 5. Cada posição corresponde a um
	 * valor de um dado. Supões-se que cada dado pode ter valor entre 1 e 6.
	 * @throws java.lang.IllegalArgumentException Se a posição estiver ocupada ou se for
	 * passado um valor de posição inválido, essa exceção é lançada. Não é feita nenhuma
	 * verificação quanto ao tamanho do array nem quanto ao seu conteúdo.
	 */
	public void add(int posicao, int[] dados) throws java.lang.IllegalArgumentException {
		if (posicao <= 0 || posicao > 10) {
			throw new IllegalArgumentException("Esta posição é inválida.");
		} else if (posicoes[posicao - 1] != -1) {
			throw new IllegalArgumentException("Esta posição está ocupada.");
		}
		
		// Cria um array de contagem de dados
		int[] ocorrencias = new int[6];
		for (int i = 0; i < 5; i++) {
			ocorrencias[dados[i] - 1]++;
		}
		
		int pontuacao = 0;
		if (posicao >= 1 && posicao <= 6) {
			pontuacao = ocorrencias[posicao - 1] * posicao;
		} else if (posicao == FULL_HAND) {
			boolean repete2 = false;
			boolean repete3 = false;
			boolean repete5 = false;
			for (int i = 0; i < 6; i++) {
				if (ocorrencias[i] ==  2) repete2 = true;
				else if (ocorrencias[i] ==  3) repete3 = true;
				else if (ocorrencias[i] ==  5) repete5 = true;
			}
			if (repete2 && repete3 || repete5) pontuacao = 15;
		} else if (posicao == SEQUENCIA) {
			int streak = 0;
			for (int i = 0; i < 6; i++) {
				if (ocorrencias[i] == 1) streak++;
				else if (streak < 5) streak = 0;
			}
			if (streak == 5) pontuacao = 20;
		} else if (posicao == QUADRA) {
			for (int i = 0; i < 6; i++) {
				if (ocorrencias[i] >= 4) pontuacao = 30;
			}
		} else if (posicao == QUINA) {
			for (int i = 0; i < 6; i++) {
				if (ocorrencias[i] == 5) pontuacao = 40;
			}
		}
		
		posicoes[posicao - 1] = pontuacao;
	}
	
	/**
	 * Computa a soma dos valores obtidos, considerando apenas as posições que já estão
	 * ocupadas.
	 * 
	 * @return O valor da soma.
	 */
	public int getScore() {
		int pontuacao = 0;
		for (int i = 0; i < 10; i++) {
			if (posicoes[i] != -1) pontuacao += posicoes[i];
		}
		
		return pontuacao;
	}
	
	/**
	 * A representação na forma de string mostra o placar completo, indicando quais são
	 * as posições livres (com seus respectivos números) e o valor obtido nas posições
	 * já ocupadas.
	 */
	public java.lang.String toString() {
		String[] placares = new String[10];
		
		for (int i = 0; i < 10; i++) {
			if (posicoes[i] == -1) { // Vazio
				placares[i] = "(" + (i + 1) + ")";
				if (i < 9) placares[i] += " ";
			} else {
				if (posicoes[i] <= 9) placares[i] = posicoes[i] + "   "; // Um dígito
				else placares[i] = posicoes[i] + "  "; // Dois dígitos
			}
		}
		
		String placar_completo = "";
		
		// Três primeiras linhas da tabela
		for (int i = 0; i < 3; i++) {
			placar_completo += placares[i] + "   |   ";
			placar_completo += placares[i + 6] + "   |   ";
			placar_completo += placares[i + 3];
			placar_completo += "\n--------------------------\n";
		}
		
		// Última linha da tabela
		placar_completo += "       |   " + placares[9] + "   |";
		placar_completo += "\n       +----------+\n";
		
		return placar_completo;
	}
	
	/**
	 * Método utilizado apenas para testes.
	 * @param args
	 */
	public static void main(java.lang.String[] args) {
		Placar pl = new Placar();
		
		System.out.println("\nPontuação: " + pl.getScore());
		System.out.println(pl.toString());
		
		int[] dados_teste = {2, 2, 2, 3, 3};
		pl.add(FULL_HAND, dados_teste);
		System.out.println("\nPontuação: " + pl.getScore());
		System.out.println(pl.toString());
	}

}
