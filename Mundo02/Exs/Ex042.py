print('-' * 25)
print('Analizador de triangulo')
print('-' * 25)
r1 = float(input('Digite o segmento da 1° reta: '))
r2 = float(input('Digite o segmento da 2° reta: '))
r3 = float(input('Digite o segmento da 3° reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um \033[1;32mTRIANGULO \033[m', end = '')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 or r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os segmentos acima \033[1;31mNÃO podem formar um TRIANGULO!!!\033[m')