#Tuplas      ()
#Listas      []
#Dicionarios {}
pessoas = {'nome': 'Joao', 'idade': 20, 'sexo': 'M'}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

del pessoas['sexo']#elento sexo apagado
pessoas['peso'] = 95.5#adicionando o elemento(key) peso com o valor 95.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado = {}
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}#uf = key, Rio de janeiro = value
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}#sigla = key, SP = value
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

for c in range(0, 3):
    estado['uf'] = str(input('UF: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():#keys e values
        print(f'O campo {k} tem o valor {v}.')
