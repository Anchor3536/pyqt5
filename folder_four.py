import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog,  QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from Crypto.Cipher import AES
from PyQt5.QtGui import QIcon
from binascii import b2a_base64, a2b_base64 
import random
import string 
import time
import datetime
import os


class Folder_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Folder_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowIcon(QIcon('logo.ico'))
        MainWindow.setStyleSheet("#MainWindow{border-image:url(logo3.jpg);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt.setGeometry(QtCore.QRect(350, 350, 101, 41))
        self.encrypt.setObjectName("encrypt")
        self.decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt.setGeometry(QtCore.QRect(350, 470, 101, 41))
        self.decrypt.setObjectName("decrypt")
        self.filecontent = QtWidgets.QTextEdit(self.centralwidget)
        self.filecontent.setGeometry(QtCore.QRect(60, 330, 231, 231))
        self.filecontent.setObjectName("filecontent")
        self.ciphertext = QtWidgets.QTextEdit(self.centralwidget)
        self.ciphertext.setGeometry(QtCore.QRect(500, 330, 241, 231))
        self.ciphertext.setObjectName("ciphertext")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 261, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 360, 31, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 480, 31, 31))
        self.label_3.setObjectName("label_3")
        self.key = QtWidgets.QTextEdit(self.centralwidget)
        self.key.setGeometry(QtCore.QRect(500, 140, 241, 71))
        self.key.setObjectName("key")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 240, 111, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(0, 0, 92, 28))
        self.open.setObjectName("open")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(90, 0, 92, 28))
        self.save.setObjectName("save")
        self.folderroute = QtWidgets.QTextEdit(self.centralwidget)
        self.folderroute.setGeometry(QtCore.QRect(60, 180, 231, 51))
        self.folderroute.setObjectName("folderroute")
        self.route = QtWidgets.QLabel(self.centralwidget)
        self.route.setGeometry(QtCore.QRect(60, 160, 121, 21))
        self.route.setObjectName("route")
        self.route_2 = QtWidgets.QLabel(self.centralwidget)
        self.route_2.setGeometry(QtCore.QRect(60, 230, 121, 21))
        self.route_2.setObjectName("route_2")
        self.route_3 = QtWidgets.QLabel(self.centralwidget)
        self.route_3.setGeometry(QtCore.QRect(60, 310, 121, 21))
        self.route_3.setObjectName("route_3")
        self.route_4 = QtWidgets.QLabel(self.centralwidget)
        self.route_4.setGeometry(QtCore.QRect(500, 110, 101, 21))
        self.route_4.setObjectName("route_4")
        self.route_5 = QtWidgets.QLabel(self.centralwidget)
        self.route_5.setGeometry(QtCore.QRect(500, 310, 61, 21))
        self.route_5.setObjectName("route_5")
        self.file = QtWidgets.QTextEdit(self.centralwidget)
        self.file.setGeometry(QtCore.QRect(60, 250, 231, 61))
        self.file.setObjectName("file")
        self.suffix = QtWidgets.QTextEdit(self.centralwidget)
        self.suffix.setGeometry(QtCore.QRect(60, 130, 231, 31))
        self.suffix.setObjectName("suffix")
        self.route_6 = QtWidgets.QLabel(self.centralwidget)
        self.route_6.setGeometry(QtCore.QRect(60, 100, 191, 31))
        self.route_6.setObjectName("route_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.encrypt.clicked.connect(self.encrypt_1)
        self.decrypt.clicked.connect(self.decrypt_1)
        self.pushButton_3.clicked.connect(self.random)
        self.open.clicked.connect(self.openfile)
        self.open.clicked.connect(self.showfile)
        self.open.clicked.connect(self.showfilecontent)
        self.save.clicked.connect(self.savefile)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件夹加解密"))
        self.encrypt.setText(_translate("MainWindow", "加密"))
        self.decrypt.setText(_translate("MainWindow", "解密"))
        self.filecontent.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.07563pt;\"><br /></p></body></html>"))
        self.ciphertext.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.07563pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">文件批处理</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">→</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">←</span></p></body></html>"))
        self.key.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.07563pt;\"><br /></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "生成随机秘钥"))
        self.open.setText(_translate("MainWindow", "打开"))
        self.save.setText(_translate("MainWindow", "保存"))
        self.route.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">文件夹路径：</span></p></body></html>"))
        self.route_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">可加密文件：</span></p></body></html>"))
        self.route_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">可加密内容：</span></p></body></html>"))
        self.route_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">随机秘钥：</span></p></body></html>"))
        self.route_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">密文：</span></p></body></html>"))
        self.file.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.07563pt;\"><br /></p></body></html>"))
        self.suffix.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.07563pt;\"><br /></p></body></html>"))
        self.suffix.setPlaceholderText(_translate("MainWindow", "格式: .txt"))
        self.route_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">输入文件格式后缀：</span></p></body></html>"))
    def openfile(self):
        folder=QFileDialog.getExistingDirectory(self.open, '打开文件夹', './')
        self.folderroute.setText(folder)
    def showfile(self):
        path=(self.folderroute.toPlainText())
        back=(self.suffix.toPlainText())
        dirs = os.listdir(path)                    # 获取指定路径下的文件
        self.file.setText("可加密文件有：")
        for i in dirs:                             # 循环读取路径下的文件并筛选输出
            if os.path.splitext(i)[1] == back:# 筛选文件
                self.file.append(i)
            '''else:
                self.file.setText("格式错误或没有该类型的文件")'''
                #print(i)
                #self.file.append(i)
    def showfilecontent(self):
        path=(self.folderroute.toPlainText())
        self.filecontent.setText("文件内容：")
        back=(self.suffix.toPlainText())
        files= os.listdir(path) #得到文件夹下的所有文件名称    
        for file in files: #遍历文件夹  
            if os.path.splitext(file)[1] == back: 
                #print(file)
                if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开  
                    f = open(path+"/"+file); #打开文件  
                    iter_f = iter(f); #创建迭代器  
                    a = ""  
                    for line in iter_f: #遍历文件，一行行遍历，读取文本  
                        a = a + line
                    self.filecontent.append(a)
                    #print(a) #每个文件的文本存到list中   
                    
    def savefile(self):
        key=str(self.key.toPlainText())
        ciphertext=str(self.ciphertext.toPlainText())
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d--%H:%M:%S')
        f=open("文件夹加解密.txt",'a')
        f.write("加密文件夹内容是：\r\n")
        f.write(nowTime)
        f.write("\r\n")
        f.write(ciphertext)
        f.write("秘钥是：\r\n")
        f.write(key)
        f.write("\r\n")
        f.write(nowTime)
        f.write("\r\n")
        f.close

    def random(self):
        randomlist=''.join(random.sample(string.ascii_letters + string.digits, 10))
        self.key.setText(randomlist)
    def encrypt_1(self):
        text = str(self.filecontent.toPlainText())
        key = str(self.key.toPlainText())
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
            
            
        self.ciphertext.setText(Prpcrypt(key).encrypt(text))  
    def decrypt_1(self):
        key = str(self.key.toPlainText())
        text = str(self.ciphertext.toPlainText())
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
        self.filecontent.setText(Prpcrypt(key).decrypt(text))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    MainWindow = QtWidgets.QMainWindow()
    ui = Folder_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

