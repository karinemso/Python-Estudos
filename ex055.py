# Minha resolução:
'''pesos = []
for c in range(0,5):
    peso = float(input('Digite um peso:'))
    pesos.append(peso)

print(f'O maior peso é {max(pesos)}kg')

print(f'O menor peso é {min(pesos)}kg')'''

maior = 0
menor = 0
for c in range(0,5):
    peso = float(input('Digite um peso:'))
    if c == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso



print(f'O maior peso é {maior}kg')

print(f'O menor peso é {menor}kg')