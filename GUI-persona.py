from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtCore import Slot
from formapersona import Ui_MainWindow

import pickle

from inforpersona import infoPersona


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.registros = []
        # self.ui.mostrar.hide()

        self.ui.Registro.clicked.connect(self.registrar)
        self.ui.mostrar.clicked.connect(self.mostrar_personas)
        self.ui.limpiar.clicked.connect(self.ui.cuadro.clear)

        self.ui.selectnombre.currentIndexChanged.connect(self.imprimir)
        self.ui.abrirB.clicked.connect(self.abrirarchivo)

    @Slot()
    def abrirarchivo(self):
        filename = QFileDialog.getOpenFileName(self, 'Arbir archivo', '.', 'Image Files(*.png)')
        file = open(filename[0], 'rb')

        count = 0
        size = 0

        f2 = open('copiaimg.png', 'wb')

        # for i in file:

        i = file.read(1000)

        while i:
            f2.write(i)

            print(f'[{count+1}:{len(i)}] {i}')
            count += 1

            size += len(i)
            i = file.read(1000)

        f2.close()
        file.close()

        print(f'img size: {size} bytes ({size/1024:.2f} kB)')

        # unpickler = pickle.Unpickler(file)

        # salir = False
        #
        # while not salir:
        #     try:
        #         ipr = unpickler.load()
        #         print(ipr)
        #         # self.ui.cuadro.setText(str(ipr))
        #     except EOFError:
        #         salir = True
        #
        # file.close()

        self.ui.nombrearchivoLE.setText(filename[0])

    @Slot()
    def imprimir(self):
        item = self.ui.selectnombre.currentText()
        print(item)

    @Slot()
    def registrar(self):
        tmp = infoPersona(self.ui.nombre.text(), self.ui.fecha.text(), self.ui.lugar.text())

        # self.registros.append(tmp)
        print(f'Persona registrada {tmp.Nombre()}')

        file = open('personas.txt', 'ab')
        pickle.dump(tmp, file)
        file.close()

        self.ui.nombre.clear()
        self.ui.fecha.clear()
        self.ui.lugar.clear()

        # self.ui.mostrar.show()

    @Slot()
    def mostrar_personas(self):
        self.ui.cuadro.clear()

        file = open('personas.txt', 'rb')
        unpickler = pickle.Unpickler(file)

        salir = False

        while not salir:
            try:
                ipr = unpickler.load()
                self.ui.cuadro.append(str(ipr) + '\n')
                self.ui.comboBox.addItem(ipr.Nombre())
            except EOFError:
                salir = True

        file.close()


if __name__ == '__main__':
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec_()
