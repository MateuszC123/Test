import random
k = []
i = 0
while i < 5:
    x = [random.randint(-5, 10)]
    k.append(x)
    i += 1

print(k)
suma = 0
for l in k:
    if k[l] > 0:
        suma += k[l]
print(suma)















