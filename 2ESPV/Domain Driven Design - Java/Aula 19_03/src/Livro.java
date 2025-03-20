public class Livro {

    private String titulo = "Livro";
    private String autor = "Nome_Autor";
    private double desconto = 0.0;
    private double preco = 0.0;

    public Livro(){
        System.out.println("Livro foi criado!!");
    }
    public Livro(String titulo, String autor, double desconto, double preco){
        this.titulo = titulo;
        this.autor = autor;
        this.desconto = desconto;
        this.preco = preco;
    }


    public String getTitulo() {
        return titulo;
    }
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }


    public String getAutor() {
        return autor;
    }
    public void setAutor(String autor) {
        this.autor = autor;
    }


    public double getDesconto() {
        return desconto;
    }
    public void setDesconto(double desconto) {
        this.desconto = desconto;
    }


    public double getPreco() {
        return preco;
    }
    public void setPreco(double preco) {
        this.preco = preco;
    }


    public void aplicarDesconto(double descontoPorc){
        System.out.println("Aplicando desconto!!");
        if (descontoPorc < 1 && descontoPorc > 0) {
            this.desconto = descontoPorc;
            this.preco = this.preco - (this.preco * this.desconto);
        }
        else{
            System.out.println("Para de ser SAFADA");
        }
        System.out.println("Desconto Aplicado!!");
    }
    public void aplicarDesconto(int descontoFixo){
        System.out.println("Aplicando desconto!!");
        this.desconto = descontoFixo;
        this.preco = this.preco-this.desconto;
        System.out.println("Para de ser SAFADA");
    }
}
