tot = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        tot+= c
        print(tot)
print(tot)