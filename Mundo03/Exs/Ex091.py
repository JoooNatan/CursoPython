from random import randint
from time import sleep
from operator import itemgetter

ranking = []
jogo = {'jogador1': randint(1, 6),
'jogador2': randint(1, 6),
'jogador3': randint(1, 6),
'jogador4': randint(1, 6)}

print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(0.5)

ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)#itemgetter = pega o valor
print('-' * 25)
print('==RANKING DOS JOGADORES==')
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}.')
