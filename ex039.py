from datetime import date
birth_year = int(input('Qual seu ano de nascimento? '))

this_year = date.today().year
age = this_year - birth_year

if age >= 16 and age < 18:
    yearsgap = 18 - age
    print(f'Quem nasceu em {birth_year} tem {age} anos em {this_year}!')
    print(f'Faltam {yearsgap} anos para se alistar')
    print(f'Seu alistamento será em {this_year + yearsgap}')
elif age == 18: 
    print(f'Quem nasceu em {birth_year} tem {age} anos em {this_year}!')
    print('Você deve se alistar esse ano!')
elif age > 18:
    when18 = birth_year + 18
    print(f'Quem nasceu em {birth_year} tem {age} anos em {this_year}!')
    print(f'Você já deveria ter se alistado a {this_year - when18} anos')
    print(f'Seu alistamento foi em {when18}')
else:
    print('Você não pode se alistar')

