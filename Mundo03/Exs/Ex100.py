from random import randint
from time import sleep

def sort(list):
    print(f'Sorteando cinco valores da lista: ', end = '')
    for c in range(0, 5):
        n = randint(1, 10)
        list.append(n)
        print(f'{n} ', end = '', flush = True)
        sleep(.3)
    print('PRONTO!')


def somaPar(list):
    soma = 0
    for num in list:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valore pares de {list} temos {soma}')


nums = []
sort(nums)
somaPar(nums)
