soma = quant = num = 0

while num != 999:
    num = int(input('Digite um numero [999 para parar] '))
    if num == 999:
        print('Foram digitados {} numeros e a soma entre ele é igual a: {}'.format(quant, soma))
    else:
        quant += 1
        soma += num
