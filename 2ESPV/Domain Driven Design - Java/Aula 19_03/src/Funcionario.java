public class Funcionario {
	
	private String nome;
	
	String matricula;
	
	double salario;
	
	public Funcionario() {System.out.println("Inicializou funcionario!");
	}

	public Funcionario(String nome, String matricula, double salario) {
		this.nome = nome;
		this.matricula = matricula;
		this.salario = salario;
	}
	
	public Funcionario(String nome, String matricula) {
		super();
		this.nome = nome;
		this.matricula = matricula;
	}
	
	void imprimir() {
		System.out.println("Funcionário " + nome + " da matricula "+ matricula + " tem o salario "+ salario);
	}
	
	//public void controlarPonto(String matricula, int jornada) {} - OK
	//public void controlarPonto(String matricula, int jornada) {} - Método duplicado
	//public void controlarPonto(int jornada, String matricula) {} - OK
	//public void controlarPonto(int jornada, String matricula, String nome) {} - OK
	//public int controlarPonto(int jornada, String matricula, String nome) {} - Não OK
	//public void controlarPonto(int jornada1, String matricula1, String nome1) {} - Não OK
	//public void controlarPonto(int jornada, String nome, String matricula ) {} - Não OK
	//public void controlarPonto( String matricula, int jornada, String nome) {} - OK
	
	public void controlarPonto(String matricula, int jornada) {
		System.out.println("Ponto registrado para a matrícula " + matricula + " com a jornada " + jornada);
	}
	
	public void controlarPonto(int jornada, String matricula, String nome) {
		System.out.println("Ponto registrado para a matrícula " + matricula + " com a jornada " + jornada + " do funcionario " + nome);
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}
}
