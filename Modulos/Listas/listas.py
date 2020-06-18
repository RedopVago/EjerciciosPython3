
# for element in l:
#     print(element)

# for i in range(4):
#     print(i, ':', l[i])

def printLIst(list):
    for i, l in enumerate(list):
        print(i, ':', l)


if __name__ == '__main__':
    # l = [1, 2.7, True, 'Hola']
    #
    # print(l)
    # l.append(5)
    # print(l)
    #
    # r = l.pop()
    # print(r)
    #
    # print(l)
    # print(l.pop(1))
    # print(l)

    lista1 = [1, 2, 3, 4, 5]

    lista2 = lista1[-2:-5:-1]

    print(lista2)

    lista3 = []
    for r in reversed(lista1):
        lista3.append(r)

    print(lista3)

