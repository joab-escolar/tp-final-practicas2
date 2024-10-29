# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cliente_create.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_ClienteIterableWindow(object):
    def setupUi(self, ClienteIterableWindow):
        if not ClienteIterableWindow.objectName():
            ClienteIterableWindow.setObjectName(u"ClienteIterableWindow")
        ClienteIterableWindow.resize(1000, 800)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Computer))
        ClienteIterableWindow.setWindowIcon(icon)
        ClienteIterableWindow.setStyleSheet(u"background-color: rgb(17, 51, 83);")
        self.centralwidget = QWidget(ClienteIterableWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 131, 31))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.lbl_show_user = QLabel(self.centralwidget)
        self.lbl_show_user.setObjectName(u"lbl_show_user")
        self.lbl_show_user.setGeometry(QRect(130, 10, 451, 31))
        self.lbl_show_user.setFont(font)
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(860, 20, 111, 41))
        self.btn_back.setStyleSheet(u"background-color: rgb(39, 39, 39)")
        self.input_nombre = QLineEdit(self.centralwidget)
        self.input_nombre.setObjectName(u"input_nombre")
        self.input_nombre.setGeometry(QRect(330, 210, 171, 31))
        self.input_nombre.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_create = QPushButton(self.centralwidget)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setGeometry(QRect(330, 460, 351, 31))
        self.btn_create.setStyleSheet(u"background-color: rgb(11, 3, 255);\n"
"selection-background-color: rgb(138, 138, 138);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 190, 111, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(520, 190, 111, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 250, 111, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(520, 250, 111, 16))
        self.input_apellido = QLineEdit(self.centralwidget)
        self.input_apellido.setObjectName(u"input_apellido")
        self.input_apellido.setGeometry(QRect(510, 210, 171, 31))
        self.input_apellido.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(340, 310, 111, 16))
        self.input_dni = QLineEdit(self.centralwidget)
        self.input_dni.setObjectName(u"input_dni")
        self.input_dni.setGeometry(QRect(330, 270, 171, 31))
        self.input_dni.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(520, 310, 111, 16))
        self.input_direccion = QLineEdit(self.centralwidget)
        self.input_direccion.setObjectName(u"input_direccion")
        self.input_direccion.setGeometry(QRect(330, 330, 171, 31))
        self.input_direccion.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.input_telefono = QLineEdit(self.centralwidget)
        self.input_telefono.setObjectName(u"input_telefono")
        self.input_telefono.setGeometry(QRect(510, 330, 171, 31))
        self.input_telefono.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(340, 370, 111, 16))
        self.btn_activo = QRadioButton(self.centralwidget)
        self.btn_activo.setObjectName(u"btn_activo")
        self.btn_activo.setGeometry(QRect(330, 400, 89, 20))
        self.btn_inactivo = QRadioButton(self.centralwidget)
        self.btn_inactivo.setObjectName(u"btn_inactivo")
        self.btn_inactivo.setGeometry(QRect(410, 400, 89, 20))
        self.input_fechaN = QDateTimeEdit(self.centralwidget)
        self.input_fechaN.setObjectName(u"input_fechaN")
        self.input_fechaN.setGeometry(QRect(510, 270, 171, 31))
        self.input_fechaN.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        ClienteIterableWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ClienteIterableWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        ClienteIterableWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ClienteIterableWindow)
        self.statusbar.setObjectName(u"statusbar")
        ClienteIterableWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ClienteIterableWindow)

        QMetaObject.connectSlotsByName(ClienteIterableWindow)
    # setupUi

    def retranslateUi(self, ClienteIterableWindow):
        ClienteIterableWindow.setWindowTitle(QCoreApplication.translate("ClienteIterableWindow", u"BANCO", None))
        self.label.setText(QCoreApplication.translate("ClienteIterableWindow", u"CLIENTES-", None))
        self.lbl_show_user.setText("")
        self.btn_back.setText(QCoreApplication.translate("ClienteIterableWindow", u"Atras", None))
        self.btn_create.setText(QCoreApplication.translate("ClienteIterableWindow", u"Crear", None))
        self.label_2.setText(QCoreApplication.translate("ClienteIterableWindow", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("ClienteIterableWindow", u"Apellido", None))
        self.label_4.setText(QCoreApplication.translate("ClienteIterableWindow", u"DNI", None))
        self.label_5.setText(QCoreApplication.translate("ClienteIterableWindow", u"Fecha Nacimiento", None))
        self.label_6.setText(QCoreApplication.translate("ClienteIterableWindow", u"Direccion", None))
        self.label_7.setText(QCoreApplication.translate("ClienteIterableWindow", u"Numero Telefono", None))
        self.label_8.setText(QCoreApplication.translate("ClienteIterableWindow", u"Estado", None))
        self.btn_activo.setText(QCoreApplication.translate("ClienteIterableWindow", u"Activo", None))
        self.btn_inactivo.setText(QCoreApplication.translate("ClienteIterableWindow", u"Inactivo", None))
    # retranslateUi

