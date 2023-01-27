def notas(* n, sit = False):
    '''
    -> Função para notas e situacoes de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita carias).
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao.
    :return: dicionario com varias informacoes da turma.
    '''
    media = maior = menor = c = 0
    tot = len(n)
    for c in range(0, tot, 1):
        media += n[c]
        if c == 0:
            maior = n[c]
            menor = n[c]
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor = n[c]
    media /= tot
    
    list = {'total': tot, 'maior': maior, 'menor': menor, 'media': media}
    if sit:
        if media < 5:
            list['situacao'] = 'ruim'
        elif media < 7:
            list['situacao'] = 'razoavel'
        else:
            list['situacao'] = 'boa'
    return list


print(notas(4, 8, 7, 2.5))
print(notas(4, 8, 9, sit = True))
print(help)

'''def notas(* n, sit = False):
    //
    -> Função para notas e situacoes de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita carias).
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao.
    :return: dicionario com varias informacoes da turma.
    //
    dic = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': sum(n) / len(n)}
    if sit:
        if dic['media'] < 5:
            dic['situacao'] = 'ruim'
        elif dic['media'] < 7:
            dic['situacao'] = 'razoavel'
        else:
            dic['situacao'] = 'boa'
    return dic


print(notas(4, 8, 7, 2.5))
print(notas(4, 8, 9, sit = True))
print(help(notas))
'''
