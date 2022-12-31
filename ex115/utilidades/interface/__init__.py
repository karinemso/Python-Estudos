import json
from utilidades import dado
from utilidades import arquivo




def linha(tam = 42):
    return print('-'*tam)

def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()
def menu():
    cabecalho("Menu de Cadastros")
    ops =("1- Ver pessoas cadastradas","2- Cadastrar novas pessoas",
     " 3- Sair do sistema")
    for c,o in enumerate(ops):
        if c == 2:
            print(o.center(34))
        else:
            print(o.center(42))

def show(arq):
    while True:
        menu()
        op = dado.leiaInt('Digite sua opção: ')
        if op == 1:
           arquivo.verArquivo(arq)
        if op == 2:
            cabecalho('Faça o cadastro')
            nome = dado.leiaNome('Digite um nome: ')
            idade = dado.leiaInt('Digite uma idade: ')
            arquivo.cadastra(nome,idade,arq)
        if op == 3:
            break
        
