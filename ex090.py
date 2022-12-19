aluno = dict()

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = float(input(f'Digite a média do aluno {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5 and aluno['média'] <7:
     aluno['situação'] = 'Recuperação'
else:
     aluno['situação'] = 'Reprovado'

print('-=-'*10)
for k, a in aluno.items():
    print(f' -{k.capitalize()} é igual a {a}')