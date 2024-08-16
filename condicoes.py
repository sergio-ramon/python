nota = float(input("Digite a nota: "))
media_alta = 7
media_baixa = 5

#-------------------------------------------
def verifica_nota():
    nota_p = float(input("Digite a nota da segunda prova: "))
    if nota_p >= media_baixa:
        print("Aprovado")
    else:
        print("Reprovado")

#-------------------------------------------
if nota >= media_alta:
    print("Aprovado")
elif nota >= media_baixa:
    print("Fazer prova final")
    verifica_nota()
else:
    print("Fazer recuperação final")
    verifica_nota()