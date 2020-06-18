d = {}

d['uno']= 1
d[True] = 0
d[False] = 1
d[10] = False

# print(d)
# print(d['uno'])
# print(d[True])
# print(d[False])
# print(d[10])

enum = {'uno': 'Juan', True: 'Pedro'}

for i in enum:
    print(i, ':', enum[i])
