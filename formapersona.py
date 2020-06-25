# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formapersona.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(437, 466)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nombre = QLineEdit(self.centralwidget)
        self.nombre.setObjectName(u"nombre")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nombre)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.fecha = QLineEdit(self.centralwidget)
        self.fecha.setObjectName(u"fecha")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.fecha)

        self.lugar = QLineEdit(self.centralwidget)
        self.lugar.setObjectName(u"lugar")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lugar)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Registro = QPushButton(self.centralwidget)
        self.Registro.setObjectName(u"Registro")

        self.horizontalLayout_2.addWidget(self.Registro)

        self.mostrar = QPushButton(self.centralwidget)
        self.mostrar.setObjectName(u"mostrar")

        self.horizontalLayout_2.addWidget(self.mostrar)

        self.limpiar = QPushButton(self.centralwidget)
        self.limpiar.setObjectName(u"limpiar")

        self.horizontalLayout_2.addWidget(self.limpiar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.cuadro = QTextEdit(self.centralwidget)
        self.cuadro.setObjectName(u"cuadro")

        self.verticalLayout.addWidget(self.cuadro)

        self.selectnombre = QComboBox(self.centralwidget)
        self.selectnombre.addItem("")
        self.selectnombre.setObjectName(u"selectnombre")

        self.verticalLayout.addWidget(self.selectnombre)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.abrirB = QPushButton(self.centralwidget)
        self.abrirB.setObjectName(u"abrirB")

        self.horizontalLayout.addWidget(self.abrirB)

        self.nombrearchivoLE = QLineEdit(self.centralwidget)
        self.nombrearchivoLE.setObjectName(u"nombrearchivoLE")

        self.horizontalLayout.addWidget(self.nombrearchivoLE)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 437, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Lugar", None))
        self.Registro.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.selectnombre.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecciona nombre", None))

        self.abrirB.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
    # retranslateUi

