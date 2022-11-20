first_term = int(input('Digite o primeiro termo da P.A: '))
ratio = int(input('Digite a razão da P.A: '))

c = 1
while c < 11:
    termo = first_term + (c - 1) * ratio
    c= c + 1
    if c == 11:
        print(f'{termo}', end = '')
    else:
        print(f'{termo} -> ' , end = '')
    