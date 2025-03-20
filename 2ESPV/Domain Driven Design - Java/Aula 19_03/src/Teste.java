public class Teste {

	public static void main(String[] args) {
		
		Funcionario funcionario = new Funcionario(); // Cria instancia do objeto funcionario
		
		funcionario.matricula = "XX-11111"; // Atribui valores
		funcionario.setNome("Funcionario 1");
		funcionario.salario = 10000;
		
		funcionario.imprimir(); // faz a impressao
		funcionario.controlarPonto(funcionario.matricula, 8);
		
		Funcionario funcionario2 = new Funcionario("Funcionario 2", "XX-22222", 20000);
		funcionario2.imprimir();
		funcionario2.controlarPonto(8, funcionario2.matricula, funcionario2.getNome());


	}

}
