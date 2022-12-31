from utilidades import interface
from utilidades import dado

def existeArquivo(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except:
        return False
    else:
        return True
    
def criaArquivo(arq):
    try:
        a = open(arq,'w+')
        a.close()
    except:
        print('Erro na criação do arquivo!')
    else:
        print('Arquivo criado com sucesso')

def verArquivo(arq):
    try:
        aberto = open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        interface.cabecalho('Pessoas cadastradas')
        for linha in aberto:
            dados = linha.replace('\n','').split(';')
            print(f'{dados[0]:<30}{dados[1]:3>} anos')

def cadastra(n,i,arq):
    while True:
        pessoa = {}
        pessoa['nome'] = n
        pessoa['idade'] = i
        a = open(arq,'at')
        a.write(f"{n};{i}\n")
        
        pessoa.clear()
        op = str(input('Quer continuar cadastrando?[S/N]')).upper()
        if op == 'S':
            n = dado.leiaNome('Digite um nome: ')
            i = dado.leiaInt('Digite uma idade: ')
        elif op ==  'N':
            break
        