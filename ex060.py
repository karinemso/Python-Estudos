num = int(input('Digite um número e ache seu fatorial: '))
c = num
tempnum = num

while c != 1:
    c = c - 1
    fatorial =  tempnum * c
    tempnum = fatorial
   

print(f'O fatorial de {num} é igual a {fatorial}')

numfor = num
for k in range(numfor - 1, 1, -1):
    resultadofor = numfor * k
    numfor = resultadofor

print(f'O fatorial de {num} utilizando for é igual a {resultadofor}')