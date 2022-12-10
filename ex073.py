ranking = ('Palmeiras',
'Internacional',
'Fluminense',
'Corinthias',
'Flamengo',
'Athletico-PR',
'Atlético-MG',
'Fortaleza',
'São Paulo',
'América-MG',
'Botafogo',
'Santos',
'Goiás',
'Bragantino',
'Coritiba',
'Cuiába',
'Ceará-SC',
'Atlético-GO',
'Avaí',
'Juventude'
)
c = 0
for elemento in ranking:
    c+=1
    if elemento == 'Avaí':
        position = c
print(f'Os 5 primeiros colocados do Brasileirão são: {ranking[:5]}')
print(f'Os 4 últimos colocados do Brasileirão são: {ranking[16:]}')
print(f'Os colocados do Brasileirão em ordem alfabética são: {sorted(ranking)}')
print(f'O Ceará está na posição {position}')
