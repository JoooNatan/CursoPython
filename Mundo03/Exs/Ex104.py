#------------------------------------------meu jeito------------------------------------------
def leiaInt(num):
    num = input(num)
    if num.isnumeric():
        return num
    else:
        while num.isnumeric() == False:
            print(f'\033[0;31mERRO! Digite um numero inteiro valido\033[m')
            num = input()
        return num
    

n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
#------------------------------------------meu jeito------------------------------------------

#-----------------------------------------jeito Guana-----------------------------------------
def leiaINt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO! Digite um numero inteiro valido\033[m')
        if ok:
            break
        return valor
    

nu = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {nu}')
#-----------------------------------------jeito Guana-----------------------------------------
