from datetime import date

atual = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    idade = atual - ano
    if idade <= 21:
        menor += 1
    else:
        maior += 1

print('Ao todo tivemos {} pessoa maiores de idade'.format(maior))
print('E tambem tivemos {} pessoa menores de idade'.format(menor))
