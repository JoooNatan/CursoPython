from datetime import datetime

pessoa = {}
pessoa['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho(0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario: '))
pessoa['idade'] = datetime.now().year - ano
pessoa['aposentadoria'] = ((pessoa['contratacao'] + 35) - datetime.now().year) + pessoa['idade']
print('-' * 50)

for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')
