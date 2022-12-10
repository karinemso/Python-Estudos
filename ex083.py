exp = str(input('Digite uma expressão matemática:'))

abri = exp.count('(')
fechei = exp.count(')')

if abri == fechei:
    print('Sua expressão está correta')
else:
    if abri> fechei:
        falta_fechar = abri - fechei
        print('-=-'*20)
        print(f'Sua expressão está errada, faltam {falta_fechar} parênteses de fechamento')
        print('-=-'*20)
    elif abri < fechei:
        falta_abrir = fechei - abri
        print('-=-'*20)
        print(f'Sua expressão está errada, faltam {falta_abrir} parênteses de abertura')
        print('-=-'*20)
    
