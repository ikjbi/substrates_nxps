from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# Dimensions
#Start position of window when opening up
xstart = ystart = 50
# Dimensions of the window
width = 1200; height = 800
xcenter = width/2
ycenter = width/2


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(xstart, ystart, width, height)
        self.setWindowTitle('Substrate Database - NXP    S')
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first label")
        self.label.move(xcenter-50, 50)

        self.btn_1 = QtWidgets.QPushButton(self)
        self.btn_1.setText("Press me")
        self.btn_1.move(xcenter-200, 50)
        self.btn_1.clicked.connect(self.clicked_btn)

    def clicked_btn(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
   app = QApplication(sys.argv)
   win = MyWindow()
   win.show()
   sys.exit(app.exec_())

window()