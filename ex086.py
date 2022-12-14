

matriz = []

cont = 0
for c in range(0,9):
    if c <= 2:
        num = int(input(f'Digite um número para a posição [0,{cont}]: '))
        matriz.append([num])
        cont+=1
    if c>2 and c <=5:
        if c == 3:
            cont=0
        num = int(input(f'Digite um número para a posição [1,{cont}]: '))
        matriz.append([num])
        cont+=1
    if c>5 and c <=9:
        if c == 6:
            cont=0
        num = int(input(f'Digite um número para a posição [2,{cont}]: '))
        matriz.append([num])
        cont+=1
    

print('-=-'*10)
linha = 0
for n in matriz:
    linha+=1
    if linha == 3 or linha == 6:
         print(n)
    else:
        print(f'{n:^5} ', end='')

