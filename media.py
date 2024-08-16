from statistics import mean, geometric_mean, harmonic_mean

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

# média simples
mediaA = mean([n1, n2])
# média geométrica
mediaG = geometric_mean([n1, n2])
# média harmônica
mediaH = harmonic_mean([n1, n2])

print("A média simples dos valores é: {}\nA média geométrica é: {}\nA média harmônica é: {}".format(mediaA, mediaG, mediaH))