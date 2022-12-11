nums = [[], []]

for c in range(1, 8):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)

print('-' * 30)
nums[0].sort()
nums[1].sort()
print(f'Os valores pares digitados foram {nums[0]}')
print(f'Os valores impares digitados foram {nums[1]}')
