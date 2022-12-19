from time import sleep

def contador(inicio, fim , passo):
    if inicio > fim:
        if passo == 0:
            passo = 1
        print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
        sleep(1)
        if fim <= 0:
            fim-=1
        if passo > 0:
            passo = -passo
        for c in range(inicio, fim, passo):
                print(c, end=' ', flush=True)
                sleep(0.5)
        print('FIM!')
        print('-=-'*10)
            
    else:
        if passo < 0:
            passo*=-1
        print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
        sleep(1)
        for c in range(inicio, fim+1, passo):
                print(c, end=' ', flush=True)
                sleep(0.5)
        print('FIM!')
        print('-=-'*10)

contador(1,10,1)
contador(10,0,2)
i = int(input('Digite um número para inicio: '))
f = int(input('Digite um número para fim: '))
p = int(input('Digite um número para passo: '))
contador(i,f,p)
