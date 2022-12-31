def leiaInt(n):
    n = input(n)
    while True:
        try:
            n=int(n)
        except:
            print(f'\033[31mErro! Valor "{n}" inválido!\033[m')
            n = input('Digite um novo valor:')
        else:
            print(f'\033[32mValor "{n}" é um valor inteiro válido\033[m')
            break

def leiaFloat(n):
    n = input(n)
    while True:
        try:
            n=float(n)
        except:
            print(f'\033[31mErro! Valor "{n}" inválido! \033[m')
            n = input('Digite um novo valor:')
        else:
            print(f'\033[32mValor "{n}" é um valor do tipo float válido\033[m')
            break


numInteiro = leiaInt('Digite um número inteiro: ')
numFloat = leiaFloat('Digite um número do tipo float: ')