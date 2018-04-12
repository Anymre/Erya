import itchat
#import win32con,win32gui
#import win32clipboard as cb
#import win32con
#import tkinter
#import tkinter.messagebox
import time
#import chardet
import threading
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QListWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QClipboard
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QListWidget, QWidget, QLineEdit, QDateTimeEdit, QVBoxLayout, QHBoxLayout \
        , QGridLayout, QLabel
from PyQt5.QtCore import Qt, QDateTime
#import os
#from widgets import  MainWidget
#from main import  MainWindow
class Erya(object):
    UserName=''
    def getter(self):
        return Username
    @itchat.msg_register(itchat.content.TEXT,isMpChat=True)
    def print_content(msg):
        a=msg['Text']
        print(a.split('<', 2)[0] )
    def getMps():
            mps = itchat.get_mps()
            mps=itchat.search_mps(name='tkBank')
            #print(mps)
            userName = mps[0]['UserName']
            #itchat.send(msg=question,toUserName = userName)
            return userName

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()
        self.addClipbordListener()


    def addClipbordListener(self):
        clipboard = QApplication.clipboard()
        clipboard.dataChanged.connect(self.widget.onClipboradChanged)


    def init(self):
        self.text = QTextEdit('主窗口')
        self.widget = MainWidget()
        self.setCentralWidget(self.widget)
        self.setGeometry(0, 0, 0, 0)
        self.setWindowTitle('监听粘贴板')
        self.show()
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        grid = QGridLayout()
        vlayout.addLayout(grid)
        vlayout.addStretch(1)
        self.setLayout(vlayout)


    def onClipboradChanged(self):
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        if text:
            content = str(text)
            itchat.send(msg=content,toUserName = hello.UserName)

if __name__ == '__main__':
    #with open(picDir, 'wb') as f:
        #f.write(qrStorage.getvalue())
    #itchat.utils.print_qr('D:/1.png')
    itchat.auto_login(hotReload=True)
    threading._start_new_thread(itchat.run, ())
    #_thread.start_new_thread(itchat.run())
    print('开始检测')
    hello=Erya()
    hello.UserName=Erya.getMps()
    app = QApplication(sys.argv)
    window =MainWindow()
    sys.exit(app.exec_())


            #question=Erya.gettext().decode('GB2312')
            #Erya.getMps(question)
            #itchat.configured_reply()   
        #time.sleep(0.5)
