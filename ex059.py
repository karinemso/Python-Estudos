from time import sleep
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

c = 0

while c == 0:
    print('''
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
    ''')
    op = int(input('Digite sua opção: '))

    if op == 1:
        soma  = num1 + num2
        print(f'O resultado da soma dos números {num1} e {num2} é {soma}')
        print('O menu será reiniciado')
        sleep(1)
    elif op == 2:
        multi = num1 * num2
        print(f'O resultado da multiplicação dos números {num1} e {num2} é {multi}')
        print('O menu será reiniciado')
        sleep(1)
    elif op == 3:
        numarray = [num1,num2]
        maior = max(numarray)
        if num1 == num2:
            print(f'Os números {num1} e {num2} são iguais')
        else:
            print(f'O maior número entre {num1} e {num2} é {maior}')
        print('O menu será reiniciado')
        sleep(1)
    elif op == 4:
        print('Digite novos números')
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        print('O menu será reiniciado')
        sleep(1)

    elif op == 5:
        c = 1

print('Você saiu do programa!')
