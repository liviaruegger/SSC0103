import java.io.File;
import java.io.FileNotFoundException;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

/**
 * Esta classe recebe no construtor um nome de arquivo, abre esse arquivo
 * e lê seu conteúdo, inserindo em um mapa as palavras encontradas e seu
 * número de ocorrências.
 * 
 * @author Ana Lívia Ruegger Saldanha (N.USP 8586691)
 *
 */
public class ContaPalavra {
	private TreeMap<String,Integer> word_count_map;
	private File fp;
	
	public ContaPalavra(String filename) {
		word_count_map = new TreeMap<String,Integer>();
		
		String filepath = System.getProperty("user.dir") + '/' + filename;
		fp = new File(filepath);
	}
	
	public int criaMapa() throws FileNotFoundException {
		Scanner file_stream = new Scanner(fp);
		
		while (file_stream.hasNext()) {
			String word = file_stream.next();
			
			if (word_count_map.containsKey(word)) {
				Integer count = word_count_map.get(word);
				word_count_map.replace(word, count + 1);
			} else {
				word_count_map.put(word, 1);
			}
		}
		
		return 1;
	}

	public void mostraMapa() {
		for (Map.Entry m : word_count_map.entrySet()) {
		    System.out.println(m.getKey() + " " + m.getValue());
		}
	}

	public static void main(String[] args) throws FileNotFoundException {
		ContaPalavra teste = new ContaPalavra("teste.txt");
		teste.criaMapa();
		teste.mostraMapa();
	}
}
