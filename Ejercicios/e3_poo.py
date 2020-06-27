## Herencia y polimorfismo
class Figura():
    _base = 0
    _altura = 0

    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    def area(self):
        return self._base * self._altura

    def perimetro(self):
        pass


class rectangulo(Figura):

    def __init__(self, base, altura):
        super(rectangulo, self).__init__(base=base, altura=altura)
        print(f'rectangulo:\n\tbase: {self._base}\n\taltura: {self._altura}')

    def perimetro(self):
        return self._base * 2 + self._altura * 2


class triangulo(Figura):
    """ Asumiendo un triangulo rectangulo"""
    def __init__(self, base, altura):
        super(triangulo, self).__init__(base=base, altura=altura)

        self.hipo = (self._base ** 2 + self._altura ** 2) ** (1 / 2)

        print(f'trinagulo:\n\tbase: {self._base}\n\taltura: {self._altura}\n\thipotenuza: {self.hipo}')

    def area(self):
        return super().area() / 2

    def perimetro(self):
        return self.hipo + self._base + self._altura


## Encapsulacion
class Estudiante:
    _nombre = ''
    _correo = ''
    _contrasena = ''

    def __init__(self, nombre, correo, contrasena):
        self._nombre = nombre
        self._correo = correo
        self._contrasena = contrasena

    def nombre(self):
        self._nombre

    def correo(self):
        self._correo

    def contrasena(self):
        self._contrasena

    def actualizarNombre(self, nombre):
        self._nombre = nombre

    def actualizarCorreo(self, correo):
        self._correo = correo

    def actualizarContrasena(self, contrasena):
        self._contrasena = contrasena


if __name__ == '__main__':
    t = triangulo(3, 4)
    print(f'area triangulo: {t.area()}')
    print(f'perimetro triangulo: {t.perimetro()}')

    print('')

    r = rectangulo(3, 4)
    print(f'area triangulo: {r.area()}')
    print(f'perimetro triangulo: {r.perimetro()}')
