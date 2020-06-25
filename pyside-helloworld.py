import sys
from PySide2.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel('Hola Mundo!')
label.show()
app.exec_()