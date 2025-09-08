s = 0  # Inicializa a variável para armazenar a soma dos números pares

# Executa 6 iterações, pedindo números ao usuário
for i in range(6):
    num = int(input("Digite um número: \n"))  # Solicita um número inteiro ao usuário
    if num % 2 == 0:  # Se o número for par
        s += num  # Soma o número par à variável `s`

# Exibe a soma total dos números pares digitados
print("Soma dos números pares: {}.".format(s))
