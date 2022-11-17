
num = int(input('Digite um número inteiro: '))

cont = 0
for c in range(1,num + 1): 
    op = num % c
    if op == 0:
        print(f'\033[0;31m{c}\033[m', end = ' ')
        cont+=1
    else:
        print(f'{c}', end = ' ')

if cont == 2:
    print(f'\nPor isso o número {num} é primo')
else:
    print(f'\nPor isso o número {num} não é primo')
