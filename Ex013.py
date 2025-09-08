def numeros_vizinhos(numero):
    return numero - 1, numero + 1

numero = int(input("Digite um número: "))
menor, maior = numeros_vizinhos(numero)
print(f"O número anterior é {menor} e o próximo número é {maior}.")
