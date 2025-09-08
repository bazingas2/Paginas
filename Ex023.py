s = 0  # Inicializa a variável para armazenar a soma

# Percorre os números de 1 a 500
for num in range(1, 501):
    if num % 2 != 0:  # Verifica se o número é ímpar
        if num % 3 == 0:  # Verifica se o número ímpar é múltiplo de 3
            s += num  # Adiciona o número à soma total

# Exibe o resultado final da soma dos ímpares múltiplos de 3
print("A soma dos múltiplos é: {}.".format(s))
