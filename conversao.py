num = int(input("Digite o numero a ser convertido : \n "))
base = int(input('''Escolha a base da conversão :
Para binario digite 1 
Para octal digite 2
Para hexadecimal digite 3
Sua escolha : \n '''))
if base == 1:
    print("Conversão para binário")
    print("{} convertido para binário é: {}.".format(num, bin(num)[2:]))
elif base == 2:
    print("Conversão para octal")
    print("{} convertido para octal é: {}.".format(num, oct(num)[2:]))
elif base == 3:
    print("Conversão para hexadecimal")
    print("{} convertido para hexadecimal é: {}.".format(num, hex(num)[2:]))
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
