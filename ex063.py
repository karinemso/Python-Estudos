
print('-=-'*15)
print('Sequência de Fibonacci')
print('-=-'*15)

quant = int(input('Quantos elementos quer gerar? '))

c = 0
termo = 1
termoanterior = 0
while c < quant:
    termo = termo + termoanterior
    if c == 0:
         print(f'{0} -> {1} -> {termo} -> ', end='')
    elif c == quant - 1:
        print(f'{termo}', end='')
    else:
        print(f'{termo} -> ', end='')
    termoanterior = termo - termoanterior

    c+=1


