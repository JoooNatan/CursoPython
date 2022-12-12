matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor da posicao [{l}, {c}] '))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        if c == 2:
            scol += matriz[l][c]
        if l == 1:
            if c == 0 or matriz[l][c] > maior:
                maior = matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end = '')
    print()

print(f'Soma de todos valores pares: {spar}')
print(f'Soma de todos valores da terceira coluna: {scol}')
print(f'Maior valor da segunda linha: {maior}')
