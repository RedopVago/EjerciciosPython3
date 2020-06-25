from PySide2.QtWidgets import QApplication, QPushButton, QVBoxLayout, QMainWindow


app = QApplication([])

window = QMainWindow()
layout = QVBoxLayout()

for i in range(5):
    boton = QPushButton(f'Boton {i+1}!')
    boton.show()
    layout.addWidget(boton)

window.setLayout(layout)

window.show()

app.exec_()