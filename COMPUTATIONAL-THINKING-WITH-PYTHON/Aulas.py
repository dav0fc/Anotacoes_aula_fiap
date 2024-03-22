''' AULA 1
nome = input("Diga seu nome: ")
p_n = int(input(f"{nome}, Diga um numero: "))
s_n = int(input(f"{nome}, Diga outro numero: "))

operacao = p_n + s_n
print(f"A soma de {p_n} e {s_n} dá {operacao} ")

operacao = p_n - s_n
print(f"A subtração de {p_n} e {s_n} dá {operacao} ")

operacao = p_n / s_n
print(f"A divisão de {p_n} e {s_n} dá {operacao} ")

operacao = p_n * s_n
print(f"A multiplicação de {p_n} e {s_n} dá {operacao} ")

frase = "O"
print(frase)
frase = frase + " São Paulo"
print(frase)
frase = frase + " foi"
print(frase)
frase = frase + " roubado"
print(frase)
frase = frase + " domingo"
print(frase)'''
import math

'''AULA 2
p_n = 2
s_n = 3

a = p_n < s_n
print(f"A comparação {p_n}<{s_n} é {a}.")

a = p_n > s_n
print(f"A comparação {p_n}>{s_n} é {a}.")

a = p_n <= s_n
print(f"A comparação {p_n}<={s_n} é {a}.")

a = p_n >= s_n
print(f"A comparação {p_n}>={s_n} é {a}.")

a = p_n == s_n
print(f"A comparação {p_n}={s_n} é {a}.")

a = p_n != s_n
print(f"A comparação {p_n}≠{s_n} é {a}.")



a = 2
b = 3
c = 4
d = 5

print("Comparações OR\n")

print(f"A comaparação {a}<{b} or {c}<{d}, ou seja {a<b} or {c<d} dá {a<b or c<d} ")

print(f"A comaparação {a}<{b} or {c}>{d}, ou seja {a<b} or {c>d} dá {a<b or c>d} ")

print(f"A comaparação {a}>{b} or {c}<{d}, ou seja {a>b} or {c<d} dá {a>b or c<d} ")

print(f"A comaparação {a}>{b} or {c}>{d}, ou seja {a>b} or {c>d} dá {a>b or c>d} \n")

print("Comparações AND\n")

print(f"A comaparação {a}<{b} and {c}<{d}, ou seja {a<b} and {c<d} dá {a<b and c<d} ")

print(f"A comaparação {a}>{b} and {c}>{d}, ou seja {a>b} and {c>d} dá {a>b and c>d} ")

print(f"A comaparação {a}<{b} and {c}>{d}, ou seja {a<b} and {c>d} dá {a<b and c>d} ")

print(f"A comaparação {a}>{b} and {c}<{d}, ou seja {a>b} and {c<d} dá {a>b and c<d} ")



idade = int(input("Diga sua idade: "))

if idade < 18:
    print("Você não pode beber, na teoria :).")
    print("Que feio!")
if idade => 18:
    print("Pode bebeeerrr")



idoso = input("Você é idoso? ")
cadeirante = input("Você é cadeirante? ")

if idoso == 'sim':
    print("Pode estacionar!")

if cadeirante == 'sim':
    print("Pode estacionar!")


idoso = input("Você é idoso? ")
cadeirante = input("Você é cadeirante? ")

if idoso == 'sim' or cadeirante == 'sim':
    print("Pode estacionar!")



idade = int(input("Diga sua idade: "))

if idade < 18:
    print("Você não pode beber, na teoria :).")
    print("Que feio!")
else :
    print("Pode bebeeerrr")




letra = input("Digite uma letra: ")

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U' :
    print(" é uma vogal")
else :
    print(f"{letra} é uma consoante")




letra = input("Digite uma letra: ")
vogal = False

if letra == 'A' or letra == 'a':
    print(" é uma vogal")
    vogal = True

if letra == 'E' or letra == 'e':
    print(" é uma vogal")
    vogal = True

if letra == 'I' or letra == 'i':
    print(" é uma vogal")
    vogal = True

if letra == 'O' or letra == 'o':
    print(" é uma vogal")
    vogal = True

if letra == 'U' or letra == 'u':
    print(" é uma vogal")
    vogal = True

if not vogal:
    print(" é uma consoante")



letra = input("Digite uma letra: ")

if letra == 'A' or letra == 'a':
    print(" é uma vogal")

elif letra == 'E' or letra == 'e':
    print(" é uma vogal")


elif letra == 'I' or letra == 'i':
    print(" é uma vogal")


elif letra == 'O' or letra == 'o':
    print(" é uma vogal")


elif letra == 'U' or letra == 'u':
    print(" é uma vogal")

else:
    print(" é uma consoante")


print("-------------------------------")
print("        HORA DO LEÃO           \n")
salario = float(input("Me diga seu salario para eu descontar: R$"))


if salario <= 1903.98 :
    aliquota = 0
    print("Voce está isento\n")
    print("       ESCAPOU DO LEÃO         ")
    print("-------------------------------")

elif 1903.99 < salario  :
    aliquota = 7.5/100

elif 2826.66 < salario   :
    aliquota = 15/100

elif 3751.06 < salario  :
    aliquota = 22.5/100

else  :
    aliquota = 27.5/100
desconto = aliquota * salario
salario =  salario - desconto

if aliquota != 0 :
    print(f"Seu desconto é de R${desconto} e seu Salario liquido é de R${salario}\n")
    print(" MUITO OBRIGADO POR CONTRIBUIR ")
    print("-------------------------------")'''

#Questao 1
'''
valor_1 = int(input("Escreva um valor: "))
valor_2 = int(input("Escreva um valor: "))

if valor_2 - valor_1 < 0:
    guardar = valor_1
    valor_1 = valor_2
    valor_2 = guardar
print(valor_2)'''

#Questao 2
'''
nasc = int(input("Em que ano nasceu? "))
if 2024 - nasc >= 16:
    print("Você ja pode votar :)")
else:
    print("Você não pode votar. ")'''

#Questao 3
'''
senha = "1234"
senha_escrita = input("Digite sua senha: ")

if senha_escrita == senha :
    print("ACESSO CONCEDIDO")
else:
    print("ACESSO NEGADO")'''

#Questao 4
'''
macas = int(input("Quantas maçãs tem no carrinho? "))
if macas >= 12:
    multi = 0.25
else:
    multi = 0.30
total = multi * macas
print(f"O preço total é: R${total}")
print(multi)'''

#QUESTAO 5
'''
valor_1 = int(input("Escreva um valor: "))
valor_2 = int(input("Escreva um valor: "))
valor_3 = int(input("Escreva um valor: "))

if valor_2 - valor_1 < 0:
    guardar = valor_1
    valor_1 = valor_2
    valor_2 = guardar
elif valor_3 - valor_2 < 0:
    guardar = valor_2
    valor_2 = valor_3
    valor_3 = guardar
if valor_2 - valor_1 < 0:
    guardar = valor_1
    valor_1 = valor_2
    valor_2 = guardar

print(valor_1,valor_2,valor_3)
'''
#Questão 6

'''
sex = input("Seu sexo é (F/M): ")
alt = float(input("Sua altura é (Em M com ponto): "))

if sex == 'M' or sex == 'm':
    imc = 72.7 * alt- 58
elif sex == 'F' or sex == 'f':
    imc = 62.1 * alt - 44.7
else:
    imc = 0
    print("Sexo invalido.")
print(f"Seu IMC é: {imc}")'''

#Questão 7&8
'''
lados = int(input("Quantos lados tem o poligono regular? "))

if lados < 3:
    print('Não é um poligono')
else:
    l_m = float(input("Qual a medida desses lados? "))
    if lados == 3:
        peri = lados * l_m
        print(f'É um triangulo com perimetro: {peri}cm')
    elif lados == 4:
        peri = lados * l_m
        print(f'É um retangulo com perimetro: {peri}cm')
    elif lados == 5:
        peri = lados * l_m
        print(f'É um pentagono com perimetro: {peri}cm')
    else:
        print("Poligono não indentificado")'''
#Melhor colocar um print só

#Questão 9
'''

valor_1 = int(input("Escreva um valor: "))
valor_2 = int(input("Escreva um valor: "))
valor_3 = int(input("Escreva um valor: "))

if valor_1 > valor_2 and valor_1 > valor_3 :
    print(f"{Valor_1} é o maior)
elif valor_2 > valor_3 < 0:
    print(f"{Valor_2} é o maior)
else:
    print(f"{Valor_3} é o maior)
#or 

maior = a
if b > maior
    maior = b
if c > maior
    maior = c

print(valor_3)'''
#Da pra melhorar o codigo verificando quem é maior que quem
#Questao 10
'''
p_l = int(input("Me o valor do primeiro lado: "))
s_l = int(input("Me o valor do segundo lado: "))
t_l = int(input("Me o valor do terceiro lado: "))

if p_l == s_l == t_l:
    print("É um Triângulo Equilátero")
elif p_l == s_l or p_l == t_l or s_l == t_l:
    print("É um Triângulo Isóceles")
else:
    print("É um Triângulo Escaleno")'''
#Só o python da pra fazer p_l == s_l == t_l, nas outras linguagens tem que usar AND entre elas.
#Melhor com 1 print só.
#Questao 11
'''
a1 = int(input("Me diga um angulo: "))
a2 = int(input("Me outro um angulo: "))
a3 = int(input("Me outro um angulo: "))

if a1 == 90 or a2 == 90 or a3 == 90:
    print("É um Triângulo Retângulo. ")
elif a1 > 90 or a2 > 90 or a3 > 90:
    print("É um Triângulo Obtusângulo. ")
elif a1 < 90 or a2 < 90 or a3 < 90:
    print("É um Triângulo Acutângulo. ")'''
#Melhor com 1 print só
'''
password = '1234'
senha = ''
tentativa = 3
while password != senha and tentativa > 0:
    senha = input("Digite sua senha: ")
    tentativa = tentativa - 1
'''
'''Aula 4
lados = int(input("Diga qts lados: "))
if lados < 3:
    print("Não é um poligono")
elif lados > 5:
    print("Não indentificado")
else:
    if lados == 3:
        forma = 'Triângulo'
    elif lados == 4:
        forma = 'quadrado'
    else
        forma = 'Pentágono'
    medida = int(input("Diga a medida do lado: "))
    perimetro = lados*medida
    ´print(f"Você escolheu um {forma} de perimetro: {perimetro}")

vl = int(input("Qual era a velocidade do veicúlo(KM/H): "))
if vl <= 100:
    print("Carro isento, não aplicar multa.")
else:
    if vl <= 120:
        multa = 0.2 * vl
    elif vl <= 150:
        multa = 0.2 * 120 + 0.3 * vl
    else:
        multa = 0.2 * 120 + 0.3 * 150 + 0.4 * vl
    print(f"Veiculo a {vl}Km/h, aplica multa de R${multa:.2f} ")

qtd_ped = int(input("Quantos numeros quer?: "))
par = 0
qtd = 0
while qtd < qtd_ped:
    n = int(input("Me diga um numero: "))
    if n%2 == 0:
       par += 1
    qtd += 1
impar = 5 - par
print(f"Você digitou {par} pares e {impar} impares ")

senha = ''
qtd_senha = 4
while senha != '1234' and qtd_senha > 0:
    senha = input("Coloque sua senha: ")
    print("Senha errada.")
    qtd_senha -= 1
if senha != '1234':
    print("Conta bloqueada")
else:
    print("Seja bem vindo")
'''
qtd = 0
soma = 0
qtd_pedida = int(input("Quantos somar? "))
while qtd < qtd_pedida:
    qtd += 1
    soma += qtd
print(soma)
