velo = float(input('Digite a velocidade do seu carro '))
if velo > 80:
    print('Voce passou do limite de velocidade de 80km/h e foi multado em R${:.2f}' .format((velo - 80) * 7))
else:
    print('Parabens voce esta dentro da velocidade da via!')