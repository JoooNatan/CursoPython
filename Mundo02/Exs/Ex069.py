op = ' '
pessoa18mais = homens = mulher20menos = 0
while True:
    if 'N' in op:
        break
    else:
        print('-' * 30)
        print('{:-^30}'.format(' Cadastre uma Pessoa '))
        print('-' * 30)
        idade = int(input('Digite a idade: '))
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('Digite o sexo:[M/F] ')).strip().upper()[0]

        if idade >= 18:
            pessoa18mais += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulher20menos += 1
            
        op = ' '
        while op not in 'SN':
            op = str(input('Quer Continuar?[S/N] ')).strip().upper()[0]

print(f'{pessoa18mais} pessoas tem mais de 18 anos')
print(f'{homens} homens foram cadastrados')
print(f'{mulher20menos} mulheres tem menos de 20 anos')
