# 60 por dia e 0.15 por km rodado

day = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

day_price = day * 60
km_price = km * 0.15
total = day_price + km_price

print(f'O total a pagar é de R${total}')