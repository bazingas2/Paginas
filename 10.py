n = int(input('Digite um número inteiro: '))
print('Tipo:', type(n))

m = float(input('Digite um número decimal: '))
print('Tipo:', type(m))

# Conversão explícita para booleano com tradução
o = input('Digite algo (Verdadeiro/Falso): ').strip().lower()
o = o == 'verdadeiro'
print('Tipo:', type(o))

p = input('Digite algo (Verdadeiro/Falso): ').strip().lower()
p = p == 'verdadeiro'
print('Tipo:', type(p))

q = input('Digite uma cadeia de caracteres (texto): ')
print('Tipo:', type(q))
