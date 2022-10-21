peso = float(input('Digite o peso(kg) '))
altura = float(input('Diguite a altura(m) '))
imc = peso / (altura ** 2)
print('IMC: {:.2f}'.format(imc))
print('Situação: ', end = '')
if imc < 18.5:
    print('abaixo do peso')
elif imc < 25:
    print('peso ideal')
elif imc < 30:
    print('sobrepeso')
elif imc < 40:
    print('obesidade')
else:
    print('obesidade morbida')