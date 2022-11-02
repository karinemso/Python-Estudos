from random import shuffle

n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))

alunos = [n1, n2, n3, n4]
order = shuffle(alunos)
#shuffle não retorna uma nova lista, mas sim altera a lista original

print(f'A ordem de apresentações será: {alunos}')
