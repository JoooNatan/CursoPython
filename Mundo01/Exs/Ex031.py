dis = float(input('Digite a distancia da sua viagem '))
if dis <= 200:
    print('O preço da passagem sera de: R${}'.format(dis * 0.50))
else:
    print('O preço da passagem sera de: R${}'.format(dis * 0.45))

#if simplificado
#preco = dis * 0.50 if dis <= 200 else preco = dis * 0.45