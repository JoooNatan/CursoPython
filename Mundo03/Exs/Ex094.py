pessoa = {}
pessoas = []
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())

    while True:
        op = str(input('Quer continuar?[S/N] ')).upper()[0]
        if op in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if op == 'N':
        break

media = soma / len(pessoas)
print(f'A) Ao todo temos {len(pessoas)} cadastradas')
print(f'B) A media das é {media:.1f}anos.')
print(f'C) As mulheres cadastradas foram ', end = '')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}, ', end = '')
print()
print(f'D) Lista das pessoas que estão acima da media: ')
for p in pessoas:
    if p['idade'] >= media:
        print('    ', end = '')
        for k, v in p.items():
            print(f'{k} = {v}; ', end = '')
        print()
