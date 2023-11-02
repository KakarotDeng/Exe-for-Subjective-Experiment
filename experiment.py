# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'experiment.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
from PyQt5.QtCore import QTimer

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")

        Form.resize(1920, 1080)
        Form.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")


        self.imgshow = QLabel(Form)
        self.imgshow.setObjectName(u"imgshow")
        self.imgshow.setGeometry(QRect(410, 10, 1101, 960))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1680, 870, 141, 51))
        self.pushButton.setStyleSheet(u"font: 16pt \"Segoe Fluent Icons\";\n"
"background-color: rgb(182, 182, 182);\n"
"color: rgb(255, 255, 255);")

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1680, 950, 141, 51))
        self.pushButton_2.setStyleSheet(u"font: 16pt \"Segoe Fluent Icons\";\n"
"background-color: rgb(182, 182, 182);\n"
"color: rgb(255, 255, 255);")
        self.reprod = QLabel(Form)
        self.reprod.setObjectName(u"reprod")
        self.reprod.setGeometry(QRect(1650, 435, 201, 41))
        self.reprod.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.present_infor = QLabel(Form)
        self.present_infor.setObjectName(u"present_infor")
        self.present_infor.setGeometry(QRect(470, 1010, 481, 41))
        self.present_infor.setStyleSheet(u"font: 75 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.next_infor = QLabel(Form)
        self.next_infor.setObjectName(u"next_infor")
        self.next_infor.setGeometry(QRect(1020, 1010, 411, 41))
        self.next_infor.setStyleSheet(u"font: 75 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.img_count = QLabel(Form)
        self.img_count.setObjectName(u"img_count")
        self.img_count.setGeometry(QRect(40, 470, 181, 71))
        self.img_count.setStyleSheet(u"font: 75 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(80, 870, 141, 51))
        self.pushButton_3.setStyleSheet(u"font: 16pt \"Segoe Fluent Icons\";\n"
"background-color: rgb(182, 182, 182);\n"
"color: rgb(255, 255, 255);")
        self.prefer = QLabel(Form)
        self.prefer.setObjectName(u"prefer")
        self.prefer.setGeometry(QRect(1650, 510, 201, 41))
        self.prefer.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")




        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.imgshow.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Previous", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Next", None))
        self.reprod.setText(QCoreApplication.translate("Form", u"Reprod : ", None))
        self.present_infor.setText("")
        self.next_infor.setText(QCoreApplication.translate("Form", u"Next : ", None))
        self.img_count.setText(QCoreApplication.translate("Form", u"C :", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Start", None))
        self.prefer.setText(QCoreApplication.translate("Form", u"Pref : ", None))
    #   retranslateUi

