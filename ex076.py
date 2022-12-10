tabela_precos = ('Sanduíche de Berinjela', 'R$10,00','Sanduíche de Frango veg', 'R$18,00', 'Suco Natural', 'R$5,00', 'Chocolate Vegano', 'R$10,00', 'Sorbet Veg', 'R$12,00')


print('-'*48)
print(f'{"LISTAGEM DE PREÇOS":^48}')
print('-'*48)
for c  in range(0, len(tabela_precos),2):
    print(f'{tabela_precos[c]:.<40}', f'{tabela_precos[c+1]:>5}')