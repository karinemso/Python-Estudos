from random import randint
from time import sleep

num = randint(0,5)
print('-'*20)
print('Estou pensando em um número de 0 a 5. Consegue adivinhar qual?')
print('-'*20)
palpite = int(input('Digite seu palpite: '))
print('PROCESSANDO...')
sleep(2)
if palpite == num:
    print('Parabéns, você adivinhou!')
else:
    print(f'Não foi dessa vez.. O número que eu estava pensando era {num}')

