# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'output.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

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

        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(70, 180, 611, 331))

        self.generate = QPushButton(Form)
        self.generate.setObjectName(u"generate")
        self.generate.setGeometry(QRect(410, 130, 291, 41))
        self.generate.setStyleSheet(u"font: 14pt \"Cascadia Code\";")

        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(760, 180, 301, 331))

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
        self.tableok.setText(QCoreApplication.translate("Form", u"Next", None))
#if QT_CONFIG(tooltip)
        self.generate.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>OK</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.generate.setText(QCoreApplication.translate("Form", u"Generate Disordered Table", None))
    # retranslateUi

