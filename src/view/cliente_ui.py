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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_clienteWindow(object):
    def setupUi(self, clienteWindow):
        if not clienteWindow.objectName():
            clienteWindow.setObjectName(u"clienteWindow")
        clienteWindow.resize(1000, 800)
        clienteWindow.setMinimumSize(QSize(1000, 800))
        clienteWindow.setMaximumSize(QSize(1000, 800))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Computer))
        clienteWindow.setWindowIcon(icon)
        clienteWindow.setStyleSheet(u"background-color: rgb(17, 51, 83);")
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
        self.btn_create.setStyleSheet(u"background-color: rgb(39, 39, 39)")
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(870, 10, 111, 41))
        self.btn_back.setStyleSheet(u"background-color: rgb(39, 39, 39)")
        self.btn_edit = QPushButton(self.centralwidget)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setGeometry(QRect(120, 70, 81, 41))
        self.btn_edit.setStyleSheet(u"background-color: rgb(39, 39, 39)")
        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(210, 70, 81, 41))
        self.btn_delete.setStyleSheet(u"background-color: rgb(190, 0, 0);")
        self.table_clients = QTableWidget(self.centralwidget)
        self.table_clients.setObjectName(u"table_clients")
        self.table_clients.setGeometry(QRect(30, 130, 651, 601))
        self.table_clients.setStyleSheet(u"background-color: rgb(39, 39, 39)")
        self.lbl_total_clients = QLabel(self.centralwidget)
        self.lbl_total_clients.setObjectName(u"lbl_total_clients")
        self.lbl_total_clients.setGeometry(QRect(700, 460, 251, 31))
        font1 = QFont()
        font1.setPointSize(13)
        self.lbl_total_clients.setFont(font1)
        self.lbl_total_active_clients = QLabel(self.centralwidget)
        self.lbl_total_active_clients.setObjectName(u"lbl_total_active_clients")
        self.lbl_total_active_clients.setGeometry(QRect(700, 500, 251, 31))
        self.lbl_total_active_clients.setFont(font1)
        self.lbl_total_inactive_clients = QLabel(self.centralwidget)
        self.lbl_total_inactive_clients.setObjectName(u"lbl_total_inactive_clients")
        self.lbl_total_inactive_clients.setGeometry(QRect(700, 540, 251, 31))
        self.lbl_total_inactive_clients.setFont(font1)
        self.list_estadistica = QListWidget(self.centralwidget)
        self.list_estadistica.setObjectName(u"list_estadistica")
        self.list_estadistica.setGeometry(QRect(700, 130, 261, 291))
        self.list_estadistica.setStyleSheet(u"background-color: rgb(39, 39, 39)")
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
        self.lbl_total_clients.setText("")
        self.lbl_total_active_clients.setText("")
        self.lbl_total_inactive_clients.setText("")
    # retranslateUi

