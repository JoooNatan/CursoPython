def maior(*n):
    tam = len(n)
    print(f'Foram informado {tam} valores.')
    for c in range(0, tam):
        print(n[c], end = ' ')
        if c == 0:
            maior = n[0]
        else:
            if n[c] > maior:
                maior = n[c]
    print(f'\nO maior valor foi {maior}')
    print('-' * 35)
    

maior(4, 2, 3)
maior(6, 2, 9, 12, 0, 1)
maior(1)
