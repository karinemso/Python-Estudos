import moeda

valor = float(input('Digite um valor em reais: '))
print(f'O valor R${valor} aumentado em 10% é igual a R${moeda.aumentar(valor)}')
print(f'A metade de R${valor} é igual a R${moeda.metade(valor)}')