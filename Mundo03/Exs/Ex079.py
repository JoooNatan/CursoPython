num = list()

while True:
    n = int(input('Digite um numero '))
    if n not in num:
        num.append(n)
    else:
        print('Valor ja adicionado...')
    r = str(input('Quer Continuar?[S/N] '))
    if r in 'Nn':
        break

num.sort()
print(f'Valores digitados: {num}')
