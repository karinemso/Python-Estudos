
fnum = int(input('Primeiro valor: '))
snum = int(input('Segundo valor: '))
tnum = int(input('Terceiro valor: '))

numbers = [fnum, snum, tnum]
maxnum = max(numbers)
min_num = min(numbers)

print(f'O \033[0;35mmenor valor\033[m digitado foi \033[0;35m{min_num}\033[m')
print(f'O \033[0;34mmaior valor\033[m digitado foi \033[0;34m{maxnum}\033[m')