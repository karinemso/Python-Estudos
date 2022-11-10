house_value = float(input('Qual é o  valor da casa? R$'))
buyer_salary = float(input('Quanto você ganha? R$'))
years = int(input('Em quantos anos você pretende pagar? '))

part = house_value/(years*12)

print(f'Para pagar uma casa de R${house_value:.2f} em {years} anos', end =' ')
print(f'a prestação mensal será de R${part:.2f}')


if part > buyer_salary * 0.3:
    print('Empréstimo \033[0;31mnegado\033[m')
else:
    print('Empréstimo \033[0;32maprovado\033[m')