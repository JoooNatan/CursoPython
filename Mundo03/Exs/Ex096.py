def area(larg, comp):
    r = larg * comp
    print(f'A area de um terreno {l:.1f}x{c:.1f} é de {r}m²')

print('-' * 30)
print(f"{'Controle de Terrenos':^30}")
print('-' * 30)

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
