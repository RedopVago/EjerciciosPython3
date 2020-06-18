t = (1, 2.7, True, 'Hola')

# for element in t:
#     print(element)

for index, element in enumerate(t):
    print(index, ':', element)

    t[index] = index *10

    # print(index, ':', t[index])
