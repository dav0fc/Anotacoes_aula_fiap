import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class SaidaEmArquivo {
    public static void main(String[] args) throws IOException {
        PrintWriter arquivo = new PrintWriter(new FileWriter("saida.txt"));

        String texto = "carlinhos recordista";
        texto = texto.toUpperCase();
        arquivo.println(texto);
        arquivo.close();
    }
}
