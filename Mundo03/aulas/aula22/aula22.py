from uteis import nums

num = int(input('Digite um numero: '))
fat = nums.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {nums.dobro(num)}')
print(f'O triplo de {num} é {nums.triplo(num)}')
