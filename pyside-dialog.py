import sys
from PySide2.QtWidgets import QApplication, QVBoxLayout, QDialog, QLineEdit, QPushButton

class Forma(QDialog):
    def __init__(self, parent=None):
        super(Forma, self).__init__(parent)
        self.setWindowTitle('Mi Dialogo')

        self.edit = QLineEdit()
        self.edit.setPlaceholderText('Escribe tu nombre')
        self.boton = QPushButton('Saluda!')

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.boton)

        self.setLayout(layout)

        self.boton.clicked.connect(self.saludar)

    def saludar(self):
        print(f'Hola {self.edit.text()}')

if __name__ == '__main__':
    app = QApplication()
    forma = Forma()
    forma.show()

    sys.exit(app.exec_())