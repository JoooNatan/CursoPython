def mensagem(msg):#funcao
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)
mensagem('SISTEMA DE ALUNOS')


def soma(n1, n2):
    return print(f'{n1} + {n2} = {n1 + n2}')
soma(4,5)


def contador(* n):
    print(f'Recebi os valores {n} e o tamanho é {len(n)}')
contador(1, 2, 7)


valores = [6, 8, 9, 2, 1, 5]
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1
dobra(valores)
print(valores)
