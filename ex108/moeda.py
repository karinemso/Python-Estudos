def aumentar(n):
    aumentado = n + (n*0.1)
    return aumentado

def diminuir(n):
    diminuido = n - (n*0.1)
    return diminuido

def dobro(n):
    dobro = n * 2
    return dobro

def metade(n):
    metade = n / 2
    return metade

def moeda(n):
    format = 'R$'+ str(f'{n:.2f}')
    if format.count('.') == 1:
        reformat = format.replace('.',',')
        return reformat
    else:
        return format