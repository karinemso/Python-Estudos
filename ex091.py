from random import randint
from time import sleep
from operator import itemgetter

print('Joguem seus DADOS!')

jogos = dict()
jogos['jogador1'] = randint(1,6)
jogos['jogador2'] = randint(1,6)
jogos['jogador3'] = randint(1,6)
jogos['jogador4'] = randint(1,6)

ranking = []
for k,j in jogos.items():
    print(f'O {k} tirou {j} no dado')
    sleep(1)

ranking = sorted(jogos.items(), key = itemgetter(1), reverse=True)

print('-=-'*10)

for c, j in enumerate(ranking):
    print(f'O {c+1}° colocado foi {j[0]} com {j[1]} pontos')
    sleep(1)