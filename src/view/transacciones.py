# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transacciones.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_transanccionWindow(object):
    def setupUi(self, transanccionWindow):
        if not transanccionWindow.objectName():
            transanccionWindow.setObjectName(u"transanccionWindow")
        transanccionWindow.resize(1000, 800)
        transanccionWindow.setMinimumSize(QSize(1000, 800))
        transanccionWindow.setMaximumSize(QSize(1000, 800))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Computer))
        transanccionWindow.setWindowIcon(icon)
        transanccionWindow.setStyleSheet(u"background-color: rgb(17, 51, 83);\n"
"\n"
"")
        self.centralwidget = QWidget(transanccionWindow)
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
        self.btn_nuevo = QPushButton(self.centralwidget)
        self.btn_nuevo.setObjectName(u"btn_nuevo")
        self.btn_nuevo.setGeometry(QRect(30, 70, 81, 41))
        self.btn_nuevo.setStyleSheet(u"background-color: rgb(17, 51, 83);\n"
"selection-background-color: rgb(23, 69, 112);\n"
"")
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(880, 10, 111, 41))
        self.btn_back.setStyleSheet(u"background-color: rgb(39, 39, 39)")
        self.table_transacctions = QTableWidget(self.centralwidget)
        self.table_transacctions.setObjectName(u"table_transacctions")
        self.table_transacctions.setGeometry(QRect(30, 120, 651, 601))
        self.table_transacctions.setStyleSheet(u"background-color: rgb(39, 39, 39)")
        transanccionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(transanccionWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        transanccionWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(transanccionWindow)
        self.statusbar.setObjectName(u"statusbar")
        transanccionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(transanccionWindow)

        QMetaObject.connectSlotsByName(transanccionWindow)
    # setupUi

    def retranslateUi(self, transanccionWindow):
        transanccionWindow.setWindowTitle(QCoreApplication.translate("transanccionWindow", u"BANCO", None))
        self.label.setText(QCoreApplication.translate("transanccionWindow", u"TRANSACCION-", None))
        self.lbl_show_user.setText("")
        self.btn_nuevo.setText(QCoreApplication.translate("transanccionWindow", u"Nuevo", None))
        self.btn_back.setText(QCoreApplication.translate("transanccionWindow", u"Atras", None))
    # retranslateUi

