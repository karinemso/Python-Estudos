from random import randint

print('-=-'*10)
print('   VAMOS JOGAR \033[0;35mIMPAR PAR!\033[m   ')
print('-=-'*10)
print('REGRAS')
print('''1- Nós dois jogamos um número de 0 a 10
2- Escolha impar ou par! 
3- Ganha o jogo quem escolheu o tipo de número que a soma dos números jogados forma
''')
print('Vamos começar!')
c = 0
ipmaquina = 0
par = 1
impar = 0
while True:
    num = int(input('Digite um número de 0 a 10: '))
    while num > 10 or num <0:
        num = int(input('Número inválido! Digite um número de 0 a 10: '))
    ippessoa = int(input('[0] impar\n[1] par\nDigite sua opção: '))
    while ippessoa != 0 and ippessoa != 1:
        ippessoa = int(input('[0] impar\n[1] par\nDigite 0 ou 1: '))
    nummaquina = randint(0,10)
    if ippessoa == 0:
        ipmaquina = 1
    elif ippessoa == 1:
        ipmaquina == 0
    soma = num + nummaquina
    if soma % 2 == 0:
        if ippessoa == 1:
            print('Parabéns você venceu!')
            print(f'Eu joguei o número {nummaquina} e você jogou o número {num}, resultando em {soma} que é um número par')
            print('-=-'*10)
        else:
            print(f'Eu joguei o número {nummaquina} e você jogou o número {num}, resultando em {soma} que é um número par')
            print(f'Ops, por isso você perdeu dessa vez. Mesmo assim, você ganhou {c} vezes')
            break
    else:
        if ippessoa == 0:
            print('Parabéns você venceu!')
            print(f'Eu joguei o número {nummaquina} e você jogou o número {num}, resultando em {soma} que é um número impar')
            print('-=-'*10)
        else:
            print(f'Eu joguei o número {nummaquina} e você jogou o número {num}, resultando em {soma} que é um número impar')
            print(f'Ops, por isso você perdeu dessa vez. Mesmo assim, você ganhou {c} veze(s)')
            break
    c+=1        
    