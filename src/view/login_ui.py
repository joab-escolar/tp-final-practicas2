# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import login_resource_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(800, 600)
        LoginWindow.setStyleSheet(u"background-color: rgb(17, 51, 83);")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 61, 31))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.input_username = QLineEdit(self.centralwidget)
        self.input_username.setObjectName(u"input_username")
        self.input_username.setGeometry(QRect(300, 250, 171, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 230, 49, 16))
        self.btn_ingresar = QPushButton(self.centralwidget)
        self.btn_ingresar.setObjectName(u"btn_ingresar")
        self.btn_ingresar.setGeometry(QRect(300, 430, 171, 31))
        self.input_password = QLineEdit(self.centralwidget)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setGeometry(QRect(300, 320, 171, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 300, 61, 16))
        self.lbl_error = QLabel(self.centralwidget)
        self.lbl_error.setObjectName(u"lbl_error")
        self.lbl_error.setGeometry(QRect(300, 380, 331, 31))
        self.lbl_error.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, -20, 511, 281))
        self.label_4.setPixmap(QPixmap(u":/images/603322212.png"))
        self.label_4.setScaledContents(True)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.label_4.raise_()
        self.label.raise_()
        self.input_username.raise_()
        self.label_2.raise_()
        self.btn_ingresar.raise_()
        self.input_password.raise_()
        self.label_3.raise_()
        self.lbl_error.raise_()
        self.menubar = QMenuBar(LoginWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"BANCO", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"LOGIN", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"Usuario", None))
        self.btn_ingresar.setText(QCoreApplication.translate("LoginWindow", u"Ingresar", None))
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"Contrase\u00f1a", None))
        self.lbl_error.setText("")
        self.label_4.setText("")
    # retranslateUi

