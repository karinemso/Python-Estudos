from random import randint
from time import sleep

def somapar(lista):
    soma = 0
    par = []
    for n in lista:
        if n % 2 == 0:
            soma+=n
            par.append(n)
    print(f'Os números pares são {par} e a soma entre os números pares resulta em {soma}')

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0,5):
        num = randint(1,10)
        lista.append(num)
        print(num, end=' ', flush=True)
        sleep(0.5)
    print()

numeros = []
sorteia(numeros)
somapar(numeros)

