print('-=-'*15)
print('FAÇA SUA COMPRA')
print('-=-'*15)
product = float(input('Qual o valor do produto desejado? '))
print(f'Para comprar à vista no dinheiro ou cheque com 10% de desconto - Digite 1')
print(f'Para comprar à vista no cartâo com 5% de desconto - Digite 2')
print(f'Até 2x no cartâo - Digite 3')
print(f'3x ou mais no cartão (20% de juros) - Digite 4')
choice = int(input('Digite o número correspondente à opção desejada: '))

if choice == 1:
    price = product - (product * 0.1)
    economy = product - price
    print(f'O valor final do seu produto é de R${price:.2f} e você economizou R${economy:.2f}')
elif choice == 2:
    price = product - (product * 0.05)
    economy = product - price
    print(f'O valor final do seu produto é de R${price:.2f} e você economizou R${economy:.2f}')
elif choice == 3:
    parcela = product/2
    print(f'O valor final do seu produto é de R${product:.2f} e você pagará 2x de R${parcela:.2f}!')
elif choice == 4:
    parcela = int(input('Quantas vezes você deseja parcelar? '))
    price = product + (product * 0.2)
    prestação = price/ parcela
    waste = price - product
    print(f'O valor final do seu produto é de R${price:.2f} e você acrescentou R${waste:.2f} ao valor original!')
    print(f'Você pagará {parcela} parcelas de {prestação:.2f}')
else:
    print('Opção inválida! Tente novamente!')

