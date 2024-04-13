/* alert("Olá, Mundo!")
confirm("Voce deseja sair? Maxwell ficara triste contigo") */

/* // entrada
var nome = prompt("Digite seu nome: ");
var idade = 23

// saida
console.log("Olá " + nome + ", seja bem-vindo!")
console.log(`Olá ${nome}, seja bem-vindo!`) */
/* var nome = prompt("Escreva seu nome")
var idade = prompt("Escreva sua idade")
var trab = prompt("Escreva onde voce trabalha")
alert(`Olá ${nome}, voce tem ${idade} anos e trabalha na(o) ${trab}`) */
// var nome = prompt("Digite seu nome: ");
// var titulo = document.querySelector('h1');
// titulo.innerText = `Olá ${nome}, seja bem-vindo!`;

//Resultado
var resultado = document.getElementById('resultado')

function somar(){
    //Entrada
    var n1 = parseFloat(document.getElementById('n1').value)
    var n2 = parseFloat(document.getElementById('n2').value)

    //Calculo
    var soma = n1 + n2

    //Saida
    resultado.innerText = soma
    console.log(soma)
}

function subt(){
    //Entrada
    var n1 = parseFloat(document.getElementById('n1').value)
    var n2 = parseFloat(document.getElementById('n2').value)

    //Calculo
    var soma = n1 - n2

    //Saida
    resultado.innerText = soma
    console.log(soma)
}

function mult(){
    //Entrada
    var n1 = parseFloat(document.getElementById('n1').value)
    var n2 = parseFloat(document.getElementById('n2').value)

    //Calculo
    var soma = n1 * n2

    //Saida
    resultado.innerText = soma
    console.log(soma)
}

function divi(){
    //Entrada
    var n1 = parseFloat(document.getElementById('n1').value)
    var n2 = parseFloat(document.getElementById('n2').value)

    //Calculo
    if (n2 != 0){
        var soma = n1 / n2
        resultado.innerText = soma
    }    
    else{
        resultado.innerText = "Não se divide por 0"
    }
    //Saida
    
    console.log(soma)
}