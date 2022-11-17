from random import choice
from time import sleep


print('-=-'*15)
print('VAMOS JOGAR \033[0;34mPEDRA, PAPEL E TESOURA\033[m')
print('-=-'*15)
your_choice = str(input('Digite pedra, papel ou tesoura: ')).lower()
possible = ['pedra', 'papel', 'tesoura']
mychoice = choice(possible)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')


if mychoice == your_choice:
    print(f'Nós dois jogamos {mychoice.capitalize()}. \033[0;33mEMPATE!\033[m')

machinewin1= mychoice == 'pedra' and your_choice == 'tesoura'
machinewin2 = mychoice == 'tesoura' and your_choice == 'papel'
machinewin3 = mychoice == 'papel' and your_choice == 'pedra'
youwin1= mychoice == 'tesoura' and your_choice == 'pedra'
youwin2 = mychoice == 'papel' and your_choice == 'tesoura'
youwin3 = mychoice == 'pedra' and your_choice == 'papel'

if machinewin1 or machinewin2 or machinewin3 :
    print(f'{mychoice.capitalize()} ganha de {your_choice.capitalize()} - \033[0;31mVOCÊ PERDEU\033[m')

if youwin1 or youwin2 or youwin3 :
    print(f'{your_choice.capitalize()} ganha de {mychoice.capitalize()} - \033[0;32mVOCÊ GANHOU\033[m')
