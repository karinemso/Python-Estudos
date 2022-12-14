nums = []
for c in range(0,5):
    if c == 0:
        num = int(input(f'Digite um número na Posição {c}: '))
    else:
        num = int(input(f'Digite mais um número na Posição {c}: '))
    nums.append(num)


max = max(nums)
min = min(nums)
max_position = []
min_position = []


for c, n in enumerate(nums):
    if n == max:
        max_position.append(c)
    if n == min:
        min_position.append(c)
        


print('-=-'*20)
print(f'Os números digitados foram {nums}:')
print(f'O maior número digitado foi {max} e ele esta nas posições: {max_position}')
print(f'O menor número digitado foi {min} e ele esta nas posições: {min_position}')
print('-=-'*20)