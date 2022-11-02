media = 0
homemMaisVelho = 0
mulheresMenosDe20 = 0
nomeHomemMaisVelho = ''

for c in range(1, 5):
    print("--- {}° pessoa ---".format(c))
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Digite a idade da pessoa: '))
    sexo = int(input('Digite o sexo da pessoa (1-masculino/2-feminino): '))
    media = idade + media
    if sexo == 1:
        if idade > homemMaisVelho:
            homemMaisVelho = idade
            nomeHomemMaisVelho = nome
    else:
        if idade < 20:
            mulheresMenosDe20 += 1

media = media / 4

print('-' * 20)
print('Media das idades do grupo: {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(homemMaisVelho, nomeHomemMaisVelho))
print('Numero de mulheres que têm menos de 20 anos: {} '.format(mulheresMenosDe20))
