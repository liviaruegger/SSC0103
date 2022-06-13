/**
 * Essa é a classe inicial do programa Bozó. Possui apenas o método main, que
 * cuida da execução do jogo.
 * 
 * @author Ana Lívia Ruegger Saldanha (N.USP 8586691)
 *
 */
public class Bozo {
	
	/**
	 * Método inicial do programa. Ele cuida da execução do jogo e possui um laço,
	 * no qual cada iteração representa uma rodada do jogo. Em cada rodada, o
	 * jogador joga os dados até 3 vezes e depois escolhe a posição do placar que
	 * deseja preencher. No final das rodadas a pontuação total é exibida.
	 * 
	 * @param args
	 * @throws java.io.IOException
	 */
	public static void main(java.lang.String[] args) throws java.io.IOException {
		RolaDados dados = new RolaDados(5);
		Placar placar = new Placar();
		
		System.out.println("Pressione ENTER para iniciar a rodada.");
		EntradaTeclado.leString();
		
		String rolar_novamente = "Quais dados você gostaria de rolar novamente?\n"
				               + "Digite os números dos dados separados por um espaço\n"
				               + "(ou pressione enter para passar a vez):\n";
		
		for (int i = 0; i < 10; i++) {
			System.out.println("==================== RODADA " + (i + 1) + "/10 ====================\n");
			
			int[] ultima_rolagem = dados.rolar();
			System.out.println("Primeira rolagem de dados:");
			System.out.println(dados.toString());
			
			System.out.println(rolar_novamente);
			String input = EntradaTeclado.leString();
			if (input != "") ultima_rolagem = dados.rolar(input);
			System.out.println("\nSegunda rolagem de dados:");
			System.out.println(dados.toString());
			
			System.out.println(rolar_novamente);
			input = EntradaTeclado.leString();
			if (input != "") ultima_rolagem = dados.rolar(input);
			System.out.println("\nTerceira rolagem de dados:");
			System.out.println(dados.toString());
			
			System.out.println("Este é o placar atual:");
			System.out.println(placar.toString());
			
			System.out.println("Qual posição você quer ocupar?\n");
			int posicao = EntradaTeclado.leInt();
			placar.add(posicao, ultima_rolagem);
			System.out.println("\nPlacar atualizado:");
			System.out.println(placar.toString());
			
			System.out.println("Pontuação atual: " + placar.getScore());
			System.out.println("\nPressione ENTER para finalizar a rodada.");
			EntradaTeclado.leString();
		}
		
		System.out.println("==================== FIM DE JOGO! ====================\n");
		System.out.println("Pontuação final: " + placar.getScore());
	}

}
