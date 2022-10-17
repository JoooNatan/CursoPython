n1 = int(input('Digite o 1° numero '))
n2 = int(input('Digite o 2° numero '))
n3 = int(input('Digite o 3° numero '))
maior = int(0)
menor = int(0)
if n1 > n2 and n1 > n3:
    maior = n1
    if n2 < n3:
        menor = n2
    else:
        menor = n3
else:
    if n1 < n2 and n1 < n3:
        menor = n1
    if n2 > n3:
        maior = n2
    else:
        maior = n3

print('O maior numero foi: {}'.format(maior))
print('O menor numero foi: {}'.format(menor))