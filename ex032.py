from datetime import date
year = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
current_year = 2022
if year == 0 and current_year % 4 == 0 or current_year == 0 and current_year/100 % 10 == 00 and current_year % 400 == 0:
     print(f'O ano {current_year} é bissexto!')
elif  year != 0 and year/100 % 10 == 00 and year % 400 == 0 or year/10 % 10 == 00 and year % 400 == 0:
    print(f'O ano {year} é bissexto!')
elif  year != 0 and year/100 % 10 == 00 and year % 400 != 0:
    print(f'O ano {year} NÃO é bissexto!')
elif year != 0 and year/100 % 10 != 00 and year/10 % 10 != 00 and year % 4 == 0:
    print(f'O ano {year} é bissexto!')
elif year == 0:
    print(f'O ano {current_year} NÃO é bissexto!')
else:
    print(f'O ano {year} NÃO é bissexto!')