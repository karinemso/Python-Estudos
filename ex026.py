name = str(input('Digite seu nome completo: ')).lower().strip()
howmany_a = name.count('a')
first_a = name.find('a') + 1
last_a = name.rfind('a') + 1

print(f'Seu nome tem quantos A? {howmany_a}')
print(f'Onde aparece o primeiro A? {first_a}')
print(f'Onde aparece o último A? {last_a}')
