n50 = n20 = n10 = n1 = 0
print('-' * 45)
print('{:^45}'.format(' Banco NJ '))
print('-' * 45)
valor = int(input('Qual valor voce quer sacar? '))

while True:
    if valor == 0:
        break
    else:
        if valor >= 50:
            n50 += 1
            valor -= 50
        elif valor >= 20:
            n20 += 1
            valor -= 20
        elif valor >= 10:
            n10 += 1
            valor -= 10
        elif valor >= 1:
            n1 += 1
            valor -= 1

print(f'Total de cedulas de R$50: {n50}')
print(f'Total de cedulas de R$20: {n20}')
print(f'Total de cedulas de R$10: {n10}')
print(f'Total de cedulas de R$1:  {n1}')
