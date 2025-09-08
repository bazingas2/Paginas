
print("- À vista dinheiro/cheque: 10% de desconto")
print("- À vista no cartão: 5% de desconto")
print("- Em até 2x no cartão: preço normal")
print("- Em 3x ou mais no cartão: 20% de juros")


valor = float(input("Qual o preço do produto? \n"))

print("Selecione uma forma de pagamento:")
print('''
Digite 1: Para pagar à vista no dinheiro.
Digite 2: Para pagar à vista no cartão.
Digite 3: Em 2x no cartão.
Digite 4: Em 3x no cartão ou mais.
''')


forma = int(input("Selecione a forma de pagamento: \n"))

if forma == 1:  # 10% de desconto
    print("Você selecionou à vista no dinheiro.")
    desconto = valor * 0.10
    print(f"Valor à vista no dinheiro: R${valor - desconto:.2f}.")
elif forma == 2:  # 5% de desconto
    print("Você selecionou à vista no cartão.")
    desconto = valor * 0.05
    print(f"Valor à vista no cartão: R${valor - desconto:.2f}.")
elif forma == 3:  # Em até 2x no cartão: preço normal
    print("Você selecionou em 2x no cartão.")
    print(f"Pagamento em 2x de R${valor / 2:.2f}.")
elif forma == 4:  # Em até 3x ou mais: 20% de juros
    print("Você selecionou em 3x no cartão ou mais.")
    parcelas = int(input("Em quantas vezes você deseja parcelar? \n"))
    if parcelas >= 3:
        juros = valor * 0.20
        print(f"Pagamento, com juros de 20%, em {parcelas}x de R${(valor + juros) / parcelas:.2f}.")
    else:
        print("A quantidade mínima de parcelas é de 3x no cartão.")
else:
    print("Por favor, selecione uma alternativa válida. Tente novamente.")
