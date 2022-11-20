from random import randint
nums = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print('Numeros sorteados: ', end = '')
for n in nums:
    print(f'{n} ', end = '')

print(f'\nMaior valor: {max(nums)}')
print(f'Menor valor: {min(nums)}')
