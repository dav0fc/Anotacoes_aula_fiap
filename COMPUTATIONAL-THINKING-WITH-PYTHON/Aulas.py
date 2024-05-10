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
print(frase)
import math
'''
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

i = 0
soma = 0
qtd_pedida = int(input("Quantos somar? "))
while i < qtd_pedida:
    i += 1
    soma += i*i
    print(soma)
'''

''' Aula 5
boleano = ''
while not(boleano == 'sim' or boleano == 'nao'):
    boleano = input("Digite sim ou nao: ")
    if boleano != 'sim' and boleano != 'Sim' and boleano != 'Nao' and boleano != 'nao':
        print("ESCREV DNV MARRECO")'''

'''#Questão 1 - Lista Loop
while True:
    num = input("Diga um Numero entre 0 a 10: ")
    if num.isnumeric():
        num = int(num)
        if num > 0 and num <= 10:
            break
        else:
            print("O numero deve ser entre 1 a 10")
    else:
        print("Escreva um numero")
print("Dentro do intervalo")'''

'''#Questão 2 - Lista Loop
while True:
    nome = input("Digite um nome (minimo 3 caracteres)->: ")
    nome_tamanho = len(nome)
    if nome_tamanho < 3:
        print("Valor errado. Digite novamente")
    else:
        break
while True:
    idade = input("Digite sua idade(entre 0 e 150)->:")
    if idade.isnumeric():
        idade = int(idade)
        if idade <= 150 and idade >= 0:
            break
        else:
            print("Valor errado. Digite novamente")
    else:
        print("Valor errado. Digite novamente")
while True:
    salario = input("Digite seu salario(Maior que 0)->:")
    if salario.isnumeric():
        salario = int(salario)
            break
        else:
            print("Valor errado. Digite novamente")
    else:
        print("Valor errado. Digite novamente")
while True:
    sexo = input("Digite seu sexo (F/M)->: ")
    if sexo == 'F' or sexo == 'M':
            break
    else:
        print("Valor errado. Digite novamente")
while True:
    estCivil = input("Digite seu estado civil.\n->\n:")
    if estCivil == 's' or 2 == 'c' or sexo == 'v' or sexo == 'd':
            break
    else:
        print("Valor errado. Digite novamente")'''
'''#Questao 3
populaA = 80000
populaB = 200000
taxaAnualA = 0.03
taxaAnualB = 0.15
anos = 0

def quebrar():
    while populaA < populaB:
        populaA += populaA * taxaAnualA
        populaB += populaB * taxaAnualB
        print(populaA)
        print(populaB)
        anos += 1
    print(anos)'''

'''Questao 4
i = 0
num = 0
while i < 5:
    num_n = input("Digite um numero: ")
    if num_n.isnumeric():
        num_n = int(num_n)
        i += 1
        num_qtd = i
        num += num_n
        print (num)
    else:
        print("Valor errado. Digite novamente")
num = num / num_qtd
print(num)'''

'''#Questao 5

i = 0
aux = 0
while True:
    n1 = input("Primeiro numero: ")
    n2 = input("Segundo numero: ")
    if n1.isnumeric() and n2.isnumeric():
        n1 = int(n1)
        n2 = int(n2)
        break
    else:
        print("Valor errado. Digite novamente")
if n1 > n2:
    aux = n2
    n2 = n1
    n1 = aux
while n1 < n2 :
    n1 += 1 
    if n1 == n2:
        break
    else:
        print(n1)'''

'''Questao 6
while True:
    usuario = input("Digite um nome de usuario: ")
    senha = input("Digite uma senha: ")
    if usuario == senha:
        print("Senha não pode ser igual ao nome de usuario.")
    else:
        break'''
'''Questao 7
num = input("Digite um numero pra ver a tabuada: ")
i = 0
while True:
    if num.isnumeric():
        num = int(num)
        break
    else:
        print("Valor errado. Digite novamente")
while i <= 10:
    i += 1
    num_tab = num * i
    print(f"{num} X {i} = {num_tab} ")
    i = 0
j = 0
k = 0
while j < 10:
    j += 1
    while i < 100:
        i += 1
        num_tab = j * i
        print(f"{j} X {i} = {num_tab} ")
    i = 0 '''

'''#Questao 8
i = 0
pos1 = 0
pos2 = 1
while True:
    fibo = input("Digite o n-nésimo numero do Fibbonaci: ")
    if fibo.isnumeric():
        fibo = int(fibo)
        break
    else:
        print("Valor errado. Digite novamente")
while not i == fibo:
    i += 1
    print(pos2)
    pos3 = pos1 + pos2
    pos1 = pos2
    pos2 = pos3'''

'''Questao 9
i = 0
par = 0
impar = 0
while i < 10:
    i += 1
    while True:
        num = input("Digite um numero: ")
        if num.isnumeric():
            num = int(num)
            break
        else:
            print("Valor errado. Digite novamente")
    if not num % 2:
        par += 1
    else:
        impar += 1
print(f"São {par} pares e {impar} impares")'''

'''Questao 10
i = 0
fat_r = 1
while True:
    fat = input("Digite um numero pra fatorar: ")
    if fat.isnumeric():
        fat = int(fat)
        break
    else:
        print("Valor errado. Digite novamente")
while i < fat:
    i += 1
    fat_r = fat_r * i
    print(fat_r)'''

'''Questao 11
while True:
    num = input("Digite um numero pra varificar se é primo: ")
    if num.isnumeric():
        num = int(num)
        break
    else:
        print("Valor errado. Digite novamente")
if num % 2 and num != 1 or num == 2 : 
    print(f"{num} é primo.")
else:
    print(f"{num} não é primo.")'''

'''Questao 12
while True:
    nota_n = input("Digite o numero de notas: ")
    if nota_n.isnumeric():
        nota_n = int(nota_n)
        break
    else:
        print("Valor errado. Digite novamente")
i = 0
nota_c = 0
while i < nota_n:
    i += 1
    while True:
        nota = input("Digite uma nota: ")
        if nota.isnumeric():
            nota = int(nota)
            break
        else:
            print("Valor errado. Digite novamente")
    nota_c += nota
nota = nota_c / nota_n
print(f" a media aritimetica das {nota_n} é {nota}")'''
'''#Questao 13
ano = 1995
while True:
        ano_atual = input("Digite um ano a partir de 1995: ")
        if ano_atual.isnumeric():
            ano_atual = int(ano_atual)
            if ano_atual >= 1995:
                break
            else:
                print("Valor errado. Digite novamente")
        else:
            print("Valor errado. Digite novamente")
salario = 1000
salario_atual = 0
aumento = 0.015
while ano <= ano_atual:
    ano += 1
    salario += salario * aumento
    aumento = aumento * 2
print(f"{salario:.2f}")'''

'''Questao 14
num_numeros = 0
while True:
    num_numeros = input("Quantos numeros quer ?")
    if num_numeros.isnumeric():
        num_numeros = int(num_numeros)
        break
    else:
        print("Valor errado. Digite novamente")
num = 0
i = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
while i < num_numeros:
    i += 1
    while True:
        num = input("Digite um numero: ")
        if num.isnumeric():
            num = int(num)
            break
        else:
            print("Valor errado. Digite novamente")
    if num < 0:
        print("Numero negativo não entra")
        break
    if num > 0 and num <=25:
        c1 += 1
    elif num > 25 and num <=50:
        c2 += 1
    elif num > 50 and num <=75:
        c3 += 1
    elif num > 75 and num <=100:
        c4 += 1
    else: 
        print("Esse numero nao entra em nenhuma caixa")
print(f"Tem {c1} numeros na caixa 1")
print(f"Tem {c2} numeros na caixa 2")
print(f"Tem {c3} numeros na caixa 3")
print(f"Tem {c4} numeros na caixa 4")'''


'''Aula For
for char in 'arroz':
    print(char)

for i in range(0,10,2): #start,end, step
    print(i)
for i in range(10,0,-2): #start,end, step
    print(i)
    
senha_cadastrada  = '1234'
senha = input("Diga sua senha: ")
tentativas = 1
while senha != senha_cadastrada and tentativas < 3:
    print("Voce errou!!")
    senha = input("Diga sua senha: ")
    tentativas += 1
if senha == senha_cadastrada:
    print("Acesso Liberado")
else:
    print("Sai hacker")
i = 0
for i in range(3):
    senha = input("Diga sua senha: ")
    if senha == senha_cadastrada:
        print("Acesso Liberado")
        break
    else:
        print("Voce errou!!")
if senha != senha_cadastrada:
    print("Sai hacker")
par = 0
num = 0
impar = 0
for i in range(10):
    num = int(input("Me diga um numero: "))
    if not num % 2:
        par += 1
impar =  10 - par
print(f"Voce digitou {par} pares e {impar} impares.")

num = 0
num_soma = 0
for i in range(1,11):
    num = int(input("Me diga um numero: "))
    num_soma += num
num_media = num_soma / 10
print(f"A soma desses numeros é {num_soma} e a media é {num_media}")
num_soma = 0
for i in range(101):
    num_soma += i
print(num_soma)

for i in range(1, 11):
    print(f"Tabuada do {i}")
    for j in range(1, 11):
        print(f"{i} X {j} = {i * j}")
    print()'''

# anoAtual = 2024
# idade = 0
# def calcIdade(anoNasc):
#     idade = anoAtual -anoNasc
#     return idade
# a = calcIdade(int(input("Diga seu ano de nascedura: \n ->")))
# print(a)
# lista = [-50,35,90,7,68,170,45,7,88]
# def maiorElemento():
#     maior = lista[0]
#     for numero in lista:
#         if numero > maior:
#             maior = numero
#     return maior
# print(maiorElemento())

# def tempoMaisUm(hora,minuto):
#     minuto += 1
#     if minuto >= 60:
#         hora += 1
#         minuto = 0
#     if hora >= 23:
#         hora = 0
#     hora = str(hora)
#     minuto = str(minuto)
#     if len(hora) == 1:
#         hora = (f"0{hora}")
#     if len(minuto) == 1:
#         minuto = (f"0{minuto}")
#     return f"{hora}:{minuto}"
# minutos =  int(input("Me diga quantos minutos quer pular:\n->"))
# for i in range(minutos):
#     print(tempoMaisUm(0,i))
# def eNumerico(num):
#     while not num.isnumeric():
#         print(f"O {num} não é um numero")
#         num = input("Tente novamente:\n->")
#     return num
# def verificarNumero(numeroCelular):
#     eNumerico(numeroCelular)
#     carac = len(numeroCelular)
#     if carac == 11 or carac == 9 or carac == 8:
#         return True
#     else:
#         return False
# print(verificarNumero("111"))
# print(verificarNumero("112132"))
# print(verificarNumero("11982765532"))

# def verificarCarro(carros = [], carroEscolhido = ""):
#     while True:
#         for carro in carros:
#             if carro == carroEscolhido:
#                 return True
#         carroEscolhido = input("Carro não está nessa lista\n->")
# print(verificarCarro(["Corsa" , "Palio", "Corola"], "Corola"))
# print(verificarCarro(["Corsa" , "Palio", "Corola"], "Palio"))
            
# def tem_numero_impar(lista):
#     for num in lista:
#         if num % 2 == 1:
#             return True
#     return False

# a = tem_numero_impar([12,3,10])

carros = ["Corsa" , "Palio", "Corola"]
precos = [150000 , 50000, 30000]

def carroMaisCaro():
    maiorPreco = 0
    for preco in precos:
        
