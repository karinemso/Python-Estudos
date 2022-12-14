matriz = [[0,0,0], [0,0,0], [0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l},{c}]:'))

somapar = 0
soma3c = 0
print('-=-'*10)
for l in range(0,3):
    for c in range(0,3):
        if c == 2:
            print(f'[{matriz[l][c]:^5}]')
            soma3c+=matriz[l][c]
        else:
            print(f'[{matriz[l][c]:^5}]', end ='')
        if matriz[l][c] %2 == 0:
            somapar+=matriz[l][c]
print('-=-'*10)
print(f'A soma de todos os valores pares digitados é: {somapar}')
print(f'A soma de todos os números da terceira coluna é: {soma3c}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
