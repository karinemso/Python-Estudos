pessoa = {}
pessoas = []

totp=0
while True:
    
    pessoa['nome'] = str(input('Digite um nome: '))
    pessoa['sexo'] = str(input('Digite o sexo [F/M]: ')).upper()
    while pessoa['sexo'] not in 'FM':
        pessoa['sexo'] = str(input('Digite o sexo [F/M]: ')).upper()
    pessoa['idade'] = int(input('Digite a idade: '))
    pessoas.append(pessoa.copy())
    totp+=1
    pessoa.clear()
    op = str(input('Deseja continuar cadastrando pessoas?[S/N]: ')).upper()
    while op != 'S' and op != 'N':
        op = str(input('Deseja continuar cadastrando pessoas?[S/N]: ')).upper()
    if op == 'N':
        break

idade = 0
mulheres = []
for p in pessoas:
    for k, v in p.items():
        if k == 'idade':
            idade+=v
        if k == 'sexo' and v == 'F':
            mulheres.append(p['nome'])
media = idade/ len(pessoas)
acimamedia = []
for p in pessoas:
    for k, v in p.items():
        if k == 'idade' and v > media:
            acimamedia.append(p)

print('-=-'*10)
print(f'{totp} pessoas foram cadastradas')
print(f'A média da idade do grupo é de {media:.2f} anos')
print(f'As mulheres cadastradas foram: {mulheres}')
print(f'As pessoas com idade acima da média são:')
for p in acimamedia:
    print(f'  => nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]}')