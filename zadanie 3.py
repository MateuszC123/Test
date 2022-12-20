def dodl(a, b, c):
    lista = []
    i = a
    while i <= b:
        lista.append(i)
        i += c
    return lista
print(dodl(2,10,2))