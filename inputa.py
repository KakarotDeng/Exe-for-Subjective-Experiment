# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inputa.ui'
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
    QTextBrowser, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1127, 651)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 540, 1121, 91))
        self.label_2.setStyleSheet(u"font: 9pt \"Cambria Math\";")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 200, 281, 51))

        self.showifinputok = QTextBrowser(Form)
        self.showifinputok.setObjectName(u"showifinputok")
        self.showifinputok.setFontPointSize(14)
        self.showifinputok.setGeometry(QRect(100, 460, 921, 51))

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(10, 20, 1121, 161))

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())

        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(1121, 161))
        self.label.setMaximumSize(QSize(1121, 161))
        self.label.setStyleSheet(u"font: 9pt \"PMingLiU-ExtB\";\n"
"font: 9pt \"Gabriola\";")

        self.inputcheck = QPushButton(Form)
        self.inputcheck.setObjectName(u"inputcheck")
        self.inputcheck.setGeometry(QRect(830, 340, 161, 41))
        self.inputcheck.setStyleSheet(u"font: 20pt \"Cascadia Code\";")

        self.inputlight = QTextEdit(Form)
        self.inputlight.setFontPointSize(14)
        self.inputlight.setText('A D55 D65 D65+duv0.02 D65-duv0.02 D80')
        self.inputlight.setObjectName(u"inputlight")
        self.inputlight.setGeometry(QRect(400, 250, 291, 151))

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(810, 200, 281, 51))

        self.inputok = QPushButton(Form)
        self.inputok.setObjectName(u"inputok")
        self.inputok.setGeometry(QRect(480, 530, 161, 41))
        self.inputok.setStyleSheet(u"font: 20pt \"Cascadia Code\";")

        self.inputnum = QTextEdit(Form)
        self.inputnum.setFontPointSize(14)
        self.inputnum.setText('15')
        self.inputnum.setObjectName(u"inputnum")
        self.inputnum.setGeometry(QRect(800, 240, 221, 31))

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 130, 181, 51))

        self.inputpathedit = QTextEdit(Form)
        self.inputpathedit.setFontPointSize(14)
        self.inputpathedit.setObjectName(u"inputpathedit")
        self.inputpathedit.setGeometry(QRect(290, 140, 711, 31))

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 200, 191, 51))

        self.inputcmf = QTextEdit(Form)
        self.inputcmf.setFontPointSize(14)
        self.inputcmf.setText('1931 2015')
        self.inputcmf.setObjectName(u"inputcmf")
        self.inputcmf.setGeometry(QRect(110, 250, 181, 151))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">By KakarotDeng</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">LightSource Information</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; color:#ffaa7f;\">Subjective Experiment</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inputcheck.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>OK</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inputcheck.setText(QCoreApplication.translate("Form", u"Next", None))
        self.inputlight.setPlaceholderText(QCoreApplication.translate("Form", u"D65                                                                A...", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">Number of images</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inputok.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>OK</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inputok.setText(QCoreApplication.translate("Form", u"Next", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:22pt;\">Input Path</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">CMF Information</span></p></body></html>", None))
        self.inputcmf.setPlaceholderText(QCoreApplication.translate("Form", u"1931                             1964                           2015...", None))
    # retranslateUi

