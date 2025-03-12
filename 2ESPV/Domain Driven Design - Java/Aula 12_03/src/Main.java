import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
//        Scanner scanner = new  Scanner(System.in);
//        System.out.println("Me dia um numero");
//        float n1 = scanner.nextFloat();
//        System.out.println("Outro numero");
//        float n2 = scanner.nextFloat();
//        float add = n1 + n2;
//        float sub = n1 - n2;
//        float div = n1 / n2;
//        float mult = n1 * n2;
//        float mod = n1 % n2;
//        System.out.println("A soma é " + add);
//        System.out.println("A subtração é " + sub);
//        System.out.println("A divisão é " + div);
//        System.out.println("A multiplicação é " + mult);
//        System.out.println("O modulo é " + mod);
//        scanner.close();
//        Scanner scanner = new  Scanner(System.in);
//        float n = 10;
//        System.out.println("O numero é " + n);
//        System.out.println("Soma 1");
//        n += 1;
//
//        System.out.println("O numero é " + n);
//        System.out.println("Tira 5");
//        n -= 5;
//
//        System.out.println("O numero é " + n);
//        System.out.println("Divide por 3");
//        n /= 3;
//
//        System.out.println("O numero é " + n);
//        System.out.println("Multiplica com 12");
//        n *= 12;
//
//        System.out.println("O numero é " + n);
//        System.out.println("Tira o modulo de 4");
//        n %= 4;
//
//        System.out.println("O numero final é " + n);
//        scanner.close();
//        Scanner scanner = new  Scanner(System.in);
//        System.out.println("Me diga 3 numeros");
//        int n1 = scanner.nextInt();
//        int n2 = scanner.nextInt();
//        int n3 = scanner.nextInt();
//
//        int maior  = n1;
//        int menor = n1;
//
//        if (n2 > maior && n2 > n3){
//            maior = n2;
//        } else if (n3 > maior && n3 > n2) {
//            maior = n3;
//        }
//
//        if (n2 < menor && n2 < n3){
//            menor = n2;
//        } else if (n3 < menor && n3 < n2) {
//            menor = n3;
//        }
//
//        System.out.println(maior+ " é o numero maior,  " + menor+ " é o numero menor");
//        scanner.close();
        Scanner scanner = new Scanner(System.in);
        boolean a = false;
        boolean b = true;

        boolean and = a && b;
        boolean or = a || b;
        boolean notA = !a;
        boolean notB =!b;

        System.out.println("Operador logico AND " +and);
        System.out.println("Operador logico OR "+ or);
        System.out.println("Operador logico NOTa " +notA);
        System.out.println("Operador logico NOTb " +notB);


        scanner.close();
    }
}