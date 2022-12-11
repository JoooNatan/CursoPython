dados = []
pessoas = []
maior = []
menor = []
maiorpes = menorpes = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maiorpes = menorpes = dados[1]
    else:
        if dados[1] > maiorpes:
            maiorpes = dados[1]
        if dados[1] < menorpes:
            menorpes = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    op = str(input('Quer Continuar?[S/N] '))
    if op in 'Nn':
        break

print('-' * 30)
print(f'Os dados foram: {pessoas}')
print(f'Foram cadastradas {len(pessoas)} pessoas.')

print(f'O maior peso foi {maiorpes}kg de ', end = '')
for p in pessoas:
    if p[1] == maiorpes:
        print(f'[{p[0]}] ', end = '')
print()

print(f'O menor peso foi {menorpes}kg de ', end = '')
for p in pessoas:
    if p[1] == menorpes:
        print(f'[{p[0]}] ', end = '')
