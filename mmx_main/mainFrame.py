import sys

from PyQt5.QtGui import QFont

import mmx_Frame.gridFrame as g
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLineEdit, QDesktopWidget, QWidget, QPushButton
from PyQt5.uic.properties import QtWidgets, QtGui, QtCore

'''
简单的计算器，通过pyqt5设置布局，这个小程序中采用gridlayout网格布局
setWindowTitle设置框架名，resize为设置组件大小，setFixedSize为固定了组件大小，禁用最大化按钮
在这个计算器中采用eval处理计算
这个小程序中把功能和界面分开，mainFrame.py处理功能，gridFrame.py处理页面
mainFrame.py

'''

class MyFrame(QWidget):

     def __init__(self):
      super(MyFrame, self).__init__()
      #布局设置
      self.initUI()

     def initUI(self):
         self.string = ''  # 作为容器去计算
         self.number = '0'  # 初始值

         #题目
         self.setWindowTitle('简易计算器')
         #大小并且固定大小禁用最大化窗口
         self.resize(400, 300)
         self.setFixedSize(self.width(), self.height())

         #设置组件处于屏幕的中央
         self.center()

         #调用gridFrame.py完成布局，具体布局请看gridFrame
         g.GridFrame.grid(self)


     #位于中心函数
     def center(self):
         # 用来获取显示屏幕的大小
         screen = QDesktopWidget().screenGeometry()
         # 用来获得组件的大小
         size = self.geometry()
         # 移动到屏幕的中间
         self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

     #按钮点击后发出的信号，获取并且处理

     def buttonClicked(self):
         # sender = self.sender();  # 确定信号发送者
         # self.display.setText(sender.text())#确定text为name
         text = self.sender().text()

         #in就会置为0，==会在后面加上字符
         if text == '+-*/':
             self.string = self.string + self.number + text
             self.number = '0' #置空number
         elif text == '=':
             self.string = self.string + self.number
             #处理计算,用eval做简单计算
             self.number = str(eval(self.string))
             self.string = ''

         elif text == '.':
             self.number = self.number + text

         elif text == 'Clear':
             self.number = '0'
         elif text == 'Close':
             self.close()
         elif text == 'Back':
             print(text)

             self.number = self.number.Substring(0, self.number.Length - 1) # 删去最后一位
             print(self.number)

         else:
             if self.number == '0':
                 self.number = ''
             self.number = self.number + text
         self.display.setText(self.number)




if __name__ =="__main__":
    app = QApplication(sys.argv)
    myframe = MyFrame()
    myframe.show()
    sys.exit(app.exec_())