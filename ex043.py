

print('-=-'*15)
print('\033[0;34;36mCalculadora de IMC\033[m')
print('-=-'*15)

height = float(input('Digite sua altura em M: '))
wheight = float(input('Digite seu peso: '))

imc = wheight / pow(height,2)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f} - ABAIXO DO PESO')
elif 18.5 < imc < 25:
    print(f'Seu IMC é de {imc:.2f} - PESO IDEAL')
elif 25 < imc <= 30:
    print(f'Seu IMC é de {imc:.2f} - SOBREPESO')
elif 30 < imc <= 40:
    print(f'Seu IMC é de {imc:.2f} - OBESIDADE')
else:
    print(f'Seu IMC é de {imc:.2f} - OBESIDADE MÓRBIDA')
