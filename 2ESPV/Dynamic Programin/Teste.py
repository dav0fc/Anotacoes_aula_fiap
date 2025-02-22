n_maior = 300
n_menor = 0
numero = 69

def busca_binaria(resp, maior, menor):
    i = 0
    meio = 0
    while True:
        print(i)
        i +=1
        if meio == resp:
            return i, meio
        elif meio > maior:
            meio = (maior - menor) / 2
            print(meio)

print(busca_binaria(numero,n_menor,n_maior))