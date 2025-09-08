print("*****************************")
print("Bem vindo ao jogo do Macaco")
print("*****************************")

numero_secreto = 40
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute = int(input("Digite seu número: "))
    print("Você digitou", chute)

    if (numero_secreto == chute):
        print("Você acertou!")
    else:
        if (chute > numero_secreto):
            print("Você errou! Seu número foi maior que o número secreto.")
        else:
            print("Você errou! Seu número foi menor que o número secreto.")

    rodada = rodada + 1

print("Fim do Jogo")
