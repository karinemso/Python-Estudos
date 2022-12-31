def aumentar(n,f=False):
    aumentado = n + (n*0.1)
    if f == True:
       aumentado = moeda(aumentado)
    return aumentado

def diminuir(n,f=False):
    diminuido = n - (n*0.1)
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