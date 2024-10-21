# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_usersWindow(object):
    def setupUi(self, usersWindow):
        if not usersWindow.objectName():
            usersWindow.setObjectName(u"usersWindow")
        usersWindow.resize(800, 600)
        self.centralwidget = QWidget(usersWindow)
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
        self.btn_create = QPushButton(self.centralwidget)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setGeometry(QRect(30, 70, 81, 41))
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(680, 10, 111, 41))
        self.btn_edit = QPushButton(self.centralwidget)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setGeometry(QRect(120, 70, 81, 41))
        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(210, 70, 81, 41))
        self.list_users = QListWidget(self.centralwidget)
        self.list_users.setObjectName(u"list_users")
        self.list_users.setGeometry(QRect(30, 130, 491, 401))
        usersWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(usersWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        usersWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(usersWindow)
        self.statusbar.setObjectName(u"statusbar")
        usersWindow.setStatusBar(self.statusbar)

        self.retranslateUi(usersWindow)

        QMetaObject.connectSlotsByName(usersWindow)
    # setupUi

    def retranslateUi(self, usersWindow):
        usersWindow.setWindowTitle(QCoreApplication.translate("usersWindow", u"BANCO", None))
        self.label.setText(QCoreApplication.translate("usersWindow", u"USUARIOS -", None))
        self.lbl_show_user.setText("")
        self.btn_create.setText(QCoreApplication.translate("usersWindow", u"Crear", None))
        self.btn_back.setText(QCoreApplication.translate("usersWindow", u"Atras", None))
        self.btn_edit.setText(QCoreApplication.translate("usersWindow", u"Editar", None))
        self.btn_delete.setText(QCoreApplication.translate("usersWindow", u"Eliminar", None))
    # retranslateUi

