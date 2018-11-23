import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog,  QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from Crypto.Cipher import AES
from PyQt5.QtGui import QIcon
from binascii import b2a_base64, a2b_base64
from PyQt5.QtWidgets import *
import random
import string 
import time
import datetime
import os
#from folder_four import *
import win32com.client

class Text_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Text_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowIcon(QIcon('logo.ico'))
        MainWindow.setStyleSheet("#MainWindow{border-image:url(logo2.jpg);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 120, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 200, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 100, 231, 381))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(500, 100, 241, 381))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 261, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 130, 31, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 210, 31, 31))
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(320, 300, 161, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 260, 51, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 350, 111, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 70, 92, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 70, 92, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(300, 430, 191, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.encrypt_1)
        self.pushButton_2.clicked.connect(self.decrypt_1)
        self.pushButton_3.clicked.connect(self.random)
        self.pushButton_4.clicked.connect(self.showfile)
        self.pushButton_5.clicked.connect(self.savefile)
        self.pushButton_6.clicked.connect(self.jump)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文本加解密"))
        self.pushButton.setText(_translate("MainWindow", "加密"))
        self.pushButton_2.setText(_translate("MainWindow", "解密"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.07563pt;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.07563pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">文本加解密</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">→</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">←</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.07563pt;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">秘钥</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "生成随机秘钥"))
        self.pushButton_4.setText(_translate("MainWindow", "打开文件"))
        self.pushButton_5.setText(_translate("MainWindow", "保存文件"))
        self.pushButton_6.setText(_translate("MainWindow", "点击加载当前USB信息"))
    def showfile(self):
         filename, _ = QFileDialog.getOpenFileName(self.pushButton_4, '打开文件', './')
         if filename:
            file = open(filename)
            data = str(file.read()) 
            self.textEdit.setText(data)
    def savefile(self):
        key=str(self.textEdit_3.toPlainText())
        ciphertext=str(self.textEdit_2.toPlainText())
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d--%H:%M:%S')
        f=open("文本加解密.txt",'a')
        f.write("加密文本是：\r\n")
        f.write(nowTime)
        f.write("\r\n")
        f.write(ciphertext)
        f.write("秘钥是：\r\n")
        f.write(key)
        f.write("\r\n")
        f.write(nowTime)
        f.write("\r\n")
        f.close
        #key=str(self.textEdit_3.toPlainText())
        #ciphertext=str(self.textEdit_2.toPlainText())
       
    def random(self):
        randomlist=''.join(random.sample(string.ascii_letters + string.digits, 8))
        self.textEdit_3.setText(randomlist)
    def encrypt_1(self):
        text = str(self.textEdit.toPlainText())
        key = str(self.textEdit_3.toPlainText())
        class Prpcrypt(object):
            def __init__(self,key):
                self.mode = AES.MODE_CBC
                self.key = self.pad_key(key)
 
            def pad(self,text):
                text = bytes(text,encoding="utf8")
                while len(text) % 16 != 0:
                    text += b'\0'
                return text
 
            def pad_key(self,key):
                key = bytes(key, encoding="utf8")
                while len(key) % 16 != 0:
                    key += b'\0'
                return key
 
            def encrypt(self,text):
                texts = self.pad(text)
                aes = AES.new(self.key, self.mode,self.key)
                res = aes.encrypt(texts)
                return str(b2a_base64(res),encoding= "utf-8")
            
        self.textEdit_2.setText(Prpcrypt(key).encrypt(text))  
    def decrypt_1(self):
        key = str(self.textEdit_3.toPlainText())
        text = str(self.textEdit_2.toPlainText())
        class Prpcrypt(object):
            def __init__(self,key):
                self.mode = AES.MODE_CBC
                self.key = self.pad_key(key)
 
            def pad(self,text):
                text = bytes(text,encoding="utf8")
                while len(text) % 16 != 0:
                    text += b'\0'
                return text
 
            def pad_key(self,key):
                key = bytes(key, encoding="utf8")
                while len(key) % 16 != 0:
                    key += b'\0'
                return key 
            def decrypt(self,text):
                texts = a2b_base64(self.pad(text))
                aes = AES.new(self.key, self.mode,self.key)
                res = str(aes.decrypt(texts),encoding="utf8")
                return res
        self.textEdit.setText(Prpcrypt(key).decrypt(text))
    def jump(self):
        self.textEdit.setText("当前USB信息：")
        wmi = win32com.client.GetObject("winmgmts:")
        for usb in wmi.InstancesOf("Win32_USBHub"):
            self.textEdit.append(usb.DeviceID)
            #print(usb.DeviceID)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    MainWindow = QtWidgets.QMainWindow()
    ui = Text_MainWindow()
    #ui_folder = folder_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

