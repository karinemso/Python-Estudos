from datetime import datetime

year = datetime.now().year

pessoa = dict()

pessoa['nome'] = str(input('Digite seu nome: '))
pessoa['idade'] = year - int(input('Digite seu ano de nascimento: '))
pessoa['ctps'] = int(input('Digite o número da sua carteira de trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Digite seu ano de contratação: '))
    pessoa['salario'] = float(input('Qual o seu salário: '))
    tempocontrib = year - pessoa['contratação']
    pessoa['aposentadoria'] = (35 - tempocontrib) + pessoa['idade']

print('-=-' * 10)
for k, v in pessoa.items():
    print(f'  -{k.capitalize()} é igual a: {v}')


