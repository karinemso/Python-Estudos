from datetime import date

birth_year = int(input('Para saber sua categoria na Confederação Nacional de Natação,\nDigite seu ano de nascimento: '))
age = date.today().year - birth_year
print(age)

if age <= 9:
    print(f'Sua idade é {age} - Categoria Mirim')
elif age <=14:
     print(f'Sua idade é {age} - Categoria Infantil')
elif age <=19:
     print(f'Sua idade é {age} - Categoria Júnior')
elif age <= 20:
     print(f'Sua idade é {age} - Categoria Sênior')
else:
     print(f'Sua idade é {age} - Categoria Master')