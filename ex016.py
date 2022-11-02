from math import trunc, ceil, floor

value = float(input('Digite um número: '))
trunc_value = trunc(value)
up = ceil(value)
down = floor(value)

print(f'O valor digitado foi {value} e sua porção inteira é {trunc_value}')
print(f'Arredondando para cima: {up} \n Arredondando para baixo: {down}')