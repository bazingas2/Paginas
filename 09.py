num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else 'Indefinido (divisão por zero)'

print('A soma entre {} e {} é igual a {}'.format(num1, num2, soma))
print(f'A subtração entre {num1} e {num2} é igual a {subtracao}')
print(f'A multiplicação entre {num1} e {num2} é igual a {multiplicacao}')
print(f'A divisão entre {num1} e {num2} é igual a {divisao}')
