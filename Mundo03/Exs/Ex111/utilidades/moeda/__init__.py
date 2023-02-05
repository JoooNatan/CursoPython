def aumentar(preco = 0, taxa = 0, format = False):
    res = preco + (preco * (taxa / 100))
    return res if format is False else fmoeda(res)


def diminuir(preco = 0, taxa = 0, format = False):
    res = preco - (preco * (taxa / 100))
    return res if format is False else fmoeda(res) 


def dobro(preco = 0, format = False):
    res = preco * 2
    return res if format is False else fmoeda(res)


def metade(preco = 0, format = False):
    res = preco / 2
    return res if format is False else fmoeda(res)


def fmoeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco = 0, taxaA = 10, taxaR = 5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preco analisado: \t{fmoeda(preco)}')#\t > Tabulacao
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'{taxaA}% de aumento: \t{aumentar(preco, taxaA, True)}')
    print(f'{taxaR}% de reducao: \t{diminuir(preco, taxaR, True)}')
    print('-' * 35)
