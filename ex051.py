first_term = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))

for c in range(1,11):
    term = first_term +(c - 1)*razao
    print(f'{c}° termo da P.A é: {term}')