# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cliente.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QListView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_clienteWindow(object):
    def setupUi(self, clienteWindow):
        if not clienteWindow.objectName():
            clienteWindow.setObjectName(u"clienteWindow")
        clienteWindow.resize(1000, 800)
        clienteWindow.setMinimumSize(QSize(1000, 800))
        clienteWindow.setMaximumSize(QSize(1000, 800))
        self.centralwidget = QWidget(clienteWindow)
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
        self.btn_back.setGeometry(QRect(870, 10, 111, 41))
        self.btn_edit = QPushButton(self.centralwidget)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setGeometry(QRect(120, 70, 81, 41))
        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(210, 70, 81, 41))
        self.table_clients = QTableWidget(self.centralwidget)
        self.table_clients.setObjectName(u"table_clients")
        self.table_clients.setGeometry(QRect(30, 130, 651, 601))
        self.list_estadistica = QListView(self.centralwidget)
        self.list_estadistica.setObjectName(u"list_estadistica")
        self.list_estadistica.setGeometry(QRect(710, 130, 261, 601))
        clienteWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(clienteWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        clienteWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(clienteWindow)
        self.statusbar.setObjectName(u"statusbar")
        clienteWindow.setStatusBar(self.statusbar)

        self.retranslateUi(clienteWindow)

        QMetaObject.connectSlotsByName(clienteWindow)
    # setupUi

    def retranslateUi(self, clienteWindow):
        clienteWindow.setWindowTitle(QCoreApplication.translate("clienteWindow", u"BANCO", None))
        self.label.setText(QCoreApplication.translate("clienteWindow", u"CLIENTES-", None))
        self.lbl_show_user.setText("")
        self.btn_create.setText(QCoreApplication.translate("clienteWindow", u"Nuevo", None))
        self.btn_back.setText(QCoreApplication.translate("clienteWindow", u"Atras", None))
        self.btn_edit.setText(QCoreApplication.translate("clienteWindow", u"Editar", None))
        self.btn_delete.setText(QCoreApplication.translate("clienteWindow", u"Eliminar", None))
    # retranslateUi

