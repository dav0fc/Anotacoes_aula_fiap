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
var nome = prompt("Digite seu nome: ");
var titulo = document.querySelector('h1')
titulo.innerText = `Olá ${nome}, seja bem-vindo!`