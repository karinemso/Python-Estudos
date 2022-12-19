jogadores = []
jogador = dict()
gols = []

while True:
    jogador.clear()
    jogador['nome']= str(input('Digite o nome do jogador: '))
    jogador['partidas'] = int(input('Quantas partidas esse jogador jogou?'))
    if jogador['partidas'] != 0:
        for c in range (0, jogador['partidas']):
            gol = int(input(f'Quantos gols {jogador["nome"]} fez na {c+1}° partida? '))
            gols.append(gol)
        jogador['gols'] = gols[:]
        jogador['total'] = sum(gols[:])
        gols.clear()
    jogadores.append(jogador.copy())
    op = str(input('Deseja continuar cadastrando jogadores?[S/N] ')).upper()
    while op not in 'SN':
        op = str(input('Deseja continuar cadastrando jogadores?[S/N] ')).upper()
    if op == 'N':
        break

print('-=-'*30)
print("Cod.",  end='')
for k in jogador.keys():
    print(f'{k:<14} ', end='')
print()
print('-=-'*30)

for c, j in enumerate(jogadores):
    print(f'{c:<5}', end='')
    for v in j.values():
        print(f'{str(v):<15}', end = '')
    print()
    print('---'*30)
    
while True:
    consult = int(input('Digite o código do jogador para ver sua análise individual:'))
    while consult > len(jogadores):
        consult = int(input('Digite um código válido para ver a análise individual do jogador:'))
    if consult <= len(jogadores):
        print('-=-'*30)
        print("Cod.",  end='')
        for k in jogador.keys():
            print(f'{k:<14} ', end='')
        print()
        print('-=-'*30)
        print(f'{consult:>4}', f'{jogadores[consult]["nome"]:<15}', f'{jogadores[consult]["partidas"]:<15}',f'{str(jogadores[consult]["gols"]):<15}', f'{jogadores[consult]["total"]:<15}')
        print('-=-'*30)
        print(f'Levantamento do jogador {jogadores[consult]["nome"]}')
        for c, g in enumerate(jogadores[consult]['gols']):
            print(f' => No jogo n°{c+1} ele fez {g} gols')
        print(f'Totalizando {jogadores[consult]["total"]}')
    op = str(input('Deseja continuar visualizando jogadores?[S/N] ')).upper()
    while op not in 'SN':
        op = str(input('Deseja continuar visualizando jogadores?[S/N] ')).upper()
    if op == 'N':
        break

 
print('Programa encerrado!')

