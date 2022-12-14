
boletim_geral = []
aluno = []

while True:
    nome_aluno = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    aluno.append(nome_aluno)
    aluno.append(nota1)
    aluno.append(nota2)
    boletim_geral.append(aluno[:])
    aluno.clear()
    op = str(input('Deseja continuar cadastrando?[S/N]')).upper()
    while op not in 'SN':
        op = str(input('Deseja continuar cadastrando?[S/N]')).upper()
    if op == 'N':
        break


for c,a in  enumerate(boletim_geral):
    if a == boletim_geral[0]:
        print('-'*55)
        print(f'{"BOLETIM GERAL":^55}')
        print('-'*55)
        print(f'{"N°":<10}',f'{"NOME":^10}', f'{"MEDIA":>20}')
        print('-'*55)
    media = (a[1] + a[2])/2
    print(f'{c:<10}'f'{a[0]:^10}', f'{media:>20}')

while True:
    print('-'*55)
    op = int(input("""[1] Desejo ver o boletim geral novamente\n[2] Quero acessar as notas de um aluno individualmente\n[3] Desejo encerrar o programa\nDigite sua opção: """))
    if op == 1:
        for c,a in  enumerate(boletim_geral):
            if a == boletim_geral[0]:
                print('-'*55)
                print(f'{"BOLETIM GERAL":^55}')
                print('-'*55)
                print(f'{"N°":<10}',f'{"NOME":^10}', f'{"MEDIA":>10}')
                print('-'*55)
            media = (a[1] + a[2])/2
            print(f'{c:<10}'f'{a[0]:^10}', f'{media:>10}')
    elif op == 2:
        naluno = int(input('Digite o número do aluno que você quer consultar a nota: '))
        print('-'*55)
        print(f'{"BOLETIM INDIVIDUAL":^55}')
        print('-'*55)
        print(f'{"N°":^10}',f'{"NOME":^10}', f'{"NOTA 1":^10}', f'{"NOTA 2":^10}', f'{"MEDIA":^10}')
        print('-'*55)
        media = (boletim_geral[naluno][1] + boletim_geral[naluno][2])/2
        print(f'{naluno:^10}'f'{boletim_geral[naluno][0]:^10}', f'{boletim_geral[naluno][1]:^10}', f'{boletim_geral[naluno][2]:^10}', f'{media:^10}')
    elif op == 3:
        break
