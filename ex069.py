menor18 = 0
homens = 0
mulheres20 = 0
c = 0
print('-=-'*20)
print('CADASTRO DE PESSOAS')
print('-=-'*20)
while True: 
    idade = int(input('Digite uma idade:'))
    sexo = int(input('Digite um sexo[0- feminino;1-masculino]: '))
    c+=1
    while sexo != 0 and sexo != 1:
        sexo = int(input('Digite um sexo váido[0- feminino;1-masculino]: '))
    if idade < 18:
        menor18+=1
    if sexo == 1:
        homens+=1
    if sexo == 0 and idade <20:
        mulheres20+=1
    op =str(input('Quer continuar a cadastrar pessoas[S/N]? ')).upper().strip()
    while op not in 'SN':
        op =str(input('Quer continuar a cadastrar pessoas[S/N]? ')).upper().strip()
    if op == 'N':
        break
    else:
        print('O cadastro será continuado')
        print('-=-'*20)
print('-=-'*20)
print(f'Você cadastrou {c} pessoas')
print(f'Dentre elas {menor18} pessoas tem menos de 18 anos\n{homens} são homens\n{mulheres20} são mulheres com menos de 20 anos')
print('Cadastro encerrado!')
print('-=-'*20)