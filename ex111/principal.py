from utilidadesCeV  import moeda


valor = float(input('Digite um valor em reais: '))
aumenta = int(input('Quantos % você quer aumentar o seu valor? '))
diminui= int(input('Quantos % você quer diminuir o seu valor? '))

moeda.resume(valor,aumenta,diminui)
