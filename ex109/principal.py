import moeda

valor = float(input('Digite um valor em reais: '))
print(f'O valor {moeda.moeda(valor)} aumentado em 10% é igual a {(moeda.aumentar(valor,True))}')
print(f'A metade de {moeda.moeda(valor)} é igual a {(moeda.metade(valor,True))}')
