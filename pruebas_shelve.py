
import shelve

class infoPersona():
    __nombre = ''
    __fechaNacimiento = None
    __lugarNacimiento = ''

    def __init__(self, n, fn, ln, t=None):
        self.__nombre = n
        # datetime.datetime.date(1985, 11, 4)
        self.__fechaNacimiento = fn
        self.__lugarNacimiento = ln
        self.__telefono = False

    def nombre(self):
        return self.__nombre

    def fechaNacimiento(self):
        return self.__fechaNacimiento

    def obtenerLN(self):
        return self.__lugarNacimiento

    def telefono(self):
        return self.__telefono

    def __str__(self):
        return f'Nombre: {self.__nombre}\n' \
               f'Fecha de Nacimient: {self.__fechaNacimiento}\n' \
               f'Lugar de Naciemiento: {self.__lugarNacimiento}'


nombres = ['ana', 'maria', 'jose']
fechas = ['2000/02/23', '1952/08/12', '1997/12/07']
lugares = ['Jalisco', 'Colima', 'Nayarit']
telefonos = []


with shelve.open('personas_shelve') as shelf:
    for n, f, l in zip(nombres, fechas, lugares):
        ip = infoPersona(n, f, l)
        shelf[n] = ip

    ll = [k for k in shelf]
    print(ll)

# Referencia para Tarea 3
# def saveStudentP(student):
#     pass
#
# def saveStudentS(student):
#     pass
#
# def readstudenP(nombre, apellido):
#     pass
#
# def readStudenS(nombre, apellido):
#     pass
#
# def updateStudentP(nombre, apellido):
#     pass
#
# def updateStudentS(nombre, apellido):
#     pass