city = input('Em que cidade você nasceu? ')
lower = city.lower()
l = lower.split()
result = 'santo' in l[0]
print(f'Sua cidade começa com Santo? {result}')

""" Solução do professor:
city = input('Em que cidade você nasceu? ').strip
print(city[:5].upper() == 'SANTO')
"""