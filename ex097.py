def escreva(msg):
    tam = len(msg) -1
    print('~'*(len(msg))*3)
    print(' '*tam,msg,' '*tam)
    print('~'*(len(msg))*3)

escreva(str(input('Digite uma palavra ou frase:')))