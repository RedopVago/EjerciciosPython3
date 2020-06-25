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
               f'Fecha de Nacimiento: {self.__fechaNacimiento}\n' \
               f'Lugar de Naciemiento: {self.__lugarNacimiento}'