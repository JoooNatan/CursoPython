primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
tot = 0
mais = 10

while mais != 0:
    tot = tot + mais
    while cont <= tot:
        print('{} -> '.format(termo), end = '')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(tot))
