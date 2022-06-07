from turtle import title
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100, 100, 1200, 800)

    window.setWindowTitle('NXPS - Substrate Database')

    label = QLabel(window)
    label.setText("Substrate Database")
    label.setFont(QFont('Arial', 16))
    label.move(50, 100)


    window.show()
    app.exec_()

if __name__ == '__main__':
    main()