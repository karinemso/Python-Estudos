largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

área = largura * altura
litro = área/2

print(f'Sua parede tem a dimensão de {largura}X{altura} e sua área é de {área}m²')
print(f'Para pintá-la você irá precisar de {litro}l de tinta')