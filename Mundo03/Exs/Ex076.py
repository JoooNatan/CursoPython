listagem = ('Lapis', 1.75,
'borracha', 2,
'caderno', 15.90,
'estojo', 7.50,
'mochila', 80.30,
'caneta', 2.15)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    else:
        print(f'R${listagem[pos]:>6.2f}')
