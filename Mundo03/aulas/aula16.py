lanche = ('hamburger', 'suco', 'pizza', 'pudim')#tupla
#tuplas sao imutaveis

print(lanche[1:])#[inicio:fim:passo] indice

#for c in lanche:
#    print(c)

for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} na posicao {cont}')

print(sorted(lanche))#sorted > ordena a tupla

