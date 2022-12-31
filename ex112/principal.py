from utilidadesCeV  import moeda
from utilidadesCeV import dado


valor = dado.leiaDinheiro('Digite um valor em reais: R$')
aumenta = int(input('Quantos % você quer aumentar o seu valor? '))
diminui= int(input('Quantos % você quer diminuir o seu valor? '))

moeda.resume(valor,aumenta,diminui)

