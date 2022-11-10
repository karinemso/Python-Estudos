n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

if n1 > n2:
    print(f'O primeiro número ({n1}) é maior')
elif n2 > n1:
    print(f'O segundo número ({n2}) é maior')
else:
    print(f'Os números são IGUAIS')