print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

print("Você digitou", chute_str)

chute = int(chute_str)

if(chute == numero_secreto):
    print("Acertou, miseravi!")
else:
    print("Errou!")

print("fim do jogo")
