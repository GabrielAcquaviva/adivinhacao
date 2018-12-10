import random

print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = random.randrange(1,21)
tentativas = 3

for rodada in range(1, tentativas + 1):
    print("Tentativa {} de {}".format(rodada, tentativas))
    chute_str = input("Digite o seu número entre 1 e 20: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 20):
        print("Você deve digitar um número entre 1 e 20!")
        continue

    acertou = numero_secreto == chute
    maior = numero_secreto < chute
    menor = numero_secreto > chute

    if(acertou):
        print("Acertou!")
        break
    else:
        if(maior):
            print("Errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Errou! O seu chute foi menor que o número secreto.")

print("fim do jogo")
