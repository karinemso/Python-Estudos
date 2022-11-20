first_term = int(input('Digite o primeiro termo da P.A: '))
ratio = int(input('Digite a razão da P.A: '))

c = 1
quant = 11

while c < quant:
    termo = first_term + (c - 1) * ratio
    c= c + 1
    if c == quant:
        print(f'{termo}')
        maistermos = int(input('Quantos termos mais você quer ver [Digite 0 para sair do programa]? '))
        quant = quant + maistermos
        c = 1
        if maistermos == 0 :
            c = quant + 1
    else:
        print(f'{termo} -> ' , end = '')

print('Você saiu do programa')