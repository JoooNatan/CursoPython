from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = "dados.txt"

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        #Opcao de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('Opcao 2')
    elif resp == 3:
        cabecalho('Saindo do sistema.. Ate logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)

