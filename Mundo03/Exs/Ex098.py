from time import sleep

def contador(i, f, p):
    if p == 0:
        p = 1
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    sleep(1.5)
    if i < f:
        while i <= f:
            print(i, end = ' ', flush = True)
            i += p
            sleep(0.2)
    else:
        while i >= f:
            print(i, end = ' ', flush = True)
            if p < 0:
                i += p
            else:
                i -= p
            sleep(0.2)
    print('FIM!')

print('-' * 30)
contador(1, 10, 1)
print('-' * 30)
contador(10, 0, 2)
print('-' * 30)

print('Faça uma contagem personalizada')
i = int(input('Inicio '))
f = int(input('Fim    '))
p = int(input('Passo  '))
print('-' * 30)
contador(i, f, p)
