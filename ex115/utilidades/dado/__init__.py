def leiaDinheiro(msg):
    n = input(msg)
    while True:
        if n.isnumeric() == True:
            return float(n)
        elif n.count(',') == 1 or n.count('.') == 1 and n.isalpha() == False:
            if n.count(',') == 1:
                num = n.replace(',','.')
                return float(num)
            else:
                return float(n)
        else:
            print(f"\033[31mErro! '{n}' é um valor inválido!\033[m")
            n = input('Digite um valor válido: R$')
    
def leiaInt(n):
    n = input(n)
    while True:
        if n.isnumeric() == True:
            return int(n)
        else:
            print(f'\033[31mErro! Você digitou um valor inválido!\033[m')
            n = input('Digite um novo valor:')

def leiaFloat(n):
    n = input(n)
    while True:
        if n.isalpha() == False and n.count('.') == 1 or n.isnumeric() == True:
            return float(n)
        else:
            print(f'\033[31mErro! Você digitou um valor inválido!\033[m')
            n = input('Digite um novo valor:')

def leiaNome(n):
    n = input(n)
    while True:
        if n.isalpha() == True:
            return str(n)
        else:
            print(f'\033[31mErro! Você digitou um nome inválido!\033[m')
            n = input('Digite um novo nome:')