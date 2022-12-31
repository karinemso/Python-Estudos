from utilidadesCeV  import moeda
from utilidadesCeV import dado


valor = dado.leiaDinheiro('Digite um valor em reais: R$')
aumenta = dado.leiaInt('Quantos % você quer aumentar o seu valor? ')
diminui= dado.leiaInt('Quantos % você quer diminuir o seu valor? ')
myfloat = dado.leiaFloat('Digite um número do tipo float:')
print(f'Meu número do tipo float foi {myfloat:.2f}')


moeda.resume(valor,aumenta,diminui)

