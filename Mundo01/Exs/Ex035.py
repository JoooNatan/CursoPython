print('-' * 25)
print('Analizador de triangulo')
print('-' * 25)
r1 = float(input('Digite o segmento da 1° reta: '))
r2 = float(input('Digite o segmento da 2° reta: '))
r3 = float(input('Digite o segmento da 3° reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um TRIANGULO!!!')
else:
    print('Os segmentos acima NÃO podem formar um TRIANGULO!!!')