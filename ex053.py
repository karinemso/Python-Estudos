word = str(input('Digite uma palavra e cheque se é um palíndromo: ')).upper().strip()

words = word.split()
junto = ''.join(words)
invertido = ''

#[A, K, A, R, I, N, E]

for c in range ((len(junto)-1),-1, -1):
    invertido+= junto[c]



print(f'A palavra {junto} ao contrário é {invertido}')
if invertido == junto:
    print('Por isso é um Palíndromo')
else:
    print('Por isso não é um palíndromo')
   








