salario = float(input('Digite o salario do funcionario '))
if salario > 1250:
    print('O funcionario recebeu um aumento de \033[32m10%\033[m e seu novo salario é de R${:.2f}'.format((salario * 0.10) + salario))
else:
    print('O funcionario recebeu um aumento de \033[32m15%\033[m e seu novo salario é de R${:.2f}'.format((salario * 0.15) + salario))