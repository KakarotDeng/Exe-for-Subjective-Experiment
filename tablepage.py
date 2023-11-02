import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from output import *
import cv2
import numpy as np
import os
import random


class MyWindow2(QWidget,Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow2, self).__init__(parent)
        self.setupUi(self)
        self.generate.clicked.connect(self.showtable)
        self.tableok.clicked.connect(self.nextpage)

    def showtable(self):
        box = np.load('imgbox.npy').copy()
        cmfs = np.load('cmf.npy').copy()
        lights = np.load('lightdata.npy').copy()
        tableshow = [[''for _ in range(len(box[0][0]))] for _ in range(len(box)*len(box[0]))]
        for i in range(len(box[0])):
            for j in range(len(box)):
                for k in range(len(box[0][0])):
                    tableshow[i*len(box)+j][k] = cmfs[j]+' '+lights[i]+' '+os.path.basename(box[j][i][k])

        self.listWidget.clear()
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(tableshow))
        self.tableWidget.setColumnCount(len(tableshow[0]))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        for i in range(len(box)*len(box[0])):
            for j in range(len(box[0][0])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(tableshow[i][j]))



        disorderlist = [[''for _ in range(len(box)*len(box[0][0]))] for _ in range(len(box[0]))]
        for i in range(len(box[0])):
            imgs_order = np.arange(len(box[0][0])).tolist()
            random.shuffle(imgs_order)
            for j in range(len(box[0][0])):
                cmf_order = np.arange(len(box)).tolist()
                random.shuffle(cmf_order)
                for k in range(len(box)):
                    disorderlist[i][j*len(box)+k] = cmfs[cmf_order[k]]+' '+lights[i]+' '+os.path.basename(box[cmf_order[k]][i][imgs_order[j]])

        for i in range(len(box[0])):
            for j in range(len(box)*len(box[0][0])):
                self.listWidget.addItem(disorderlist[i][j])

        np.save('table.npy', tableshow)
        np.save('disorder.npy', disorderlist)


    def nextpage(self):

        from startmenu import MyWindow3
        self.close()
        self.W2 = MyWindow3()
        self.W2.show()





















if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow2()
    myWin.show()
    sys.exit(app.exec())
