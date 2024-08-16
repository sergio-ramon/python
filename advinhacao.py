from random import randrange

numero = randrange(0, 100)
print("Descubra o número escondido (De 0 a 100)")
chute = int(input("Digite um número: "))

while chute != numero:
    if chute < numero:
        chute = int(input("Digite um valor maior: "))
    elif chute > numero:
        chute = int(input("Digite um valor menor: "))

print("Acertou!")