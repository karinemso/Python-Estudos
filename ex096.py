def area(l,c):
    a = l * c
    print(f'A área de um terreno {l}X{c} é de {a}m²')

print('Controle de terrenos')
print('-'*20)
largura = float(input('Digite a largura do seu terreno: '))
altura = float(input('Digite a altura do seu terreno: '))

area(largura, altura)