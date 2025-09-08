def converter_unidades(numero):
    cm = numero * 100
    metros = numero
    km = numero / 1000

    print(f"{numero} metros equivalem a:")
    print(f"{cm} centímetros")
    print(f"{km} quilômetros")

numero = float(input("Digite o número em metros: "))
converter_unidades(numero)
