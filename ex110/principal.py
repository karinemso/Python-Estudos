from moeda import resume
valor = float(input('Digite um valor em reais: '))
aumenta = int(input('Quantos % você quer aumentar o seu valor? '))
diminui= int(input('Quantos % você quer diminuir o seu valor? '))

resume(valor,aumenta,diminui)
