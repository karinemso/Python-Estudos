def leiaInt(msg):
    """ Lê um valor e só o aceita se for do tipo inteiro
        param msg: mensagem do input
        return num: número inteiro válido
    """
    num = input(msg)
    while  num.strip().isnumeric()== False:
        print('\033[0;31mErro! Você não digitou um valor do tipo inteiro!\033[m')
        num = input(msg)
    print('\033[0;32mValor do tipo inteiro recebido!\033[m')
    return num
        


n = leiaInt('Digite um valor:')
print(f'Você acabou de digitar o número {n}')