# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_menuWindow(object):
    def setupUi(self, menuWindow):
        if not menuWindow.objectName():
            menuWindow.setObjectName(u"menuWindow")
        menuWindow.resize(800, 600)
        self.centralwidget = QWidget(menuWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 71, 31))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.lbl_show_user = QLabel(self.centralwidget)
        self.lbl_show_user.setObjectName(u"lbl_show_user")
        self.lbl_show_user.setGeometry(QRect(90, 10, 451, 31))
        self.lbl_show_user.setFont(font)
        self.btn_users = QPushButton(self.centralwidget)
        self.btn_users.setObjectName(u"btn_users")
        self.btn_users.setGeometry(QRect(300, 140, 181, 41))
        self.btn_clients = QPushButton(self.centralwidget)
        self.btn_clients.setObjectName(u"btn_clients")
        self.btn_clients.setGeometry(QRect(300, 190, 181, 41))
        self.btn_account = QPushButton(self.centralwidget)
        self.btn_account.setObjectName(u"btn_account")
        self.btn_account.setGeometry(QRect(300, 240, 181, 41))
        self.btn_transactions = QPushButton(self.centralwidget)
        self.btn_transactions.setObjectName(u"btn_transactions")
        self.btn_transactions.setGeometry(QRect(300, 290, 181, 41))
        self.btn_logout = QPushButton(self.centralwidget)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setGeometry(QRect(300, 340, 181, 41))
        menuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(menuWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        menuWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(menuWindow)
        self.statusbar.setObjectName(u"statusbar")
        menuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(menuWindow)

        QMetaObject.connectSlotsByName(menuWindow)
    # setupUi

    def retranslateUi(self, menuWindow):
        menuWindow.setWindowTitle(QCoreApplication.translate("menuWindow", u"BANCO", None))
        self.label.setText(QCoreApplication.translate("menuWindow", u"MENU -", None))
        self.lbl_show_user.setText("")
        self.btn_users.setText(QCoreApplication.translate("menuWindow", u"Usuarios", None))
        self.btn_clients.setText(QCoreApplication.translate("menuWindow", u"Clientes", None))
        self.btn_account.setText(QCoreApplication.translate("menuWindow", u"Cuentas", None))
        self.btn_transactions.setText(QCoreApplication.translate("menuWindow", u"Transacciones", None))
        self.btn_logout.setText(QCoreApplication.translate("menuWindow", u"Salir", None))
    # retranslateUi

