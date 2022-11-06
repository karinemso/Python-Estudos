print('-=-'*15)
print('\033[0;33;45mAnalisador de triângulos\033[m')
print('-=-'*15)

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg1 + seg3 > seg2:
    print('Esses segmentos podem formar um triângulo. \033[0;32mEsse triângulo existe!\033[m')
else:
    print('Ops, \033[0;31messe triângulo não existe!\033[m')