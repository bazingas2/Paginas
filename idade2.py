idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if(idade > 18):
    print("Você é maior de idade.")

elif(idade < 12):
        print("Você é cricança.")
else:
    print("Você é um adolecente.")
