from lib.interface import *
from time import sleep

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        cabecalho('Opcao 1')
    elif resp == 2:
        cabecalho('Opcao 2')
    elif resp == 3:
        cabecalho('Saindo do sistema.. Ate logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)

