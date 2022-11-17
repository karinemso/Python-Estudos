from time import sleep
from emoji import emojize

print('Se prepare para a contagem regressiva para o estouro de fogos!!')

for c in range (10,0, -1):
    print(c)
    sleep(1)

print('\033[0;31mBOOOM!\033[m')
print(emojize(':fireworks:'))