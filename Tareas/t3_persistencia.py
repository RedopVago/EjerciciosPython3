from Ejercicios.e3_poo import Estudiante
from Tareas.StudenIO import EstudiantesPickle, EstudiantesShelve

if __name__ == '__main__':

    # p = EstudiantesPickle()

    e1 = Estudiante('Pedro Valenzuela', 'juan.valenzuela@cinvestav.mx', 'PeVal')
    e2 = Estudiante('Roberto Hernandez', 'roberto@hdez.com', 'RoHer')
    e3 = Estudiante('Jose Jimenez', 'jose.jimenez@gmail.com', 'JoJim')
    e4 = Estudiante('Pablo Fernandez', 'pfernandez@hotmail.com', 'PaFer')
    e5 = Estudiante('Adrian Muñiz', 'adrianmuniz@yahoo.com.mx', 'AdMun')

    estudiantes = [e1, e2, e3, e4, e5]

    # for e in estudiantes:
    #     p.guardar(e)
    #     print(f'{e.nombre()} guardado')
    #
    # lt = p.leerTodos()
    # for l in lt:
    #     print(l)
    #
    # l = p.leer('Pedro Valenzuela')
    # print(f'estudiante: {l}')
    #
    # if p.actualizar('Juan Godoy', nombre='Pedro Valenzuela'):
    #     print(f'Estudiante Actualizado')
    # else:
    #     print('El estudiante no esta en la base de datos')
    #
    # lt = p.leerTodos()
    # for l in lt:
    #     print(l)

    s = EstudiantesShelve()

    # for e in estudiantes:
    #     s.guardar(e)
    #     print(f'{e.nombre()} guardado')

    # lt = s.leerTodos()
    # for l in lt:
    #     print(l)

    # e = s.leer('Pedro Valenzuela')
    # print(f'Estudiante: {e}')

    if s.actualizar('Pedro Valenzuela', nombre='Juan Godoy'):
        print(f'Estudiante Actualizado')
    else:
        print('El estudiante no esta en la base de datos')