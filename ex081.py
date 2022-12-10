nums=[]
c = 0
while True:
    if c == 0:
        num = int(input('Digite um número: '))
    else:
        num = int(input('Digite mais um número: '))
    nums.append(num)
    c+=1

    op = str(input('Deseja continuar adicionando números? [S/N]: ')).upper()
    while op not in 'SN':
        op = str(input('Deseja continuar adicionando números? [S/N]: ')).upper()
    if op == 'S':
        continue
    elif op == 'N':
        break
    
print('-'*40)
print(f'{"Resultado":^40}')
print('-'*40)
print(f'{c} numéros foram digitados')
print(f'A lista em ordem decrescente é: {sorted(nums, reverse= True)}')
if 5 in nums:
    print(f'O número 5 foi digitado')
else:
    print(f'O número 5 \033[0;31mNÃO\033[m foi digitado')
