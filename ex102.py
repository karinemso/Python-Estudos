def fatorial(num, show=False):
    """
        Calcula fatorial de um número
        param num: número que terá o seu fatorial calculado
        param show: mostra ou não o cálculo do fatorial
        return msg: resultado do fatorial
    
    """
    f = num
   
    firstnum = num
    for c in range(num, 0,-1):
        if c != 1:
            f = f * (c-1)
        if show == True:
            if c == num:
                if num == 1:
                    print(f'{c} x {c} = {f}')
                else:
                    print(f'{f"Fatorial de {num}":-^30}')
                    print(f'{c} x ',end='')
            elif c == 1:
                print(f'{c} = ',end='')
                print(f)
            elif c != 0 :
                print(f'{c} x ',end='')

    msg = print(f'O fatorial de {firstnum} é {f}')
    return msg
        
fatorial(5,True)

# O fatorial seria mais simples de fazes atribuindo 1 a váriavel f, assim não seria necessário colocar (c-1)
# Somente c. Dessa forma : f*=c

