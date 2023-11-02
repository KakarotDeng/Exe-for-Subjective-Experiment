import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from start import *
import cv2
import numpy as np
import os
import csv
import time
import pandas as pd
class MyWindow3(QWidget,Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow3, self).__init__(parent)
        self.setupUi(self)
        self.tableok.clicked.connect(self.pack)



    def pack(self):
        name = self.lineEdit.text()
        savepath = self.lineEdit_2.text()
        box = np.load('imgbox.npy').copy()
        cmfs = np.load('cmf.npy').copy()
        img_order = np.load('disorder.npy').copy()
        img_order = img_order.reshape(img_order.shape[0] * img_order.shape[1], 1)
        lights = np.load('lightdata.npy').copy()
        timelog = time.localtime()
        ths = ['' for _ in range(len(box[0][0]) + 1)]

        disorder_list = np.load('disorder.npy')

        score_path1 = savepath+'\\'+name+'_reduction'+'_'+'%s'%timelog.tm_year+'_'+'%s'%timelog.tm_mon+'_'+'%s'%timelog.tm_mday+'_'+'%s'%timelog.tm_hour+'.csv'
        score_path2 = savepath+'\\'+name+'_preference'+'_'+'%s'%timelog.tm_year+'_'+'%s'%timelog.tm_mon+'_'+'%s'%timelog.tm_mday+'_'+'%s'%timelog.tm_hour+'.csv'
        score_path3 = savepath+'\\'+name+'_img_list'+'_'+'%s'%timelog.tm_year+'_'+'%s'%timelog.tm_mon+'_'+'%s'%timelog.tm_mday+'_'+'%s'%timelog.tm_hour+'.csv'

        data1 = pd.DataFrame(img_order)
        data1.to_csv(score_path3)

        score_paths = [score_path1, score_path2]
        np.save('pths', score_paths)

        with open(score_path1, mode='w', newline='', encoding='utf8') as cf:
            wf = csv.writer(cf)

            for i in range(1, len(box[0][0]) + 1):
                ths[i] = os.path.basename(box[0][0][i - 1])
            wf.writerow(ths)
            for i in range(lights.shape[0]):
                for j in range(len(cmfs)):
                    wf.writerow([cmfs[j] + ' ' + lights[i]])

        with open(score_path2, mode='w', newline='', encoding='utf8') as cf:
            wf = csv.writer(cf)

            for i in range(1, len(box[0][0]) + 1):
                ths[i] = os.path.basename(box[0][0][i - 1])
            wf.writerow(ths)
            for i in range(lights.shape[0]):
                for j in range(len(cmfs)):
                    wf.writerow([cmfs[j] + ' ' + lights[i]])

        from exppage import MyWindow4
        self.close()
        self.W3 = MyWindow4()
        self.W3.showFullScreen()
        self.W3.show()









if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow3()
    myWin.show()

    #myWin.showFullScreen()
    sys.exit(app.exec())




