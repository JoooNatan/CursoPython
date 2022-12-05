op = 'S'
num = []
cont5 = 0

while True:
    if op in 'Nn':
        print(f'Foram digitados {len(num)} valores: {num}')
        num.sort(reverse = True)
        print(f'Lista de valores ordenada de forma decrescente: {num}')
        if 5 in num:#verifica se tem o valor 5 na lista
            print('O valor 5 foi encontrado na lista.')
        else:
            print('O valor 5 nao foi encontrado na lista')
        break
    else:
        num.append(int(input('Digite um numero: ')))
        op = str(input('Quer Continuar?[S/N] '))
