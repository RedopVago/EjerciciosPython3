try:
    import cPickle as pickle
except ImportError:
    import pickle

import datetime

class infoPersona():
    __nombre = ''
    __fechaNacimiento = None
    __lugarNacimiento = ''

    def __init__(self, n, fn, ln):
        self.__nombre = n
        # datetime.datetime.date(1985, 11, 4)
        self.__fechaNacimiento = fn
        self.__lugarNacimiento = ln

    def Nombre(self):
        return self.__nombre

    def FechaNacimiento(self):
        return self.__fechaNacimiento

    def obtenerLN(self):
        return self.__lugarNacimiento

    def __str__(self):
        return f'Nombre: {self.__nombre}\n' \
               f'Fecha de Nacimient: {self.__fechaNacimiento}\n' \
               f'Lugar de Naciemiento: {self.__lugarNacimiento}'

nombres = ['ana', 'maria', 'jose']
fechas = ['2000/02/23', '1952/08/12', '1997/12/07']
lugares = ['Jalisco', 'Colima', 'Nayarit']

ips = []
# n, f, l = (nombre, fecha, lugar)
for n, f, l in zip(nombres, fechas, lugares):
    ips.append(infoPersona(n, f, l))

for i in ips:
    print(i)

# file = open('clase3.txt', 'wb')
# pickle.Pickler(file, 4).dump(ips)

# s representa un stream de bytes
bin = pickle.dumps(ips)
print(bin)

# file = open('p4.txt', 'wb')
# personas = ['juan', 'maria', 'ana']
# pickle.dump(personas, file)
# file.close()

# file = open('clase2.txt', 'rb')
# unpickler = pickle.Unpickler(file)
# ipr = unpickler.load()
# file.close()
#
# print(ipr)
# print(type(ipr))
