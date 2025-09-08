def situacao(preco1):
    if preco1 >= 100:
        return "Caro"
    else:
        return "Barato"

preco1 = float(input("Digite o primeiro preço: "))
resultado = situacao(preco1)
print(f"O preço está {resultado}.")
