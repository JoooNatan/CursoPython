s = c = 0

while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    else:
        s += n
        c += 1

print(f'Foram digitados {c} numeros e a soma deles é {s}')
