
from math import pow, sqrt, hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

# a hipotenusa ao quadrado é igual a soma do quadrado dos catetos
#h = sqrt(pow(co, 2) + pow(ca, 2))
#método mais fácil é usar hypot

h = hypot(co,ca)

print(f'A hipotenusa mede {h:.2f}cm')
