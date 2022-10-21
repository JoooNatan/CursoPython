print('-=' * 20)
print('         Emprestimo bancario')
print('-=' * 20)

valorCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salario? R$'))
anos = int(input('Digite em quantos anos voce ira pagar: '))
prestacaoMensal = float(valorCasa / (anos * 12))

print('-' * 30)
print('Situaçao do emprestimo:')

if prestacaoMensal > (salario * 0.30):
    print('\033[31mNegado!\033[m')
else:
    print('\033[32mAprovado!\033[m')
print('Valor das prestacões mensais: R${:.2f}'.format(prestacaoMensal))