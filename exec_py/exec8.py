import random

numero = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input("Adivinhe o número: "))
    tentativas += 1

    if chute == numero:
        print("Acertou em", tentativas, "tentativas!")
        break
    elif chute < numero:
        print("Maior!")
    else:
        print("Menor!")