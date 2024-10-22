# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transaccion_create.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_transaccionAltaWindow(object):
    def setupUi(self, transaccionAltaWindow):
        if not transaccionAltaWindow.objectName():
            transaccionAltaWindow.setObjectName(u"transaccionAltaWindow")
        transaccionAltaWindow.resize(1000, 800)
        transaccionAltaWindow.setMinimumSize(QSize(1000, 800))
        transaccionAltaWindow.setMaximumSize(QSize(1000, 800))
        self.centralwidget = QWidget(transaccionAltaWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 131, 31))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.lbl_show_user = QLabel(self.centralwidget)
        self.lbl_show_user.setObjectName(u"lbl_show_user")
        self.lbl_show_user.setGeometry(QRect(130, 10, 571, 31))
        self.lbl_show_user.setFont(font)
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(870, 0, 111, 41))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 260, 111, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(500, 340, 111, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 340, 91, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(500, 260, 91, 16))
        self.btn_create = QPushButton(self.centralwidget)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setGeometry(QRect(310, 440, 341, 31))
        self.input_monto = QLineEdit(self.centralwidget)
        self.input_monto.setObjectName(u"input_monto")
        self.input_monto.setGeometry(QRect(490, 360, 171, 31))
        self.slect_Egreso = QComboBox(self.centralwidget)
        self.slect_Egreso.setObjectName(u"slect_Egreso")
        self.slect_Egreso.setGeometry(QRect(310, 280, 171, 31))
        self.slect_Ingreso = QComboBox(self.centralwidget)
        self.slect_Ingreso.setObjectName(u"slect_Ingreso")
        self.slect_Ingreso.setGeometry(QRect(490, 280, 171, 31))
        self.input_inpact_date = QDateTimeEdit(self.centralwidget)
        self.input_inpact_date.setObjectName(u"input_inpact_date")
        self.input_inpact_date.setGeometry(QRect(310, 360, 171, 31))
        transaccionAltaWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(transaccionAltaWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        transaccionAltaWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(transaccionAltaWindow)
        self.statusbar.setObjectName(u"statusbar")
        transaccionAltaWindow.setStatusBar(self.statusbar)

        self.retranslateUi(transaccionAltaWindow)

        QMetaObject.connectSlotsByName(transaccionAltaWindow)
    # setupUi

    def retranslateUi(self, transaccionAltaWindow):
        transaccionAltaWindow.setWindowTitle(QCoreApplication.translate("transaccionAltaWindow", u"BANCO", None))
        self.label.setText(QCoreApplication.translate("transaccionAltaWindow", u"TRANSACCION-", None))
        self.lbl_show_user.setText("")
        self.btn_back.setText(QCoreApplication.translate("transaccionAltaWindow", u"Atras", None))
        self.label_3.setText(QCoreApplication.translate("transaccionAltaWindow", u"Cuenta Egreso", None))
        self.label_4.setText(QCoreApplication.translate("transaccionAltaWindow", u"Monto", None))
        self.label_5.setText(QCoreApplication.translate("transaccionAltaWindow", u"Fecha Impactada", None))
        self.label_6.setText(QCoreApplication.translate("transaccionAltaWindow", u"Cuenta Ingreso", None))
        self.btn_create.setText(QCoreApplication.translate("transaccionAltaWindow", u"Crear", None))
    # retranslateUi

