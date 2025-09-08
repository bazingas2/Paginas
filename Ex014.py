def Multiplicação(numero):
    return numero * 2, numero * 3

numero = int(input("Digite um número: "))
menor, maior = Multiplicação(numero)
print(f"O Dobro  é {menor} e o Triplo é {maior}.")
