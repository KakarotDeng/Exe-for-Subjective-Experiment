# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1127, 651)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 540, 1121, 91))
        self.label_2.setStyleSheet(u"font: 9pt \"Cambria Math\";")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(10, 30, 1121, 161))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(1121, 161))
        self.label.setMaximumSize(QSize(1121, 161))
        self.label.setStyleSheet(u"font: 9pt \"PMingLiU-ExtB\";\n"
"font: 9pt \"Gabriola\";")
        self.tableok = QPushButton(Form)
        self.tableok.setObjectName(u"tableok")
        self.tableok.setGeometry(QRect(480, 530, 161, 41))
        self.tableok.setStyleSheet(u"font: 20pt \"Cascadia Code\";")

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setText('djc')
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(250, 230, 621, 31))

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 180, 481, 41))
        self.label_3.setStyleSheet(u"font: 15pt \"ROG Fonts\";\n"
"font: 15pt \"Microsoft PhagsPa\";")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 290, 481, 41))
        self.label_4.setStyleSheet(u"font: 15pt \"ROG Fonts\";\n"
"font: 15pt \"Microsoft PhagsPa\";")

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setText('D:\subexp')
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(250, 340, 621, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">By KakarotDeng</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; color:#ffaa7f;\">Subjective Experiment</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.tableok.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>OK</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tableok.setText(QCoreApplication.translate("Form", u"Start", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Enter a name for this experiment</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Enter save path</p></body></html>", None))
    # retranslateUi

