from random import randint
from time import sleep                           

print('-=-'*20)
print(f'{"MEGA SENA DA VIRADA":^60}')
print('-=-'*20)

op = int(input('Quantos palpites você quer gerar? '))


jogos = []
jogo = []

for c in range(0,op):
    while len(jogo) != 6:
        numerosorte = randint(1,60)
        if c == 0:
            jogo.append(numerosorte)
        if numerosorte not in jogo:
            jogo.append(numerosorte)
    jogos.append(jogo[:])
    jogo.clear()

c = 1
print('-=-'*20)
print(f'{"RESULTADO":^60}')
print('-=-'*20)

for j in jogos:
    j.sort()
    print(f'Jogo n°{c}: {j}')
    sleep(1)
    c+=1
print('-=-'*20)
print(f'{"BOA SORTE":-^60}')