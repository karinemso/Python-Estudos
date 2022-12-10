'''nums = []

Precisamos ordenar os números
Minha primeira ideia é colocar o max e o min nos seus devidos lugares.
Nos restam 3 números para posicionar
min min2 media max2 max 1
min2 é maior que o min e menor que a media
media é maior que min1 e min 2 e menor que max 1 e max 2
max2 é maior que a media e menor que max 1



for c in range(0,5):
    num = int(input('Digite  um número: '))
    nums.append(num)

   
max1 = max(nums)
min1 = min(nums)    
c = 0
media = 0
for n in nums:
    if min1 < n < max1 and c == 0:
        media = n
    if n == media:
        media = n
    if n < media and n > min1:
        min2 = n
    if n > media and n < max1:
        max2=n
    c+=1
  

print(nums)
print(min1, min2, media, max2, max1)
'''
#Ainda pensando na solução