dia = int(input('Digite quantos dias foi alugado: '))
km = float(input('Quantos km rodados? '))
print('Total a pagar: R${:.2f}'.format((dia * 60) + (km * 0.15)))