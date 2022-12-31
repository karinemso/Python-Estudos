def ficha(jg ='desconhecido', gl = 0):
    """
        Faz a ficha de um jogador
        param jg: nome do jogador
        param gl: quantidade de gols
    
    """
    print(f'{"Ficha do jogador":.^50}')
    print(f'O jogador {jg} marcou {gl} gols')



nome = str(input('Digite o nome do jogador: '))
gols = str(input('Quantos gols ele marcou? '))

if gols.isnumeric() == True:
    gols = int(gols)
else:
    gols = 0
if nome !='' and gols != '':
    ficha(nome, int(gols))
elif nome == '':
    ficha(gl=gols)
