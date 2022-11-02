from random import choice

alu1 = input('Digite o nome do primeiro aluno: ')
alu2 = input('Digite o nome do segundo aluno: ')
alu3 = input('Digite o nome do terceiro aluno: ')
alu4 = input('Digite o nome do quarto aluno: ')

alunos = [alu1, alu2, alu3, alu4]

ch = choice(alunos)

print(f'A aluna ou aluno escolhido foi {ch}')
