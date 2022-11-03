import mailbox


name = str(input('Digite seu nome completo: '))

maiusc = name.upper()
minus = name.lower()
spaces = name.count(' ')
length = len(name) - spaces
splited = name.split()
firstname = splited[0]
lastname = splited[-1]
#lastname = splited[len(splited)-1]
#lastname = splited.pop()
print(f'Seu nome em maiúsculo é: {maiusc}')
print(f'Seu nome em minúsculo é: {minus}')
print(f'Seu nome tem {length} letras')
print(f'Seu primeiro nome é {firstname} e possui {len(firstname)} letras')
print(f'Seu ultimo nome é: {lastname}')