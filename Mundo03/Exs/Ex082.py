nums = []
numsPar = []
numsImpar = []

while True:
    nums.append(int(input('Digite um numero: ')))
    op = str(input('Quer Continuar?[S/N] '))
    if op in 'Nn':
        break

for i, v in enumerate(nums):
    if v % 2 == 0:
        numsPar.append(v)
    else:
        numsImpar.append(v)

print(f'A lista completa é: {nums}')
print(f'A lista de pares é: {numsPar}')
print(f'A lista de impares é: {numsImpar}')
