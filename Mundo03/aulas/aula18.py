print('-' * 30)
teste = []
teste.append('Joao')
teste.append(20)
print(teste)

galera = []
galera.append(teste[:])#cria uma copia da lista
print(galera)

teste[0] = 'Natan'
teste[1] = 30
galera.append(teste[:])
print(galera)
print('-' * 30)

galera2 = [['Joao', 20], ['Pedro', 27], ['Joaquim', 32], ['Maria', 45]]
for p in galera2:
    print(f'{p[0]}, {p[1]} anos.')
print('-' * 30)

galera3 = []
dado = []
totmaior = totmenor = 0

for c in range(0, 3):
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite a idade: ')))
    galera3.append(dado[:])
    dado.clear()
for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} nao é maior de idade')
        totmenor += 1
print(f'Temos {totmaior} pessoas maior de idade e {totmenor} menores.')
print('-' * 30)

