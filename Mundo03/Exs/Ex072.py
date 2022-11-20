nums = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

op = 'S'
while True:
    if op == 'S':
        n = int(input('Digite um numero entre 0 e 20: '))
        if n > 20 or n < 0:
            print('Tente novamente. ', end = '')
        else:
            print(f'Voce digitou o numero {nums[n]}')
            op = str(input('Quer Continuar?[S/N] ')).strip().upper()[0]
    else:
        break
