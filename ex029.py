
vel = int(input('Qual a velocidade atual do carro? '))
limite = 80

multa = (float((vel - limite)) * 7)
if vel <= limite:
    print('Você está na velocidade correta da via! Dirija com segurança e tenha um bom dia!')
else:
    print(f'MULTADO! Você excedeu o limite da velocidade da via({limite}Km/h)\n Sua multa é de R${multa:.2f}!' )
