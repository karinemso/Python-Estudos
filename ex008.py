m = float(input('Digite uma distância em metros: '))
km = m/1000
hm = m/100
dam  = m/10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'A medida de {m}m corresponde a: ')
print(f'{km}km ')
print(f'{hm}hm ')
print(f'{dam}dam')
print(f'{dm:.0f}dm ')
print(f'{cm:.0f}cm ')
print(f'{mm:.0f}mm')
