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


'''

letra = input("Digite uma letra: ")

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U' :
    print(" é uma vogal")
else :
    print(f"{letra} é uma consoante")




