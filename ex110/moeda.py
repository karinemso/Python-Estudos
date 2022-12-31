def aumentar(n, q,f=False):
    aumentado = n + (n*q/100)
    if f == True:
       aumentado = moeda(aumentado)
    return aumentado

def diminuir(n,q,f=False):
    diminuido = n - (n*q/100)
    if f == True:
       diminuido = moeda(diminuido)
    return diminuido


def dobro(n,f=False):
    dobro = n * 2
    if f == True:
       dobro = moeda(dobro)
    return dobro

def metade(n,f=False):
    metade = n / 2
    if f == True:
       metade = moeda(metade)
    return metade

def moeda(n):
    format = 'R$'+ str(f'{n:.2f}')
    if format.count('.') == 1:
        reformat = format.replace('.',',')
        return reformat
    else:
        return format

def resume(n,a,d):
    print('-'*60)
    print(f'{"Resumo dos valores":^60}')
    print('-'*60)
    print(f' -- O valor analisado foi {moeda(n)}')
    print(f' -- O dobro do valor é {dobro(n,True):^10}')
    print(f' -- A metade do valor é {metade(n,True):^10}')
    print(f' -- O valor aumentado em {a}% é {aumentar(n,a,True):^10}')
    print(f' -- O valor diminuido em {d}% é {diminuir(n,d,True):^10}')
   
    print('-'*60)
