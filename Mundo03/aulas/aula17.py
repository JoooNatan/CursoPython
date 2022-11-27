num = [2, 5, 9 ,1]#lista sao mutaveis
num[2] = 7

num.append(4)#adiciona um valor no final da lista
print(num)

num.insert(2, 8)#adiciona um valor com base no indice .insert(indice, valor)
print(num)

num.sort()#ordena a lista em ordem cresente
print(num)

num.sort(reverse = True)#ordena a lista em ordem decresente
print(num)

num.pop(2)#remove um valor .pop(indice)
print(num)

num.remove(2)#remove um valor na sua primeira ocorencia .remove(valor a ser removido)
print(num)

if 4 in num:
    num.remove(4)
else:
    print('Valor 4 nao encontrado')

print(f'Essa lista tem {len(num)} elementos.')#retorna a quantidade de elementos

for valor in num:
    print(f'{valor} ')

for c, v in enumerate(num):#(c = indice, v = valor do determinado indice)
    print(f'Na posicao {c} tem o valor {v}')

valores = []
for cont in range(0, 4):
    valores.append(int(input('Digite um valor: ')))

print(valores)

valores2 = valores[:]#cria uma copia de 'valores'
valores2[2] = 9

print(valores2)
