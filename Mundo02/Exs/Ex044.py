print('{:=^35}'.format(' LOJAS NJ '))
preco = float(input('Digite o preço da compra R$'))
print('''[1] Avista/Cheque
[2] Avista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')

op = int(input('Qual a opção? '))
print('{:=^35}'.format(''))
if op > 0 and op < 5:
    if op == 1:
        total = preco - (preco * 0.10)
    elif op == 2:
        total = preco - (preco * 0.05)
    elif op == 3:
        total = preco
        parcela = total / 2
        print('Sua compra sera parcelada em 2x de R$ {:.2f}'.format(parcela))
    elif op == 4:
        total = preco + (preco * 0.20)
        totparcela = int(input('Quantas parcelas? '))
        parcela = total / totparcela
        print('Sua compra sera parcelada em {}x de R$ {:.2f} COM JUROS DE 20%'.format(totparcela, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
else:
    print('\033[31mOpção invalida\033[m')
