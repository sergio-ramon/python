# Importa o Path da biblioteca pathlib para verificar 
# se o arquivo já existe no local selecionado
from pathlib import Path

nome = str(input("Digite o nome do arquivo: "))
disciplinas = ("Português", "Matemática", "História", "Geografia",
               "Filosofia", "Ed. Física", "Química", "Física")

caminho = "\\Users\\Nelmac\\Documents\\estudos\\exercicio_for\\"
arquivo_txt = Path(f"{caminho}{nome.lower()}.txt")

def editar():
    notas = []
    for i in range(len(disciplinas)):
        valor = float(input(f"Digite a nota de {disciplinas[i]}: "))

        while valor < 0 or valor > 10:
            valor = float(input(f"Digite uma nota válida para {disciplinas[i]}: "))
        notas.append(valor)

    # Abre o arquivo .txt------------------------------
    arquivo = open(f"{caminho}{nome.lower()}.txt", "w")
    # Edita os valores no arquivo----------------------
    for i in range(len(notas)):
        arquivo.write(f"{disciplinas[i]}: {notas[i]}\n")
    # Fecha o arquivo----------------------------------
    arquivo.close()

if arquivo_txt.exists():
    escolha = int(0)
    while escolha != 1 or escolha != 2:
        escolha = int(input("Você deseja: [1] Ler o arquivo; [2] Sobescrever o arquivo? "))
        if escolha == 1 or escolha == 2:
            break
    
    if escolha == 1:
        # Abre o arquivo .txt para leitura-----------------
        arquivo = open(f"{caminho}{nome.lower()}.txt", "r")
        # Exibe as informações do arquivo------------------
        print(arquivo.read())
        arquivo.close()
    elif escolha == 2:
        editar()
else:
    editar()