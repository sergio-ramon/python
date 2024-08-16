from random import randint

nomes_npcs = (
    'Peng', 'Bang-bang', 'Deminan', 'Puc-puc', 'Wolf',
    'Iena', 'Fly', 'Dragon baby', 'Pang'
)

lista_npcs = []

player = {
    'nome': 'Meliodas',
    'nivel': 1,
    'exp': 0,
    'exp_max': 50,
    'vida': 300,
    'vida_max': 300,
    'dano': 25
}

# Cria um npc
def cria_npc(nivel1, nivel2):
    nivel = randint(nivel1, nivel2)
    vida_base = 100
    dano_base = 5
    exp_base = 7

    npc = {
        'nome': f'{nomes_npcs[randint(0, len(nomes_npcs) - 1)]} #{nivel}',
        'nivel': nivel,
        'vida': vida_base * nivel,
        'vida_max': vida_base * nivel,
        'dano': dano_base * nivel,
        'exp': exp_base * nivel
    }

    return npc

# Gera vários npcs no local
def gera_npcs(quantidade, niveis1, niveis2):
    for i in range(quantidade):
        lista_npcs.append(cria_npc(niveis1, niveis2))

# Escolhe um dos npcs da lista de forma aleatória
def seleciona_npc(escolha):
    npc_escolhido = lista_npcs[escolha - 1]
    return npc_escolhido

# Player desfere um ataque no npc selecionado caso esteja vivo
def ataque_player(npc):
    if player['vida'] > 0:
        print('Player ataca o NPC: ')
        npc['vida'] -= player['dano']
        print(f'{npc['nome']} - {npc['vida']}/{npc['vida_max']}')

# npc selecionado desfere um ataque no player caso esteja vivo
def ataque_npc(npc):
    if npc['vida'] > 0:
        print('NPC ataca o player: ')
        player['vida'] -= npc['dano']
        print(f'{player['nome']} - {player['vida']}/{player['vida_max']}')

# Ações para fim de batalha (Mensagem de vitória/derrota e ganho de status)
def fim_batalha(ultimo_npc_escolhido):
    if player['vida'] > 0 and ultimo_npc_escolhido['vida'] == 0:
        print('-' * 5 + 'Batalha vencida!' + '-' * 5)
        player['exp'] += ultimo_npc_escolhido['exp']
        print(f'Recebeu {ultimo_npc_escolhido['exp']} Exp')
        lista_npcs.remove(ultimo_npc_escolhido)
    elif player['vida'] > 0 and ultimo_npc_escolhido['vida'] > 0:
        print('Fugiu!')
    else:
        print('Fim de jogo!')

# Controlador de batalha
def batalha(npc_batalha):
    print(f'{npc_batalha['nome']} #{npc_batalha['nivel']} - '
          f'{npc_batalha['vida']}/{npc_batalha['vida_max']}')
    while True:
        opcao = input('Atacar npc?(s/n) ')
        if opcao.upper() == 'S':
            ataque_player(npc_batalha)
            ataque_npc(npc_batalha)
        elif opcao.upper() == 'N':
            break
        if npc_batalha['vida'] == 0 or player['vida'] == 0:
            break

    fim_batalha(npc_batalha)

gera_npcs(5, 1, 5)

while len(lista_npcs) > 0:
    for x in lista_npcs:
        print(f'{x['nome']} - {x['vida']}/{x['vida_max']}')
    selecionado = int(input('Escolha um npc da lista: '))
    while selecionado >= len(lista_npcs) + 1:
        selecionado = int(input('Escolha um npc da lista: '))

    batalha(seleciona_npc(selecionado))