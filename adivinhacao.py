print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

print("Você digitou", chute_str)

chute = int(chute_str)

acertou = numero_secreto == chute
maior = numero_secreto < chute
menor = numero_secreto > chute

if(acertou):
    print("Acertou!")
else:
    if(maior):
        print("Errou! O seu chute foi maior que o número secreto.")
    elif(menor):
        print("Errou! O seu chute foi menor que o número secreto.")

print("fim do jogo")
