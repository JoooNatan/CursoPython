'''
try:
    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))
    r = a / b

except:
    print('Erro!')

else:
    print(f'O resultado é: {r}')

finally:
    print('Obrigado! Volte sempre!')
'''

#------------------------------------------------------------------------------

try:
    a1 = int(input('Digite o primeiro valor: '))
    b1 = int(input('Digite o segundo valor: '))
    r1 = a1 / b1

except (ValueError, TypeError):
    print('Tivemos um problema com tipo de dados que voce digitou.')

except ZeroDivisionError:
    print('Erro! Nao é possivel dividir um numero por 0')

except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')

else:
    print(f'O resultado é: {r1}')

finally:
    print('Obrigado! Volte sempre!')
