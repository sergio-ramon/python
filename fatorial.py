num1 = int(input("Digite um número inteiro positivo: "))
while num1 < 1:
    num1 = int(input("Digite um número inteiro positivo: "))

num2 = num1
while num2 > 1:
    num2 = num2 - 1
    num1 = num1 * num2

print(f"O fatorial do valor digitado é: {num1}")