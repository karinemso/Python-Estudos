#Correspondente a aula 6 de Tipos primitivos e saída de dados
#type()
#n.isnumeric(), isalpha, isalnum, isupper

e = input('Digite algo: ')
tp = type(e)
size = len(e)
spc = e.isspace()
alfabetic = e.isalpha()
alfanumeric = e.isalnum()
upper = e.isupper()
lower = e.islower()
cap = e[0].isupper()
capconfirm = e.istitle()


print(f'O tipo é {tp}')
print(f'Tem {size} caracteres')
print(f'Só tem espaço? {spc} ')
print(f'É alfabetico? {alfabetic}')
print(f'É alfanumérico? {alfanumeric}')
print(f'Está em maiúsculas? {upper}')
print(f'Está em minúsculas? {lower}')
print(f'Está capitalizado? {cap}')
print(f'Está capitalizado mesmo? {capconfirm}') #esse é o certo
