salario = float(input('Digite o salario do funcionario '))
if salario > 1250:
    print('O funcionario recebeu um aumento de 10% e seu novo salario é de R${:.2f}'.format((salario * 0.10) + salario))
else:
    print('O funcionario recebeu um aumento de 15% e seu novo salario é de R${:.2f}'.format((salario * 0.15) + salario))