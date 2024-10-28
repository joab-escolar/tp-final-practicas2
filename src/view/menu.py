# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_menuWindow(object):
    def setupUi(self, menuWindow):
        if not menuWindow.objectName():
            menuWindow.setObjectName(u"menuWindow")
        menuWindow.resize(1000, 800)
        menuWindow.setMinimumSize(QSize(1000, 800))
        menuWindow.setMaximumSize(QSize(1000, 800))
        menuWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(menuWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 71, 31))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.lbl_show_user = QLabel(self.centralwidget)
        self.lbl_show_user.setObjectName(u"lbl_show_user")
        self.lbl_show_user.setGeometry(QRect(90, 10, 451, 31))
        self.lbl_show_user.setFont(font)
        self.lbl_show_user.setStyleSheet(u"")
        self.btn_users = QPushButton(self.centralwidget)
        self.btn_users.setObjectName(u"btn_users")
        self.btn_users.setGeometry(QRect(420, 230, 181, 41))
        self.btn_users.setStyleSheet(u"background-color: rgb(17, 51, 83);\n"
"selection-background-color: rgb(23, 69, 112);\n"
"")
        self.btn_clients = QPushButton(self.centralwidget)
        self.btn_clients.setObjectName(u"btn_clients")
        self.btn_clients.setGeometry(QRect(420, 280, 181, 41))
        self.btn_clients.setStyleSheet(u"background-color: rgb(17, 51, 83);\n"
"selection-background-color: rgb(23, 69, 112);\n"
"")
        self.btn_account = QPushButton(self.centralwidget)
        self.btn_account.setObjectName(u"btn_account")
        self.btn_account.setGeometry(QRect(420, 330, 181, 41))
        self.btn_account.setStyleSheet(u"background-color: rgb(17, 51, 83);\n"
"selection-background-color: rgb(23, 69, 112);\n"
"")
        self.btn_transactions = QPushButton(self.centralwidget)
        self.btn_transactions.setObjectName(u"btn_transactions")
        self.btn_transactions.setGeometry(QRect(420, 380, 181, 41))
        self.btn_transactions.setStyleSheet(u"background-color: rgb(17, 51, 83);\n"
"selection-background-color: rgb(23, 69, 112);\n"
"")
        self.btn_logout = QPushButton(self.centralwidget)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setGeometry(QRect(420, 430, 181, 41))
        self.btn_logout.setStyleSheet(u"background-color: rgb(131, 131, 131);\n"
"selection-background-color: rgb(17, 51, 83);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-60, -10, 171, 901))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"background-color: rgb(17, 51, 83);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-40, -30, 1111, 811))
        self.label_3.setStyleSheet(u"background-color: rgb(17, 51, 83);\n"
"background-color: rgb(166, 166, 166);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, -20, 21, 801))
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"background-color: rgb(17, 51, 83);")
        menuWindow.setCentralWidget(self.centralwidget)
        self.label_3.raise_()
        self.label_2.raise_()
        self.btn_users.raise_()
        self.btn_clients.raise_()
        self.btn_account.raise_()
        self.btn_transactions.raise_()
        self.btn_logout.raise_()
        self.label_4.raise_()
        self.lbl_show_user.raise_()
        self.label.raise_()
        self.menubar = QMenuBar(menuWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
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
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
    # retranslateUi

