lista = []

for i in range(11):
    if i % 2 == 0:
        print(f'se agrego {i} a la lista')
        lista.append(i)

print(lista)

lista2 = [i for i in range(11) if i % 2 == 0]  # Pythonic way
print(lista2)
print(type(lista))

iter1 = iter(lista2)
print(iter1)

for ii in lista2:
    print(ii*2)

















# list = []
#
# for i in range(11):
#     if i % 2 == 0:
#         list.append(i)
#
# print(list)
#
# list = [i for i in range(11) if i % 2 == 0]
# print(list)

