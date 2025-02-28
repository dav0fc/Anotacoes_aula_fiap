import java.sql.SQLOutput;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        /*for(String entrada : args) {

			System.out.println("O argumento de entreda é  " + entrada);

		}*/

        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite o seu nome: ");
        String nome = entrada.nextLine();
        System.out.println("O nome digitado é  " + nome);
        System.out.printf("O nome digitado é %s", nome);
        System.out.println("Digite sua idade");
        int idade = entrada.nextInt();
        System.out.printf("O nome digitado é %s e a idade digitada é %d.", nome,idade);
        entrada.close();
    }
}

