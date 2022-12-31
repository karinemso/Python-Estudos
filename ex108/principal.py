import moeda

valor = float(input('Digite um valor em reais: '))
print(f'O valor {moeda.moeda(valor)} aumentado em 10% é igual a {moeda.moeda(moeda.aumentar(valor))}')
print(f'A metade de {moeda.moeda(valor)} é igual a {moeda.moeda(moeda.metade(valor))}')
