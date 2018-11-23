import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from text_five import *
from folder_four import *

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 523)
        MainWindow.setWindowIcon(QIcon('logo.ico'))
        MainWindow.setStyleSheet("#MainWindow{border-image:url(logo1.jpg);}")
        #MainWindow.setStyleSheet("#MainWindow{background-color: yellow}")
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 120, 91, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 230, 91, 51))
        self.label_2.setObjectName("label_2")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(170, 350, 111, 51))
        self.login.setObjectName("login")
        self.register_2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_2.setGeometry(QtCore.QRect(430, 350, 111, 51))
        self.register_2.setObjectName("register_2")
        self.mainwindows = QtWidgets.QLabel(self.centralwidget)
        self.mainwindows.setGeometry(QtCore.QRect(190, 20, 371, 41))
        self.mainwindows.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mainwindows.setObjectName("mainwindows")
        self.user = QtWidgets.QLineEdit(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(220, 110, 411, 51))
        self.user.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.user.setStyleSheet("font: 20pt \"Adobe Arabic\";")
        self.user.setText("")
        self.user.setMaxLength(18)
        self.user.setFrame(True)
        self.user.setCursorPosition(0)
        self.user.setDragEnabled(False)
        self.user.setClearButtonEnabled(True)
        self.user.setObjectName("user")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(220, 220, 411, 51))
        self.password.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.password.setStyleSheet("font: 20pt \"Adobe Arabic\";")
        self.password.setText("")
        self.password.setMaxLength(18)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setCursorPosition(0)
        self.password.setObjectName("password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.login.clicked.connect(self.judge)
        self.register_2.clicked.connect(self.close)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "信息安全处理系统"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">账号：</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">密码：</span></p></body></html>"))
        self.login.setText(_translate("MainWindow", "登录"))
        self.register_2.setText(_translate("MainWindow", "取消"))
        self.mainwindows.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">登录界面</span></p></body></html>"))
        self.user.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\"></span></p></body></html>"))
        self.user.setPlaceholderText(_translate("MainWindow", "请输入账号"))
        self.password.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\"></span></p></body></html>"))
        self.password.setPlaceholderText(_translate("MainWindow", "请输入密码"))
    def judge(self):
        login_user = self.user.text()
        login_password = self.password.text()
        if login_user == 'admin' and login_password == '123456':
            ui_text.show()
            ui_folder.show()
            #os.system("text_five.py")
            MainWindow.close()
        else:
            QMessageBox.warning(self, "滴滴滴！！！", "账号或密码错误", QMessageBox.Yes)
            self.login.setFocus()  
    def close(self):
        MainWindow.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui_text = Text_MainWindow()
    ui_folder = Folder_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
