nums = []
c = 0
while True:
    if c == 0:
        num = int(input('Digite um número:'))
        
    else:
        num = int(input('Digite outro um número:'))
        if num in nums:
            c+=1
            print('Valor duplicado. Esse valor não será adicionado à lista.')
            op = str(input('Deseja continuar adicionando números? [S/N]: ')).upper() 
            while op not in 'SN':
                op = str(input('Deseja continuar adicionando números? [S/N]: ')).upper() 
            if op == 'N':
                break
            elif op == 'S':
                continue
                
    print('Valor adicionado com sucesso!')
    nums.append(num)
    c+=1
    op = str(input('Deseja continuar adicionando números? [S/N]: ')).upper() 
    while op not in 'SN':
        op = str(input('Deseja continuar adicionando números? [S/N]: ')).upper() 
    if op == 'N':
        break
    elif op == 'S':
         continue

nums.sort()
print(f'Os números digitados foram {nums} e você digitou {c} números')


