import requests
from time import sleep

print('Tentando conectar com o site Pudim!')
sleep(1)
try:
    on = requests.get("http://pudim.com.br/")
except Exception as e:
    print(f'\033[31mFora do ar! Erro {e.__class__}\033[m')
else:
    print('\033[32mConsegui conectar!\033[m')
finally:
    print('Volte sempre!')
