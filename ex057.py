'''sexo = str(input('Qual seu sexo [M/F]? '))

while sexo != 'M' or  sexo !='F':
    sexo = str(input('Qual seu sexo [M/F]? '))
    print('Sexo inválido. Digite M ou F')
    

print(f'Seu sexo é {sexo}')'''
#Por que não funcionou? Por que M sempre será diferente de F e vice versa, causando um loop infinito



sexo = str(input('Qual seu sexo [M/F]? ')).upper().strip()

while sexo not in'MF':
    sexo = str(input('Dado inválido. Informe seu sexo [M/F]: ')).upper().strip()
   
print(f'Seu sexo é {sexo}')