jogador = {}
time = []
gols = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    nPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0, nPartidas):
        gols.append(int(input(f'  Quantos gols na partida {c + 1}? ')))
        
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()

    while True:
        op = str(input('Quer continuar?[S/N] ')).upper()[0]
        if op in 'SN':
            break
        print('Responda apenas S ou N.')
    if op == 'N':
        break
print('=' * 42)

print('cod nome             gols            total')
print('-' * 42)
for i, j in enumerate(time):
    print(f'{i:>3}', end = '')
    print(f' {str(j["nome"]):<17}', end = '')
    print(f'{str(j["gols"]):<16}', end = '')
    print(f'{str(j["total"]):<5}')
print('-' * 42)

while True:
    jog = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if jog == 999:
        break
    if jog >= len(time):
        print(f'Codigo {jog} nao encontrado.')
    else:
        print(f'Levantamento do {time[jog]["nome"]}')
        for i, g in enumerate(time[jog]["gols"]):
            print(f'    No jogo {i + 1} fez {g} gols')
    print('-' * 49)
