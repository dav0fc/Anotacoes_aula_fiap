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
// var resultado = document.getElementById('resultado')

// function somar(){
//     //Entrada
//     var n1 = parseFloat(document.getElementById('n1').value)
//     var n2 = parseFloat(document.getElementById('n2').value)

//     //Calculo
//     var soma = n1 + n2

//     //Saida
//     resultado.innerText = soma
//     console.log(soma)
// }

// function subt(){
//     //Entrada
//     var n1 = parseFloat(document.getElementById('n1').value)
//     var n2 = parseFloat(document.getElementById('n2').value)

//     //Calculo
//     var soma = n1 - n2

//     //Saida
//     resultado.innerText = soma
//     console.log(soma)
// }

// function mult(){
//     //Entrada
//     var n1 = parseFloat(document.getElementById('n1').value)
//     var n2 = parseFloat(document.getElementById('n2').value)

//     //Calculo
//     var soma = n1 * n2

//     //Saida
//     resultado.innerText = soma
//     console.log(soma)
// }

// function divi(){
//     //Entrada
//     var n1 = parseFloat(document.getElementById('n1').value)
//     var n2 = parseFloat(document.getElementById('n2').value)

//     //Calculo
//     if (n2 != 0){
//         var soma = n1 / n2
//         resultado.innerText = soma
//     }    
//     else{
//         resultado.innerText = "Não se divide por 0"
//     }
//     //Saida
    
//     console.log(soma)
// }
// function calculo_livros(){
//     var livros  = parseFloat(document.getElementById('livros').value)
//     var calculo = 0
//     if (livros < 7){
//         var calculo = livros * 22.00
//         console.log("1")
//     }
//     else{
//         var calculo = livros * 15.00
//         console.log("2")
//     }
//     resultado.innerText = `Irá ficar R$${calculo} reais totais`
// }
// function escolha_cargo(){
//     var cargo  = document.getElementById('cargo').value
//     var calculo = 0
//     var salario = 3000
//     console.log(cargo)
//     switch (cargo){
//         case 'junior': 
//             calculo = salario 
//             console.log("1")
//             break
//         case 'pleno':
//             calculo = salario * 2
//             console.log("2")
//             break
//         case 'senior':
//             calculo = salario * 3
//             console.log("3")
//             break
//         case 'techlead':
//             calculo = salario * 4
//             console.log("4")
//             break
//         case 'diretor':
//             calculo = salario * 5
//             console.log("5")
//             break
//         default:
//             console.log("6")
//             break
//     }
//     cargo_print.innerText = `O salario será R$${calculo} totais`
// }
// function contagem(){
//     var contagem = parseInt(document.getElementById('num').value)
//     var i = 0
//     var contando = contagem
//     while (i < contagem ){
//         i++
//         console.log(contando)
//         contando = contando - 1
//     }
// }
// for (i=1;i<=10;i++){
//     for (j=1;j<=10;j++){
//         console.log(`${i} X ${j} = ${i*j}`)
//     }
// }
// function tabuada(){
//     var numero = parseInt(document.getElementById('num').value)
//     for (i=1;i<=10;i++){
//         console.log(`${numero} X ${i} = ${numero*i}`)
//     }
// }
function verificar(){
    var numero = parseInt(document.getElementById('num').value)
    for (i=1;i<=numero;i++){
        if (numero % i === 0)
            console.log(i)
    }
}
