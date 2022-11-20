c = 1
soma = 0
nums =[]
funciona = True
quant = 0
while funciona:
    if c == 1:
        num = int(input('Digite um número: '))
        quant+=1
        nums.append(num)
        soma+=num
        op = int(input('Deseja digitar mais um número[1 - continua; Outro - termina o programa]? '))
        if op != 1:
            funciona = False
            
    else:
        num = int(input('Digite outro número: '))
        quant+=1
        nums.append(num)
        soma+=num
        op = int(input('Deseja digitar mais um número[1 - continua; Outro - termina o programa]? '))
        if op != 1:
            funciona = False
        
    

print(f'{quant} números foram digitados e a média entre eles é {soma/quant}')
print(f'O maior número digitado foi {max(nums)} e o menor {min(nums)}')