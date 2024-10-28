# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_create.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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

class Ui_usersIterableWindow(object):
    def setupUi(self, usersIterableWindow):
        if not usersIterableWindow.objectName():
            usersIterableWindow.setObjectName(u"usersIterableWindow")
        usersIterableWindow.resize(1000, 800)
        usersIterableWindow.setMinimumSize(QSize(1000, 800))
        usersIterableWindow.setMaximumSize(QSize(1000, 800))
        usersIterableWindow.setStyleSheet(u"background-color: rgb(17, 51, 83);")
        self.centralwidget = QWidget(usersIterableWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 131, 31))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.lbl_show_user = QLabel(self.centralwidget)
        self.lbl_show_user.setObjectName(u"lbl_show_user")
        self.lbl_show_user.setGeometry(QRect(130, 10, 581, 31))
        self.lbl_show_user.setFont(font)
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(870, 10, 111, 41))
        self.btn_back.setStyleSheet(u"background-color: rgb(39, 39, 39);\n"
"")
        self.input_username = QLineEdit(self.centralwidget)
        self.input_username.setObjectName(u"input_username")
        self.input_username.setGeometry(QRect(400, 230, 171, 31))
        self.input_username.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.slect_roles = QComboBox(self.centralwidget)
        self.slect_roles.setObjectName(u"slect_roles")
        self.slect_roles.setGeometry(QRect(400, 350, 171, 31))
        self.slect_roles.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.input_password = QLineEdit(self.centralwidget)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setGeometry(QRect(400, 290, 171, 31))
        self.input_password.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_store = QPushButton(self.centralwidget)
        self.btn_store.setObjectName(u"btn_store")
        self.btn_store.setGeometry(QRect(400, 410, 171, 31))
        self.btn_store.setStyleSheet(u"background-color: rgb(85, 170, 127);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(400, 210, 111, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 270, 111, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(400, 330, 111, 16))
        usersIterableWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(usersIterableWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        usersIterableWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(usersIterableWindow)
        self.statusbar.setObjectName(u"statusbar")
        usersIterableWindow.setStatusBar(self.statusbar)

        self.retranslateUi(usersIterableWindow)

        QMetaObject.connectSlotsByName(usersIterableWindow)
    # setupUi

    def retranslateUi(self, usersIterableWindow):
        usersIterableWindow.setWindowTitle(QCoreApplication.translate("usersIterableWindow", u"BANCO", None))
        self.label.setText(QCoreApplication.translate("usersIterableWindow", u"USUARIOS -", None))
        self.lbl_show_user.setText("")
        self.btn_back.setText(QCoreApplication.translate("usersIterableWindow", u"Atras", None))
        self.btn_store.setText(QCoreApplication.translate("usersIterableWindow", u"Guardar", None))
        self.label_2.setText(QCoreApplication.translate("usersIterableWindow", u"Nombre de usuario", None))
        self.label_3.setText(QCoreApplication.translate("usersIterableWindow", u"Contrase\u00f1a", None))
        self.label_4.setText(QCoreApplication.translate("usersIterableWindow", u"Rol", None))
    # retranslateUi

