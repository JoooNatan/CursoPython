nums = []
maior = menor = 0

for cont in range(0, 5):
    nums.append(int(input(f'Digite o valor na posicao {cont}: ')))
    if cont == 0:
        maior = menor = nums[cont]
    else:
        if nums[cont] > maior:
            maior = nums[cont]
        elif nums[cont] < menor:
            menor = nums[cont]

print(f'Voce digitou os valores {nums}')
print(f'O maior valor foi {maior} na posicao: ', end = '')
for i, v in enumerate(nums):
    if v == maior:
        print(f'{i}.. ', end = '')

print()

print(f'O menor valor foi {menor} na posicao: ', end = '')
for i, v in enumerate(nums):
    if v == menor:
        print(f'{i}.. ', end = '')
