nums = []

for c in range(0,5):
    num = int(input('Digite  um número: '))
    if c == 0 or num > nums[-1]:
        nums.append(num)
        print(f'Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(nums):
            if num <= nums[pos]:
                nums.insert(pos, num)
                print(f'Valor adicionado na posição {pos}')
                break
            pos+=1

print(f'Sua lista em ordem crescente é: {nums}')
