tot = totMil = menorPreco = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco: '))
    cont += 1
    tot += preco

    if preco > 1000:
        totMil += 1

    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        barato = produto

    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if res == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi {tot:.2f}')
print(f'{totMil} produtos custam mais de R$1000')
print(f'O produto mais barato foi {barato} e custou R${menorPreco:.2f}')
