pessoas = []
pessoa = []
totp = 0

while True:
    pessoa.append(str(input('Digite um nome: ')))
    pessoa.append(float(input('Digite um peso: ')))
    pessoas.append(pessoa[:])
    totp+=1
    pessoa.clear()
    op = str(input('Quer continuar cadastrando?[S/N]: ')).upper()
    while op not in 'SN':
        op = str(input('Quer continuar cadastrando?[S/N]: ')).upper()
    if op in 'Nn':
        break


maiorp = 0
maiorpnome = []
menorp = 0
menorpnome = []
for c,p in enumerate(pessoas):
    if c== 0:
        maiorp = menorp= p[1]
        maiorpnome.append(p[0])
        menorpnome.append(p[0])
    else:
        if p[1]>=maiorp:
            if p[1] != maiorp:
                maiorpnome.clear()
            maiorp= p[1]
            maiorpnome.append(p[0])
        if p[1]<=menorp:
            if p[1] != menorp:
             menorpnome.clear()
            menorp = p[1]
            menorpnome.append(p[0])
       
        
print('-=-'*10)
print(f'{totp} pessoas foram cadastradas')
print(f'As pessoas mais pesadas pesam {maiorp}kg e são {maiorpnome}')
print(f'As pessoas mais leves pesam {menorp}kg e são {menorpnome}')
    