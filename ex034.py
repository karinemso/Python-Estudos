salary = float(input('Qual é o salário do funcionário? '))

if salary > 1250:
    increase = salary + (salary *0.10)
else:
    increase = salary + (salary *0.15)

print(f'Quem ganhava \033[0;31mR${salary:.2f} \033[mpassa a ganhar \033[0;32mR${increase:.2f}\033[m agora')