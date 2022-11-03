

#Essa é a resolução do professor:
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Seu numéro é: {num} \n Unidade:{u} \n Dezena:{d} \n Centena: {c} \n Milhar:{m}')

#A porcentagem é o resto da divisão por 10
"""Exemplo número 5432
    Divindo por 1 = 5432 
    Dividindo por 10 = 543 com o resto 2 ou 543,2
    Desse modo a unidade é 2
    5432 dividido por 10 é 543
    Dividindo por 10 novamente temos 54 com resto 3 ou 54,3
    Resultando em uma dezena equivalente a 3
"""
#Essa foi a solução que eu cheguei sem ver o vídeo de resolução
""""
num = input('Digite um número de 0 a 9999: ')
listnum = list(num)

if len(num) == 4:
        unidade = listnum[3]
        dezena = listnum[2]
        centena = listnum[1]
        milhar = listnum[0]
        print(f'Analisando o número {num}...')
        print(f'Unidade: {unidade}')
        print(f'Dezena: {dezena}')
        print(f'Centena: {centena}')
        print(f'Milhar: {milhar}')
elif len(listnum) == 3:
        unidade = listnum[2]
        dezena = listnum[1]
        centena = listnum[0]
        milhar = 0
        print(f'Analisando o número {num}...')
        print(f'Unidade: {unidade}')
        print(f'Dezena: {dezena}')
        print(f'Centena: {centena}')
        print(f'Milhar: {milhar}')
elif len(listnum) == 2:
        unidade = listnum[1]
        dezena = listnum[0]
        centena = 0
        milhar = 0
        print(f'Analisando o número {num}...')
        print(f'Unidade: {unidade}')
        print(f'Dezena: {dezena}')
        print(f'Centena: {centena}')
        print(f'Milhar: {milhar}')
elif len(listnum) == 1:
        unidade = listnum[0]
        dezena = 0
        centena = 0
        milhar = 0
        print(f'Analisando o número {num}...')
        print(f'Unidade: {unidade}')
        print(f'Dezena: {dezena}')
        print(f'Centena: {centena}')
        print(f'Milhar: {milhar}')"""