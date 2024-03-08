'''
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
    print("-------------------------------")

'''

valor_1 = int(input("Escreva um valor: "))
valor_2 = int(input("Escreva um valor: "))
valor_3 = int(input("Escreva um valor: "))

if valor_1 - valor_2 < 0:
    guardar = valor_1
    valor_1 = valor_2
    valor_1 = guardar
if valor_2 - valor_3 < 0:
    guardar = valor_2
    valor_2 = valor_3
    valor_2 = guardar
print(valor_1)
print(valor_2)
print(valor_3)



