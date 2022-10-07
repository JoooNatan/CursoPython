from math import sin, cos, tan, radians
ang = float(input('Digite um angulo: '))
seno = sin(radians(ang))
cose = cos(radians(ang))
tang = tan(radians(ang))
print('Seno: {:.2f}'.format(seno))
print('Cosseno: {:.2f}'.format(cose))
print('Tangente: {:.2f}'.format(tang))
