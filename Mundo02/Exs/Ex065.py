op = 'S'
soma = maior = menor = cont = 0

while op == 'S':
    num = int(input('Digite um numero: '))
    op = str(input('Quer Continuar?[S/N] ')).upper()
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

media = soma / cont
print('Foram digitados {} numeros, a media deles é: {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
