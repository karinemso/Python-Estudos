nums = []
nums_pares = []
nums_impares = []
 
c = 0
while True:
    if c == 0:
        num = int(input('Digite um número: '))
    else:
        num = int(input('Digite outro número: '))
    nums.append(num)

    op = str(input('Deseja continuar digitando números?[S/N]: ')).upper()
    while op not in 'SN':
        op = str(input('Deseja continuar digitando números?[S/N]: ')).upper()
    if op == 'S':
        continue
    elif op == 'N':
        break

for n in nums:
    if n % 2 == 0:
        nums_pares.append(n)
    else:
        nums_impares.append(n)

print('-=-' * 10)
print(f'Os números digitados foram: {nums}')
print(f'Dentre eles, os números pares são: {nums_pares}')
print(f'E os impares: {nums_impares}')
print('-=-' * 10)
