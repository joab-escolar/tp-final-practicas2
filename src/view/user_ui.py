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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_usersWindow(object):
    def setupUi(self, usersWindow):
        if not usersWindow.objectName():
            usersWindow.setObjectName(u"usersWindow")
        usersWindow.resize(1000, 800)
        usersWindow.setMinimumSize(QSize(1000, 800))
        usersWindow.setMaximumSize(QSize(1000, 800))
        usersWindow.setStyleSheet(u"background-color: rgb(17, 51, 83);")
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
        self.lbl_show_user.setGeometry(QRect(130, 10, 531, 31))
        self.lbl_show_user.setFont(font)
        self.btn_create = QPushButton(self.centralwidget)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setGeometry(QRect(30, 70, 81, 41))
        self.btn_create.setStyleSheet(u"background-color: rgb(17, 51, 83);\n"
"selection-background-color: rgb(23, 69, 112);\n"
"")
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(870, 10, 111, 41))
        self.btn_back.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.btn_edit = QPushButton(self.centralwidget)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setGeometry(QRect(120, 70, 81, 41))
        self.btn_edit.setStyleSheet(u"background-color: rgb(17, 51, 83);\n"
"selection-background-color: rgb(23, 69, 112);\n"
"")
        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(210, 70, 81, 41))
        self.btn_delete.setStyleSheet(u"background-color: rgb(190, 0, 0);")
        self.table_user = QTableWidget(self.centralwidget)
        self.table_user.setObjectName(u"table_user")
        self.table_user.setGeometry(QRect(30, 140, 651, 601))
        self.table_user.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, -40, 51, 961))
        self.label_3.setStyleSheet(u"background-color: rgb(166, 166, 166);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-60, -60, 161, 901))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"background-color: rgb(166, 166, 166);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(990, -70, 21, 901))
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"background-color: rgb(166, 166, 166);")
        usersWindow.setCentralWidget(self.centralwidget)
        self.label_5.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.lbl_show_user.raise_()
        self.btn_create.raise_()
        self.btn_back.raise_()
        self.btn_edit.raise_()
        self.btn_delete.raise_()
        self.table_user.raise_()
        self.menubar = QMenuBar(usersWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
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
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
    # retranslateUi

