import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from inputa import *
import cv2
import numpy as np
import os


class MyWindow(QWidget,Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.inputcheck.clicked.connect(self.checkvalid)
        self.inputok.clicked.connect(self.nextpage)
        if os.path.exists('originpth.npy') == True:
            path_of_imgs = np.load('originpth.npy')
            self.inputpathedit.setText(path_of_imgs[0])


    def checkvalid(self):
        if os.path.exists('originpth.npy') == False:
            path_of_imgs = self.inputpathedit.toPlainText().split()
            np.save('originpth.npy',path_of_imgs)
        if os.path.exists('originpth.npy') == True:
            path_of_imgs = np.load('originpth.npy')
            self.inputpathedit.setText(path_of_imgs[0])
            a=1


        cmfs = os.listdir(path_of_imgs[0])
        lights = os.listdir(path_of_imgs[0]+'\\'+cmfs[0])
        imgs = os.listdir(path_of_imgs[0]+'\\'+cmfs[0]+'\\'+lights[0])
        imgs_box = [[] for _ in range(len(cmfs))]

        for i in range(len(cmfs)):
            imgs_box[i] = [[''for _ in range(len(imgs))] for _ in range(len(lights))]
            for j in range(len(lights)):
                for k in range(len(imgs)):
                    lights = os.listdir(path_of_imgs[0] + '\\' + cmfs[i])
                    imgs = os.listdir(path_of_imgs[0] + '\\' + cmfs[i] + '\\' + lights[j])
                    imgs_box[i][j][k] = path_of_imgs[0]+'\\'+cmfs[i]+'\\'+lights[j]+'\\'+imgs[k]


        cmfdata = self.inputcmf.toPlainText().split()
        lightdata = self.inputlight.toPlainText().split()
        num_img = self.inputnum.toPlainText().split()
        num_get = len(cmfs)*len(lights)*len(imgs)


        if len(num_img)!=0 and num_img[0].isdigit()==False:
            txt_toshow = 'Error : Wrong Form of Input Number'
            print('no')
        elif len(cmfdata)*len(lightdata)*int(num_img[0]) != num_get:
            txt_toshow = 'Error : The Number of Images Is Wrong'
        else:
            txt_toshow = 'CMf type : %s, Light type : %s, total images account : %d ' % (cmfdata, lightdata, num_get)

        np.save('imgbox.npy', imgs_box)
        np.save('cmf.npy', cmfdata)
        np.save('lightdata.npy', lightdata)

        self.showifinputok.setText(txt_toshow, )




    def nextpage(self):
        self.close()
        from tablepage import MyWindow2
        self.W1 = MyWindow2()
        self.W1.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec())
