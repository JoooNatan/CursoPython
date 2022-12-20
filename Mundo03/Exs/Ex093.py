jogador = {}
gols = []

jogador['nome'] = str(input('Nome: '))
nPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, nPartidas):
    gols.append(int(input(f'  Quantos gols na partida {c}? ')))
    
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('-=-' * 22)
print(jogador)
print('-=-' * 22)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 22)

print(f'O jogador {jogador["nome"]} jogou {nPartidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
