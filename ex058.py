from random import randint

print('-=-'*20)
print('\033[0;34mJOGO ADIVINHE O NÚMERO QUE ESTOU PENSANDO\033[m')
print('-=-'*20)
nummaquina = randint(0,10)
numpessoa = int(input('Tente adivinhar o número que estou pensando de 0 a 10\nDigite um número: '))
c= 0
querojogar = 1
while querojogar == 1:
    c+=1
    if nummaquina > numpessoa:
        numpessoa = int(input('\033[0;33mMais..!\nDigite um número novamente:\033[m '))
    elif nummaquina < numpessoa:
        numpessoa = int(input('\033[0;33mMenos..!\nDigite um número novamente:\033[m '))
    elif nummaquina == numpessoa:
        print(f'\033[0;32mAgora sim! Você acertou! Eu estava pensando no número {nummaquina} e você digitou {numpessoa}\033[m')
        print(f'Para isso você precisou de {c} palpite(s)')
        querojogar = int(input('''Quer jogar de novo?\n[1]Quero jogar de novo\n[0] Não quero jogar mais\nDigite sua opção: '''))
        if querojogar == 1:
            print('O jogo vai começar novamente! Pensei em outro número de 0 a 10')
            nummaquina = randint(0,10)
            numpessoa = int(input('Digite seu palpite: '))
            c = 0


print('Obrigada por ter jogado comigo! Volte sempre!')
