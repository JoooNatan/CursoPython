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
    time.append(jogador.copy())#Cria uma copia do dict
    gols.clear()

    while True:
        op = str(input('Quer continuar?[S/N] ')).upper()[0]
        if op in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if op == 'N':
        break

print('-' * 34)
print('cod  nome         gols     total')
for i, v in enumerate(time):
    print(f'{i:>3}', end = '')
    for d in v.values():
        print(f'  {str(d):<13}', end = '')
    print()
print('-' * 34)

while True:
    busca = int(input('Mostrar dados de qual jogador?[999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não há jogador com codigo {busca}.')
    else:
        print(f'Levantamendo do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 47)
