
class MiClase():
    _attr1 = ''
    _attr2 = ''

    def __init__(self, string, number):
        self._attr1 = string
        self._attr2 = number

    def mostrarString(self):
        print('string:', self._attr1)

    def mostrarNumero(self):
        print('numero:', self._attr2)



class vehiculo():
    __numero_llantas = 0
    __numero_pasajeros = 0

    def acelerar(self):
        pass

    def frenar(selfself):
        pass

    def encenderLuces(self):
        pass

    def cuantasLlantas(self):
        return self.__numero_llantas


class motocicleta(vehiculo):
    def __init__(self):
        self.__numero_llantas = 5


class camioneta(vehiculo):
    __espacio = 0

    def __init__(self):
        self.__numero_llantas = 4
        self.__espacio = '90 cm3'

    def mostarEspacio(self):
        return self.__espacio


class animal():
    numero_patas = 0

    def comer(self):
        pass

    def andar(self):
        pass

class casa():
    __cuartos = 0
    __pisos = 1

    def definirCuartos(self, cuartos):
        self.cuartos = cuartos


class division():
    divisor = 0
    dividendo = 0
    resultado = 0
    residuo = 0

    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor

    def dividir(self):
        print('Clase Base')


class divisionEntera(division):
    def __init__(self, dividendo, divisor):
        super().__init__(dividendo, divisor)
        pass

    def dividir(self):
        return (self.dividendo // self.divisor,
                self.dividendo % self.divisor)


class divisionDecimal(division):
    def __init__(self, dividendo, divisor):
        super().__init__(dividendo, divisor)

    def dividir(self):
        return self.dividendo / self.divisor

if __name__ == '__main__':
    # miclase = MiClase('Hola!', 9)
    #
    # print(miclase.)

    # m = motocicleta()
    #
    #
    # c = camioneta()
    # c.mostarEspacio()

    de = divisionEntera(9, 2)
    resultado, residuo = de.dividir()
    print(f'resultado: {resultado}\nresiduo: {residuo}')

    dd = divisionDecimal(9, 2)
    res = dd.dividir()
    print(f'resultado: {res}')
