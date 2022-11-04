distance = float(input('Qual a distância da sua viagem em Km? '))
print(f'Você está prestes a começar uma viagem de {distance}Km')
'''if distance <= 200:
    price = distance * 0.5
else:
    price = distance * 0.45'''
price = distance * 0.5 if distance <= 200 else distance * 0.45
print(f'E o preço da sua passagem será R${price:.2f}')