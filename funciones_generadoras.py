def consecutivos():
    n = 0
    while True:
        print(n)
        n += 1


def consecutivos_generador():
    i = 0
    while True:
        yield i
        i += 1


lc = [i for i in range(100)]
eg = (i for i in consecutivos_generador())
eg2 = (j for j in consecutivos_generador())

print(eg)
print(eg2)

# for e in eg:
#     print(e)
