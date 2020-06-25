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
        MainWindow.resize(185, 182)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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


        self.verticalLayout_2.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Registro = QPushButton(self.centralwidget)
        self.Registro.setObjectName(u"Registro")

        self.horizontalLayout_2.addWidget(self.Registro)

        self.mostrar = QPushButton(self.centralwidget)
        self.mostrar.setObjectName(u"mostrar")

        self.horizontalLayout_2.addWidget(self.mostrar)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 185, 21))
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
        self.Registro.setText(QCoreApplication.translate("MainWindow", u"Resgistrar", None))
        self.mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
    # retranslateUi

