print("*****************************")
print("Bem vindo ao jogo do Macaco")
print("*****************************")

numero_secreto = 40
input("Digite o valor da aposta: ")
chute = int(input("Digite seu número: "))

print("Você digitou", chute)

if chute == numero_secreto:
    print("Você acertou!")
else:
    if chute > numero_secreto:
        print("Você errou! Seu número foi maior que o número secreto.")
    else:
        print("Você errou! Seu número foi menor que o número secreto.")

print("Fim do Jogo")
