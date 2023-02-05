import moeda

print('-' * 35)
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.fmoeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.fmoeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 15%, temos {moeda.diminuir(p, 15, True)}')
print('-' * 35)
