print('-=-'*20)
print('SUPER LOJA BARATONA')
print('-=-'*20)
soma = 0
maisde1000= 0
c = 0
while True:
    product = str(input('Qual o produto que deseja comprar? '))
    price = float(input('Qual o preço desse produto? R$'))
    op = int(input('Deseja continuar comprando [0- sim 1- não]?'))
    while op != 0 and op !=1:
         op = int(input('Deseja continuar comprando [0- sim 1- não]?'))
    print('-=-'*20)
    c+=1
    soma += price
    if price > 1000:
        maisde1000+=1
    if c == 1 or price < maisbarato:
        maisbarato = price
        maisbaratonome = product
    if op == 0:
        print('Coloque seu próximo produto no carrinho: ')
    elif op == 1:
        print('Obrigada por comprar com a gente!')
        print('Aqui vão os dados sobre a sua compra: ')
        break

print(f'O total gasto na compra de {c} produtos foi de R${soma:.2f}')
print(f'{maisde1000} produtos custam mais de R$1000.00')
print(f'O produto mais barato foi {maisbaratonome.capitalize()} e custou R${maisbarato:.2f}')