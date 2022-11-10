from datetime import date
birth_year = int(input('Qual seu ano de nascimento? '))

this_year = date.today().year
age = this_year - birth_year

if age >= 16 and age < 18:
    print('Você já pode se alistar! ')
elif age == 18: 
    print('Você deve se alistar esse ano!')
elif age > 18:
    print('Já passou o seu período de alistamento')
else:
    print('Você não pode se alistar')

