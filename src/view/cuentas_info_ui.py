# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cuentas_info.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_cuentasInfoWindow(object):
    def setupUi(self, cuentasInfoWindow):
        if not cuentasInfoWindow.objectName():
            cuentasInfoWindow.setObjectName(u"cuentasInfoWindow")
        cuentasInfoWindow.resize(1000, 800)
        cuentasInfoWindow.setMinimumSize(QSize(1000, 800))
        cuentasInfoWindow.setMaximumSize(QSize(1000, 800))
        self.centralwidget = QWidget(cuentasInfoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 141, 31))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.lbl_show_user = QLabel(self.centralwidget)
        self.lbl_show_user.setObjectName(u"lbl_show_user")
        self.lbl_show_user.setGeometry(QRect(130, 10, 451, 31))
        self.lbl_show_user.setFont(font)
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(880, 10, 111, 41))
        self.table_more_info = QTableWidget(self.centralwidget)
        self.table_more_info.setObjectName(u"table_more_info")
        self.table_more_info.setGeometry(QRect(10, 70, 651, 601))
        cuentasInfoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(cuentasInfoWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        cuentasInfoWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(cuentasInfoWindow)
        self.statusbar.setObjectName(u"statusbar")
        cuentasInfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(cuentasInfoWindow)

        QMetaObject.connectSlotsByName(cuentasInfoWindow)
    # setupUi

    def retranslateUi(self, cuentasInfoWindow):
        cuentasInfoWindow.setWindowTitle(QCoreApplication.translate("cuentasInfoWindow", u"BANCO", None))
        self.label.setText(QCoreApplication.translate("cuentasInfoWindow", u"CUENTAS-INFO", None))
        self.lbl_show_user.setText("")
        self.btn_back.setText(QCoreApplication.translate("cuentasInfoWindow", u"Atras", None))
    # retranslateUi

