palavras = ('acucar', 'mel', 'banana', 'maca', 'pera', 'uva','melancia')
vogais = ('a', 'e', 'i', 'o', 'u')
c = 0
for palavra in palavras:
    print(f'\nA palavra {palavra} tem as vogais:', end='')
    for letra in palavra:
        c+=1
        if letra in vogais:
                print(letra, end=' ')
    c = 0
    
    
    

