expr = str(input('Digite a expressão: '))
pilha = []

for simb in expr:
    if simb in '(':
        pilha.append('(')
    elif simb in ')':
        if len(pilha) > 0:
            pilha.pop()#remove o ultimo elemento de uma lista
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão não está valida!')
