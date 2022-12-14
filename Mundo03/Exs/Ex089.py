alunos = []

while True:
    nome = str(input('nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, nota1, nota2, media])
    op = str(input('Quer Continuar?[S/N] '))
    if op in 'Nn':
        break
    print('-' * 23)

print('-' * 23)
print('No.    NOME       MEDIA')
for i, a in enumerate(alunos):
    print(f'{i:<7}', end = '')
    print(f'{a[0]:<11}', end = '')
    print(f'{a[3]:>5.1f}')
print('-' * 23)

while True:
    nAluno = int(input('Mostrar notas de qual aluno?(999 interrompe) '))
    if nAluno == 999:
        break
    if nAluno >= len(alunos) or nAluno < 0:
        nAluno = int(input('Numero invalido! Digite novamente: '))

    print(f'Notas de {alunos[nAluno][0]} são {alunos[nAluno][1]} e {alunos[nAluno][2]}')
    print('-' * 46)
