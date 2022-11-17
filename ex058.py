from random import randint

nummaquina = randint(0,10)
numpessoa = int(input('Tente adivinhar o número que estou pensando de 0 a 10\nDigite um número: '))
c= 1
while numpessoa != nummaquina:
    if c == 1:
        print(f'Eu estava pensando no número {nummaquina} e você digitou {numpessoa}')
    c+=1
    nummaquina = randint(0,10)
    numpessoa = int(input('Não foi dessa vez!\nDigite um número novamente: '))
    print(f'Eu estava pensando no número {nummaquina} e você digitou {numpessoa}')

print(f'Agora sim! Você acertou! Eu estava pensando no número {nummaquina} e você digitou {numpessoa}')
print(f'Para isso você precisou de {c} palpites')