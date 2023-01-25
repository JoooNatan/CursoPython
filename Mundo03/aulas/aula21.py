#----------------------------------------ESCOPO----------------------------------------
def teste(b):
    global a#Usa a variavel glogal, desse jeito ele pode ser alterada no escopo global
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')
#--------------------------------------------------------------------------------------


#------------------------------------------EX------------------------------------------
def fatorial(n = 1):
    f = 1
    for c in range(n, 0, -1):
        f = f * c
    return f


num = int(input('Digite um numero: '))
print(f'O fatorial de {num} é {fatorial(num)}')

def par(n):
    if n % 2 == 0:
        return True
    else:
        return False
    

print(par(3))
#--------------------------------------------------------------------------------------


