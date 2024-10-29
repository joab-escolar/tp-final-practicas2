# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cuentas.ui'
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

class Ui_cuentasWindow(object):
    def setupUi(self, cuentasWindow):
        if not cuentasWindow.objectName():
            cuentasWindow.setObjectName(u"cuentasWindow")
        cuentasWindow.resize(1000, 800)
        cuentasWindow.setMinimumSize(QSize(1000, 800))
        cuentasWindow.setMaximumSize(QSize(1000, 800))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Computer))
        cuentasWindow.setWindowIcon(icon)
        cuentasWindow.setStyleSheet(u"background-color: rgb(17, 51, 83);")
        self.centralwidget = QWidget(cuentasWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 131, 31))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.lbl_show_user = QLabel(self.centralwidget)
        self.lbl_show_user.setObjectName(u"lbl_show_user")
        self.lbl_show_user.setGeometry(QRect(130, 30, 631, 31))
        self.lbl_show_user.setFont(font)
        self.btn_create = QPushButton(self.centralwidget)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setGeometry(QRect(30, 70, 81, 41))
        self.btn_create.setStyleSheet(u"background-color: rgb(39, 39, 39)")
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(860, 20, 111, 41))
        self.btn_back.setStyleSheet(u"background-color: rgb(39, 39, 39)")
        self.btn_edit = QPushButton(self.centralwidget)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setGeometry(QRect(120, 70, 81, 41))
        self.btn_edit.setStyleSheet(u"background-color: rgb(39, 39, 39)")
        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(210, 70, 81, 41))
        self.btn_delete.setStyleSheet(u"background-color: rgb(190, 0, 0);")
        self.table_accounts = QTableWidget(self.centralwidget)
        self.table_accounts.setObjectName(u"table_accounts")
        self.table_accounts.setGeometry(QRect(30, 130, 651, 601))
        self.table_accounts.setStyleSheet(u"background-color: rgb(39, 39, 39)")
        self.btn_history = QPushButton(self.centralwidget)
        self.btn_history.setObjectName(u"btn_history")
        self.btn_history.setGeometry(QRect(300, 70, 81, 41))
        self.btn_history.setStyleSheet(u"background-color: rgb(176, 59, 0);")
        self.lbl_total_positive_accounts = QLabel(self.centralwidget)
        self.lbl_total_positive_accounts.setObjectName(u"lbl_total_positive_accounts")
        self.lbl_total_positive_accounts.setGeometry(QRect(700, 670, 251, 31))
        font1 = QFont()
        font1.setPointSize(13)
        self.lbl_total_positive_accounts.setFont(font1)
        self.lbl_total_accounts = QLabel(self.centralwidget)
        self.lbl_total_accounts.setObjectName(u"lbl_total_accounts")
        self.lbl_total_accounts.setGeometry(QRect(700, 620, 251, 31))
        self.lbl_total_accounts.setFont(font1)
        self.list_estadistica = QListWidget(self.centralwidget)
        self.list_estadistica.setObjectName(u"list_estadistica")
        self.list_estadistica.setGeometry(QRect(690, 130, 261, 461))
        self.list_estadistica.setStyleSheet(u"background-color: rgb(39, 39, 39)")
        cuentasWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(cuentasWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        cuentasWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(cuentasWindow)
        self.statusbar.setObjectName(u"statusbar")
        cuentasWindow.setStatusBar(self.statusbar)

        self.retranslateUi(cuentasWindow)

        QMetaObject.connectSlotsByName(cuentasWindow)
    # setupUi

    def retranslateUi(self, cuentasWindow):
        cuentasWindow.setWindowTitle(QCoreApplication.translate("cuentasWindow", u"BANCO", None))
        self.label.setText(QCoreApplication.translate("cuentasWindow", u"CUENTAS-", None))
        self.lbl_show_user.setText("")
        self.btn_create.setText(QCoreApplication.translate("cuentasWindow", u"Nuevo", None))
        self.btn_back.setText(QCoreApplication.translate("cuentasWindow", u"Atras", None))
        self.btn_edit.setText(QCoreApplication.translate("cuentasWindow", u"Editar", None))
        self.btn_delete.setText(QCoreApplication.translate("cuentasWindow", u"Eliminar", None))
        self.btn_history.setText(QCoreApplication.translate("cuentasWindow", u"Historial", None))
        self.lbl_total_positive_accounts.setText("")
        self.lbl_total_accounts.setText("")
    # retranslateUi

