
pares =[]
impares = []
nums=[pares,impares]

for c in range(1, 8):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('-=-'*20)
for n in nums:
    n.sort()
    if n == nums[0]:
        print(f'Os valores pares digitados foram: {n}')
    else:
        print(f'Os valores impares digitados foram: {n}')


