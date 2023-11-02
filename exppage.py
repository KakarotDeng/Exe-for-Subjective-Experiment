import csv
import sys
import time
import pandas as pd

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, QTimer, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
from PyQt5.QtCore import pyqtSignal, QObject, QCoreApplication
#from experiment import *
import random
import cv2
import numpy as np
import os

class MyWindow4(QWidget):
    global ct
    ct = 0
    global T
    T = 0



    def __init__(self, parent=None):
        super(MyWindow4, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_3.clicked.connect(self.start_to)
        self.pushButton_2.clicked.connect(lambda : self.next_img(ct))
        self.pushButton.clicked.connect(lambda : self.previous_img(ct))



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
    def retranslateUi(self, Form):
            Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
            self.imgshow.setText("")
            self.pushButton.setText(QCoreApplication.translate("Form", u"Previous", None))
            self.pushButton_2.setText(QCoreApplication.translate("Form", u"Next", None))
            self.reprod.setText(QCoreApplication.translate("Form", u"Reprod : ", None))
            self.present_infor.setText("")
            self.next_infor.setText(QCoreApplication.translate("Form", u"Next : ", None))
            self.img_count.setText(QCoreApplication.translate("Form", u"C : ", None))
            self.pushButton_3.setText(QCoreApplication.translate("Form", u"Start", None))
            self.prefer.setText(QCoreApplication.translate("Form", u"Pref : ", None))
    def record_reprod(self, reprod):
        self.reprod.setText(QCoreApplication.translate("Form", u"Reprod : %s"%reprod, None))
        img_table = np.load('table.npy').copy()
        img_order = np.load('disorder.npy').copy()
        img_order = img_order.reshape(img_order.shape[0] * img_order.shape[1], 1)
        scorepths = np.load('pths.npy').copy()
        [psa, psb] = np.where(img_table == img_order[ct-1])
        datas = pd.read_csv(scorepths[0], index_col=0)
        datas.iloc[psa, psb] = reprod
        datas.to_csv(scorepths[0])
        global T
        T += 0.5
        if T == 1:
            self.pushButton_2.setEnabled(True)
    def record_pref(self, pref):
        self.prefer.setText(QCoreApplication.translate("Form", u"Pref : %s"%pref, None))
        img_table = np.load('table.npy').copy()
        img_order = np.load('disorder.npy').copy()
        img_order = img_order.reshape(img_order.shape[0] * img_order.shape[1], 1)
        scorepths = np.load('pths.npy').copy()
        [psa, psb] = np.where(img_table == img_order[ct-1])
        datas = pd.read_csv(scorepths[1], index_col=0)
        datas.iloc[psa, psb] = pref
        datas.to_csv(scorepths[1])
        global T
        T += 0.5
        if T == 1:
            self.pushButton_2.setEnabled(True)


    def keyPressEvent(self, event):
        imgs = np.load('imgbox.npy').copy()
        total = len(imgs)*len(imgs[0])*len(imgs[0][0])

        if (event.key() == Qt.Key_Escape):
            sys.exit()
        if 0<ct<=total:

            if (event.key() == Qt.Key_1):
                reprod = 1
                self.record_reprod(reprod)
            if (event.key() == Qt.Key_2):
                reprod = 2
                self.record_reprod(reprod)
            if (event.key() == Qt.Key_3):
                reprod = 3
                self.record_reprod(reprod)
            if (event.key() == Qt.Key_4):
                reprod = 4
                self.record_reprod(reprod)
            if (event.key() == Qt.Key_5):
                reprod = 5
                self.record_reprod(reprod)
            if (event.key() == Qt.Key_6):
                reprod = 6
                self.record_reprod(reprod)
            if (event.key() == Qt.Key_7):
                reprod = 7
                self.record_reprod(reprod)
            if (event.key() == Qt.Key_8):
                reprod = 8
                self.record_reprod(reprod)
            if (event.key() == Qt.Key_9):
                reprod = 9
                self.record_reprod(reprod)
            if (event.key() == Qt.Key_A):
                pref = 1
                self.record_pref(pref)
            if (event.key() == Qt.Key_S):
                pref = 2
                self.record_pref(pref)
            if (event.key() == Qt.Key_D):
                pref = 3
                self.record_pref(pref)
            if (event.key() == Qt.Key_F):
                pref = 4
                self.record_pref(pref)
            if (event.key() == Qt.Key_G):
                pref = 5
                self.record_pref(pref)
            if (event.key() == Qt.Key_H):
                pref = 6
                self.record_pref(pref)
            if (event.key() == Qt.Key_J):
                pref = 7
                self.record_pref(pref)
            if (event.key() == Qt.Key_K):
                pref = 8
                self.record_pref(pref)
            if (event.key() == Qt.Key_L):
                pref = 9
                self.record_pref(pref)
    def start_to(self):
        self.bigblack = QPushButton(self)
        self.bigblack.setObjectName(u"bigblack")
        self.bigblack.setGeometry(QRect(0, 0, 1920, 1080))
        self.bigblack.setStyleSheet(u"font: 14pt \"Cascadia Code\";")
        self.bigblack.setStyleSheet(u"font: 16pt \"Segoe Fluent Icons\";\n"
                                      "background-color: rgb(0,0,0);\n"
                                      "color: rgb(255, 255, 255);")
        self.bigblack.show()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.killtheblack)
        self.timer.start(3000)


    def ing(self):
        img_order = np.load('disorder.npy').copy()
        img_table = np.load('table.npy').copy()
        img_order = img_order.reshape(img_order.shape[0]*img_order.shape[1], 1)
        imgs = np.load('imgbox.npy').copy()
        img_csvpth = np.load('pths.npy').copy()
        img_recond = os.path.basename(img_csvpth[0])
        img_pref = os.path.basename(img_csvpth[1])
        #self.findandshow(img_order[0], img_table, imgs)


    def findandshow(self, pth_in_tbl, table, imgs):
        [psa, psb] = np.where(table == pth_in_tbl)
        len_b = len(imgs[0])
        psx = psa[0]//len_b
        psy = psa[0] - len_b * psx
        psz = psb[0]
        pix = QPixmap(imgs[psx][psy][psz])
        self.imgshow.setPixmap(pix)

    def lightdark(self):
        self.bigblack = QPushButton(self)
        self.bigblack.setObjectName(u"bigblack")
        self.bigblack.setGeometry(QRect(0, 0, 1920, 1080))
        self.bigblack.setStyleSheet(u"font: 14pt \"Cascadia Code\";")
        self.bigblack.setStyleSheet(u"font: 16pt \"Segoe Fluent Icons\";\n"
                                    "background-color: rgb(0,0,0);\n"
                                    "color: rgb(255, 255, 255);")

        self.bigblack.show()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.killtheblack2)
        self.timer.start(60000)

    def imgsss(self):
        self.pushButton_4.deleteLater()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.killtheblack3)
        self.timer.start(60000)

    def next_img(self, x):
        self.pushButton_2.setEnabled(False)
        self.prefer.setText(QCoreApplication.translate("Form", u"Pref : ", None))
        self.reprod.setText(QCoreApplication.translate("Form", u"Reprod : ", None))
        img_order = np.load('disorder.npy').copy()
        img_table = np.load('table.npy').copy()
        img_order = img_order.reshape(img_order.shape[0] * img_order.shape[1], 1)
        imgs = np.load('imgbox.npy').copy()
        self.findandshow(img_order[x], img_table, imgs)
        self.showdetials(x)
        global ct
        if ct!=0 and ct % (len(imgs)*len(imgs[0][0])) == 0:
            self.lightdark()
        ct += 1
        global T
        T =0
    def showdetials(self, ct):

        img_order = np.load('disorder.npy').copy()
        img_order = img_order.reshape(img_order.shape[0] * img_order.shape[1], 1)
        if ct < img_order.shape[0] * img_order.shape[1]-1:
            self.img_count.setText(QCoreApplication.translate("Form", u"C : %s" % (ct + 1), None))
            self.present_infor.setText(QCoreApplication.translate("Form", u"%s" % img_order[ct], None))
            self.next_infor.setText(QCoreApplication.translate("Form", u"Next : %s" % img_order[ct + 1], None))
        else:
            self.img_count.setText(QCoreApplication.translate("Form", u"C : %s" % (ct + 1), None))
            self.present_infor.setText(QCoreApplication.translate("Form", u"%s" % img_order[ct], None))
            self.next_infor.setText(QCoreApplication.translate("Form", u"Over", None))


    def previous_img(self, x):
        global ct
        img_order = np.load('disorder.npy').copy()
        img_table = np.load('table.npy').copy()
        img_order = img_order.reshape(img_order.shape[0] * img_order.shape[1], 1)
        imgs = np.load('imgbox.npy').copy()
        scorepths = np.load('pths.npy').copy()
        [psa1, psb1] = np.where(img_table == img_order[ct-2])
        datas_p = pd.read_csv(scorepths[1], index_col=0)
        scorepths = np.load('pths.npy').copy()
        [psa2, psb2] = np.where(img_table == img_order[ct - 2])
        datas_r = pd.read_csv(scorepths[0], index_col=0)
        p1 = datas_p.iloc[psa1, psb1].values
        p2 = datas_r.iloc[psa2, psb2].values
        self.prefer.setText(QCoreApplication.translate("Form", u"Pref : %d"%p1[0][0], None))
        self.reprod.setText(QCoreApplication.translate("Form", u"Reprod : %d"%p2[0][0], None))

        self.findandshow(img_order[x-2], img_table, imgs)
        self.showdetials(x-2)
        ct -= 1
        global T
        T = 0
    def killtheblack(self):
        self.bigblack.deleteLater()
        self.timer.stop()
        self.ing()

    def killtheblack2(self):
        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.setObjectName(u"pushButton_3")
        self.pushButton_4.setGeometry(QRect(960, 540, 141, 51))
        self.pushButton_4.setStyleSheet(u"font: 16pt \"Segoe Fluent Icons\";\n"
                                        "background-color: rgb(182, 182, 182);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Next", None))
        self.pushButton_4.show()
        self.pushButton_4.clicked.connect(self.imgsss)
        self.timer.stop()

    def killtheblack3(self):
        self.bigblack.deleteLater()
        self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow4()
    myWin.show()
    myWin.showFullScreen()
    sys.exit(app.exec())

