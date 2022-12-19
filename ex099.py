from time import sleep

def maior(*nums):
    maior = 0
    for c,n in enumerate(nums):
        if c == 0:
            maior = n
        if n > maior:
            maior = n
    print('Análisando os valores passados...')
    sleep(1)
    for n in nums:
        print(n, end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(nums)} números')
    print(f'O maior valor informado foi: {maior}')
    print('-=-'*30)
    sleep(1)


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()






