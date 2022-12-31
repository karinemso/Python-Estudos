

cores = ['\033[0m','\033[40m', '\033[42m', '\033[43m' ,'\033[45m']
def helping(com):
    """ Recebe um comando para ser acessado pelo Help do Python 
    e o torna mais amigável ao usuário"""
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cores[1],end='')
    help(com)
    print(cores[0],end='')
    
    
def colorir(c):
    print(cores[c], end='')


def titulo (msg, c = 0):
    tam= len(msg) + 4
    print(cores[c], end='')
    print("~"*tam)
    print(f'  {msg}')
    print("~"*tam)
    print(cores[0], end =' ')

titulo(f'Seja bem vindo ao Help do Python!', 2)
msg = input('Digite o comando que você quer saber mais sobre: ')
while msg.upper() != 'FIM':
       helping(msg) 
       msg = input('Digite o comando que você quer saber mais sobre: ')

titulo('Até logo!',3)