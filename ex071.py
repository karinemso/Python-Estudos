print('-=-'*20)
print('CAIXA ELETRÔNICO')
print('-=-'*20)

num = int(input('Quanto você deseja sacar? '))
n= 50
c = 0
total= num
while True:
    if total >= n:
        total = total- n
        c+=1
        if c >= 1 and total < n and n==1:
            print(f'Você receberá {c} moedas de R${n}')
        elif c >= 1 and total < n:
            print(f'Você receberá {c} notas de R${n}')
    else:
        if n == 50:
            n = 20
            c = 0
        elif n == 20:
            n = 10
            c = 0
        elif n == 10:
            n = 1
            c = 0
    if total == 0:
        break
    


