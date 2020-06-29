import pickle
import shelve


class EstudiantesPickle:

    fn = None

    def __init__(self, filename='estudiantes_pickle.db'):
        self.fn = filename

    def guardar(self, estudiante):
        """Este método no valida si existe un estudiante con los mismos datos"""
        with open(self.fn, 'ab') as fa:
            pickle.dump(estudiante, fa)

    def leer(self, nombreEstudiante):
        estudiantes = self.leerTodos()

        estudiante = None

        for e in estudiantes:
            if e.nombre() == nombreEstudiante:
                estudiante = e
                break

        if estudiante:
            return estudiante
        else:
            return -1

    def leerTodos(self):

        estudiantes = []

        with open(self.fn, 'rb') as fr:

            try:
                while True:
                    unpickler = pickle.Unpickler(fr)
                    tmp = unpickler.load()
                    estudiantes.append(tmp)
            except EOFError:
                pass

        if estudiantes:
            return estudiantes
        else:
            return -1

    def actualizar(self, nombreEstudiante, nombre=None, correo=None, contrasena=None):
        estudiantes = self.leerTodos()
        actualizado = False

        for e in estudiantes:
            if e.nombre() == nombreEstudiante:
                print(e)

                e.actualizarNombre(nombre)
                e.actualizarCorreo(correo)
                e.actualizarContrasena(contrasena)
                print(e)

                with open(self.fn, 'wb') as fw:
                    for i in estudiantes:
                        self.guardar(i)

                actualizado = True
                break

        return actualizado


class EstudiantesShelve:
    shelf = None
    count = 0

    def __init__(self, filename='estudiantes_shelve'):
        self.shelf = shelve.open(filename)
        for s in self.shelf.keys():
            if int(s) > self.count:
                self.count = int(s)

    def __del__(self):
        if self.shelf:
            self.shelf.close()

    def guardar(self, estudiante):
        self.count += 1
        self.shelf[str(self.count)] = estudiante

    def leer(self, nombreEstudiante):

        for k in self.shelf:
            if self.shelf[k].nombre() == nombreEstudiante:
                return self.shelf[k]

        return -1

    def leerTodos(self):
        es = [self.shelf[k] for k in self.shelf]
        if es:
            return es
        else:
            return [-1]

    def actualizar(self, nombreEstudiante, nombre=None, correo=None, contrasena=None):

        for k in self.shelf:
            if self.shelf[k].nombre() == nombreEstudiante:
                self.shelf[k].actualizarNombre(nombre)
                self.shelf[k].actualizarCorreo(correo)
                self.shelf[k].actualizarContrasena(contrasena)

                return True

        return False
