from datetime import date

thisyear= date.today().year
maior = 0
menor = 0

for c in range (0,6):
    birthyear = int(input('Digite um ano de nascimento: '))
    op = thisyear - birthyear
    if op >= 18:
        maior+= 1
    else:
        menor+=1


print(f'{menor} pessoas ainda não atingiram a maioridade')
print(f'{maior} pessoas já atingiram a maioridade')