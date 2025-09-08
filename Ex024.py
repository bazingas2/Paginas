S = str(input("Digite M ou F: \n")).strip().upper()[0]
while S not in "MmFf":
    S = str(input("Caro Asno. Digite M ou F: \n")).strip().upper()[0]
print(f"Sexo selecionado: {S}")
