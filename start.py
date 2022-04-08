import os

from PyQt5 import QtCore, QtGui, QtWidgets
import main

calcText = '0'
mem = '0'
action = ""
isLastAction = False
def calc(symbol):
    global calcText
    global action
    global mem
    global isLastAction
    if symbol == '=' or "+" or "-" or "*" or "/":
        if action == '+':
            calcText = str(float(mem) + float(calcText))
        if action == '-':
            calcText = str(float(mem) - float(calcText))
        if action == '/':
            calcText = str(float(mem) / float(calcText))
        if action == '*':
            calcText = str(float(mem) * float(calcText))
    if symbol in ['-', '+', '/', '*', '=']:
        mem = calcText
        action = symbol
        isLastAction = True

    else:
        if isLastAction == True:
            calcText = ''
        if calcText != '0':
            calcText = calcText+symbol
        else:
            calcText = symbol
        isLastAction = False

def click(var):
   global calcText
   calc(var.text())
   ui.textOut.setText(calcText)


if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(lambda: click(ui.pushButton))
    ui.pushButton_2.clicked.connect(lambda: click(ui.pushButton_2))
    ui.pushButton_3.clicked.connect(lambda: click(ui.pushButton_3))
    ui.pushButton_4.clicked.connect(lambda: click(ui.pushButton_4))
    ui.pushButton_5.clicked.connect(lambda: click(ui.pushButton_5))
    ui.pushButton_6.clicked.connect(lambda: click(ui.pushButton_6))
    ui.pushButton_7.clicked.connect(lambda: click(ui.pushButton_7))
    ui.pushButton_8.clicked.connect(lambda: click(ui.pushButton_8))
    ui.pushButton_9.clicked.connect(lambda: click(ui.pushButton_9))
    MainWindow.show()
    sys.exit(app.exec_())
