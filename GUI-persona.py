
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot
from formapersona import Ui_MainWindow

from inforpersona import infoPersona

import time


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.registros = []

        self.ui.Registro.clicked.connect(self.registrar)
        self.ui.mostrar.clicked.connect(self.mostrar_personas)


    @Slot()
    def registrar(self):
        tmp = infoPersona(self.ui.nombre.text(), self.ui.fecha.text(), self.ui.lugar.text())

        self.registros.append(tmp)
        print(tmp)

    @Slot()
    def mostrar_personas(self):
        for i in self.registros:
            print(i)


if __name__ == '__main__':
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec_()