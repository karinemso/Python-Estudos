
numtuple = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')))

print(f'O numero 9 apareceu {numtuple.count(9)} vezes')
if 3 in numtuple:
    print(f'O numero 3 apareceu na posição {numtuple.index(3)+1}')
print(f'Os números pares são:', end=' ')
for numero in numtuple:
    if numero % 2 == 0:
        print(numero, end=' ')
