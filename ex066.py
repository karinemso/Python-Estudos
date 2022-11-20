c=0
soma = 0
while True:
    num = int(input('Digite um numero[999 para parar]:'))
    if num == 999:
        break
    c+=1
    soma+=num

print(f'{c} números foram digitados e a soma entre eles resulta em {soma}')    