# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_create.ui'
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

class Ui_usersCreateWindow(object):
    def setupUi(self, usersCreateWindow):
        if not usersCreateWindow.objectName():
            usersCreateWindow.setObjectName(u"usersCreateWindow")
        usersCreateWindow.resize(800, 600)
        self.centralwidget = QWidget(usersCreateWindow)
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
        self.btn_back.setGeometry(QRect(680, 10, 111, 41))
        self.input_username = QLineEdit(self.centralwidget)
        self.input_username.setObjectName(u"input_username")
        self.input_username.setGeometry(QRect(300, 160, 171, 31))
        self.slect_roles = QComboBox(self.centralwidget)
        self.slect_roles.setObjectName(u"slect_roles")
        self.slect_roles.setGeometry(QRect(300, 280, 171, 31))
        self.input_password = QLineEdit(self.centralwidget)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setGeometry(QRect(300, 220, 171, 31))
        self.btn_store = QPushButton(self.centralwidget)
        self.btn_store.setObjectName(u"btn_store")
        self.btn_store.setGeometry(QRect(300, 340, 171, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 140, 111, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 200, 111, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 260, 111, 16))
        usersCreateWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(usersCreateWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        usersCreateWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(usersCreateWindow)
        self.statusbar.setObjectName(u"statusbar")
        usersCreateWindow.setStatusBar(self.statusbar)

        self.retranslateUi(usersCreateWindow)

        QMetaObject.connectSlotsByName(usersCreateWindow)
    # setupUi

    def retranslateUi(self, usersCreateWindow):
        usersCreateWindow.setWindowTitle(QCoreApplication.translate("usersCreateWindow", u"BANCO", None))
        self.label.setText(QCoreApplication.translate("usersCreateWindow", u"USUARIOS -", None))
        self.lbl_show_user.setText("")
        self.btn_back.setText(QCoreApplication.translate("usersCreateWindow", u"Atras", None))
        self.btn_store.setText(QCoreApplication.translate("usersCreateWindow", u"Guardar", None))
        self.label_2.setText(QCoreApplication.translate("usersCreateWindow", u"Nombre de usuario", None))
        self.label_3.setText(QCoreApplication.translate("usersCreateWindow", u"Contrase\u00f1a", None))
        self.label_4.setText(QCoreApplication.translate("usersCreateWindow", u"Rol", None))
    # retranslateUi

