from Tareas.ui_t5 import Ui_MainWindow

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot

from Tareas.t4_database_mongoengine import Estudiante, EstudiantesMongoengine as db

import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = db()

        self.ui.guardarB.clicked.connect(self.guardar)
        self.ui.buscarB.clicked.connect(self.buscar)
        self.ui.leertodosB.clicked.connect(self.mostarTodos)
        self.ui.actualizarB.clicked.connect(self.actualizar)
        self.ui.limpiarB.clicked.connect(self.ui.log.clear)
        self.ui.eliminarB.clicked.connect(self.eliminar)

    @Slot()
    def guardar(self):
        estudiante = {
            'nombre': self.ui.guardarnombre.text(),
            'correo': self.ui.guardarcorreo.text(),
            'contrasena': self.ui.guardarcontra.text()
        }

        e = Estudiante(**estudiante)
        estudiante_id = self.db.guardar(e)
        self.ui.log.append(f'GUARDADO estudiante con id {estudiante_id}\n')
        self.ui.log.append(str(e))

        self.ui.guardarnombre.clear()
        self.ui.guardarcorreo.clear()
        self.ui.guardarcontra.clear()

    @Slot()
    def buscar(self):
        bn = self.ui.buscarnombre.text()
        self.ui.log.append('Estudiantes encontrados:')
        for l in self.db.leer(bn):
            self.ui.log.append(str(l))

    @Slot()
    def mostarTodos(self):
        lt = self.db.leerTodos()

        text = 'MOSTRANDO TODOS LOS ESTUDIANTES\n' \
               f'------------------------------' \
               f'------------------------------'

        self.ui.log.append(text)

        for l in lt:
            self.ui.log.append(str(l))

        text = f'------------------------------' \
               f'------------------------------'

        self.ui.log.append(text)

    @Slot()
    def actualizar(self):
        buscar = self.ui.buscarnombre.text()

        act = {}

        nombre = self.ui.actualizarnombre.text()
        correo = self.ui.actualizarcorreo.text()
        contra = self.ui.actualizarcontrasena.text()

        if nombre:
            act['nombre'] = nombre

        if correo:
            act['correo'] = correo

        if contra:
            act['contrasena'] = contra

        res = db.actualizar(buscar, **act)
        self.ui.log.append(f'Estudiante actualizado {res}')

    @Slot()
    def eliminar(self):
        eid = self.ui.estudianteid.text()
        if self.db.eliminar(eid):
            self.ui.log.append(f'ELIMINADO estudiante con id {eid}')
        else:
            self.ui.log.append(f'No se econtreo estudiante con id: {eid}')

        text = f'------------------------------' \
               f'------------------------------'

        self.ui.log.append(text)


if __name__ == '__main__':
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
