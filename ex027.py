name = str(input('Digite seu nome completo: '))
name_list = name.split()
fn = name_list[0]
ln = name_list[-1]

print('Muito prazer!')
print(f'Seu primeiro nome é {fn} e seu último nome é {ln}')