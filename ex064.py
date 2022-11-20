

num = int(input('Digite um número:'))
c = 0
soma = 0
while num != 999:
    if num != 999:
        soma+=num
        c+=1
    
    num = int(input('Digite outro número:'))
   

print(f'Você digitou {c} números e a soma entre eles resulta em {soma}')

