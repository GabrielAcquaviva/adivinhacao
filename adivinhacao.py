import random

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1,21)
    tentativas = 0
    pontos = 100

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Escolha o nível: "))

    if(nivel == 1):
        tentativas = 10

    elif(nivel == 2):
        tentativas = 5

    else:
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
            print("Acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Errou! O seu chute foi maior que o número secreto.")
            elif(menor):
                print("Errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("fim do jogo")


if(__name__ == "__main__"):
    jogar()
