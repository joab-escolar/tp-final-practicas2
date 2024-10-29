# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cuenta_create.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_CuentasIterableWindow(object):
    def setupUi(self, CuentasIterableWindow):
        if not CuentasIterableWindow.objectName():
            CuentasIterableWindow.setObjectName(u"CuentasIterableWindow")
        CuentasIterableWindow.resize(1000, 800)
        CuentasIterableWindow.setMinimumSize(QSize(1000, 800))
        CuentasIterableWindow.setMaximumSize(QSize(1000, 800))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Computer))
        CuentasIterableWindow.setWindowIcon(icon)
        CuentasIterableWindow.setStyleSheet(u"background-color: rgb(17, 51, 83);\n"
"\n"
"")
        self.centralwidget = QWidget(CuentasIterableWindow)
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
        self.btn_back.setGeometry(QRect(870, 10, 111, 41))
        self.btn_back.setStyleSheet(u"background-color: rgb(39, 39, 39)")
        self.input_cbu = QLineEdit(self.centralwidget)
        self.input_cbu.setObjectName(u"input_cbu")
        self.input_cbu.setGeometry(QRect(340, 250, 171, 31))
        self.input_cbu.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.slect_titular = QComboBox(self.centralwidget)
        self.slect_titular.setObjectName(u"slect_titular")
        self.slect_titular.setGeometry(QRect(520, 250, 171, 31))
        self.slect_titular.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_crear = QPushButton(self.centralwidget)
        self.btn_crear.setObjectName(u"btn_crear")
        self.btn_crear.setGeometry(QRect(340, 440, 351, 31))
        self.btn_crear.setStyleSheet(u"background-color: rgb(11, 3, 255);\n"
"selection-background-color: rgb(138, 138, 138);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 230, 111, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(520, 230, 111, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 290, 111, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(520, 290, 111, 16))
        self.input_alias = QLineEdit(self.centralwidget)
        self.input_alias.setObjectName(u"input_alias")
        self.input_alias.setGeometry(QRect(520, 310, 171, 31))
        self.input_alias.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.input_tipo = QLineEdit(self.centralwidget)
        self.input_tipo.setObjectName(u"input_tipo")
        self.input_tipo.setGeometry(QRect(340, 310, 171, 31))
        self.input_tipo.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.input_balance = QLineEdit(self.centralwidget)
        self.input_balance.setObjectName(u"input_balance")
        self.input_balance.setGeometry(QRect(340, 380, 171, 31))
        self.input_balance.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lbl_balance = QLabel(self.centralwidget)
        self.lbl_balance.setObjectName(u"lbl_balance")
        self.lbl_balance.setGeometry(QRect(340, 360, 111, 16))
        CuentasIterableWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CuentasIterableWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        CuentasIterableWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CuentasIterableWindow)
        self.statusbar.setObjectName(u"statusbar")
        CuentasIterableWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CuentasIterableWindow)

        QMetaObject.connectSlotsByName(CuentasIterableWindow)
    # setupUi

    def retranslateUi(self, CuentasIterableWindow):
        CuentasIterableWindow.setWindowTitle(QCoreApplication.translate("CuentasIterableWindow", u"BANCO", None))
        self.label.setText(QCoreApplication.translate("CuentasIterableWindow", u"CUENTAS-", None))
        self.lbl_show_user.setText("")
        self.btn_back.setText(QCoreApplication.translate("CuentasIterableWindow", u"Atras", None))
        self.btn_crear.setText(QCoreApplication.translate("CuentasIterableWindow", u"Crear", None))
        self.label_2.setText(QCoreApplication.translate("CuentasIterableWindow", u"CBU", None))
        self.label_3.setText(QCoreApplication.translate("CuentasIterableWindow", u"Titular", None))
        self.label_4.setText(QCoreApplication.translate("CuentasIterableWindow", u"Tipo de cuenta", None))
        self.label_5.setText(QCoreApplication.translate("CuentasIterableWindow", u"Alias", None))
        self.lbl_balance.setText(QCoreApplication.translate("CuentasIterableWindow", u"balance inicial", None))
    # retranslateUi

