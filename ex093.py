dados_jogador = dict()

dados_jogador['nome'] = str(input('Digite o nome do jogador: '))
dados_jogador['partidas'] = int(input('Quantas partidas ele jogou? '))

gols = []
for c in range(0, dados_jogador['partidas']):
    gol = int(input(f'Quantos gols ele fez na {c+1}° partida? '))
    gols.append(gol)

dados_jogador['gols'] = gols[:]
dados_jogador['total de gols'] = sum(gols[:])

print('-=-'*10)
for k, v in dados_jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=-'*10)

print(f'O jogador {dados_jogador["nome"]} jogou {dados_jogador["partidas"]} partidas')
for c, g in enumerate(gols):
    print(f'  =>Na partida {c+1}, fez {g} gols')
print(f'Totalizando {dados_jogador["total de gols"]} gols.')
