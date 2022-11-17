totidade = 0
maisvelhonome = 0
maisvelhoidade = 0
menorde20 = 0
for c in range(1,5):
    print(f'-----{c}ª pessoa-----')
    nome = str(input('Digite um nome: '))
    idade = int(input('Digite uma idade: '))
    sexo =  str(input('Digite um sexo (F ou M): ')).upper()

    totidade += idade

    if c == 1 and sexo == 'M':
        maisvelhonome = nome
        maisvelhoidade = idade

    if idade > maisvelhoidade and sexo == 'M':
        maisvelhonome = nome
        maisvelhoidade = idade
    
    if sexo == 'F' and idade < 20:
        menorde20 += 1
    
   
    
  
mediaidade = totidade/4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho do grupo se chama {maisvelhonome.capitalize()} e tem {maisvelhoidade} anos')
print(f'{menorde20} mulher(es) tem menos de 20 anos')