from mongoengine import *

# Cnexion a direccion y puerto default
connect('estudiantes')

class Estudiante(Document):
    nombre = StringField(required=True)
    correo = StringField(required=True)
    contrasena = StringField(required=True)

    def __str__(self):
        return f'id: {self.id}\n' \
               f'Nombre: {self.nombre}\n' \
               f'Correo: {self.correo}\n' \
               f'------------------------------' \
               f'------------------------------'

class EstudiantesMongoengine:
    def __init__(self):
        pass

    def guardar(self, estudiante):
        estudiante.save()
        estudiante.reload()

        return estudiante.id

    def leer(self, nombreEstudiante):
        e = Estudiante.objects(nombre=nombreEstudiante)
        return e

    def leerTodos(self):
        return Estudiante.objects

    def actualizar(self, nombreEstudiante, nombre=None, correo=None, contrasena=None):

        e = Estudiante.objects(nombre=nombreEstudiante)
        print(f'{e}')

        if len(e) > 0:
            e = e[0]
        else:
            print(f'[ERROR] El estudiante no esta en la base de datos')
            return False

        update_dict = {}

        if nombre:
            update_dict['nombre'] = nombre

        if correo:
            update_dict['correo'] = correo

        if contrasena:
            update_dict['contrasena'] = contrasena

        e.update(**update_dict)

        e.reload()
        print(f'{e}')

        return e

    def eliminar(self, idestudiante):
        d = Estudiante.objects(id=idestudiante).delete()
        return True if d else False


if __name__ == '__main__':

    e1 = Estudiante(nombre='Pedro Valenzuela', correo='juan.valenzuela@cinvestav.mx', contrasena='PeVal')
    e2 = Estudiante(nombre='Roberto Hernandez', correo='roberto@hdez.com', contrasena='RoHer')
    e3 = Estudiante(nombre='Jose Jimenez', correo='jose.jimenez@gmail.com', contrasena='JoJim')
    e4 = Estudiante(nombre='Pablo Fernandez', correo='pfernandez@hotmail.com', contrasena='PaFer')
    e5 = Estudiante(nombre='Adrian Muñiz', correo='adrianmuniz@yahoo.com.mx', contrasena='AdMun')

    estudiantes = [e1, e2, e3, e4, e5]

    me = EstudiantesMongoengine()

    # for e in estudiantes:
    #     me.guardar(e)

    # es = me.leerTodos()
    # for e in es:
    #     print(f'{e}')

    # e = me.leer('Pedro Valenzuela')
    # print(f'{e}')

    # me.actualizar('Pedro Valenzuela', nombre='Juan Godoy', correo='pedro@cinvestav.mx', contrasena='JuGod')
    # me.actualizar('Juan Godoy', nombre='Pedro Valenzuela', correo='juan.valenzuela@cinvestav.mx', contrasena='PeVal')

    me.actualizar('Pedro Valenzuela', contrasena='PeVal')
    # me.actualizar('Juan Godoy', nombre='Pedro Valenzuela', correo='juan.valenzuela@cinvestav.mx', contrasena='PeVal')
