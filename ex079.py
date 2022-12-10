nums = []
c = 0
while True:
    if c == 0:
        num = int(input('Digite um número:'))
        nums.append(num)
    else:
        num = int(input('Digite outro um número:'))
        if num in nums:
            c+=1
            op = str(input('Deseja continuar adicionando números? [S/N]: ')).upper() 
            if op == 'N':
                break
            else:
                continue
        else:
            nums.append(num)
    c+=1
    op = str(input('Deseja continuar adicionando números? [S/N]: ')).upper() 
    if op == 'N':
        break


print(f'Os números digitados foram{sorted(nums)} e você digitou {c} números')


