num = int(input('Digite um número: '))
print('Escolha a base de conversão:')
convert = int(input('Digite 1 para binário\nDigite 2 para octal\nDigite 3 para hexadecimal: '))

if convert == 1:
    numbin = bin(num)
    print(f'O número {num} em binário é {numbin}')
elif convert == 2:
    ocnum = oct(num)
    print(f'O número {num} em octal é {ocnum}')
elif convert == 3:
    hexanum = hex(num)
    print(f'O número {num} em octal é {hexanum}')