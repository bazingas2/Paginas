import math

def Calculos(numero):
    return numero * 2, numero * 3, math.sqrt(numero)

numero = int(input("Digite um número: "))
dobro, triplo, raiz_quadrada = Calculos(numero)
print(f"O Dobro é {dobro}, o Triplo é {triplo}, e a Raiz Quadrada é {raiz_quadrada:.2f}.")
