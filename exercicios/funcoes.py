def soma_valores(v1, v2):
    return v1 + v2

while True:
    valor1 = int(input('Digite o valor 1: '))
    valor2 = int(input('Digite o valor 2: '))

    print(f'A soma de {valor1} + {valor2} = {soma_valores(valor1, valor2)}')