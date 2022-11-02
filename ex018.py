from math import sin, cos, tan, degrees,radians

angle = int(input('Digite o número de um ângulo: '))
sen = sin(radians(angle))
cosen = cos(radians(angle))
tg = tan(radians(angle))

print(f'O seno de {angle} é {sen:.2f}')
print(f'O cosseno de {angle} é {cosen:.2f}')
print(f'A tangente de {angle} é {tg:.2f}')

#Esse é o que mais tive dificuldade até agora, pois não me atentei na corversão para radianos