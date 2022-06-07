from mimetypes import init
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow,  QWidget, QFrame, QPushButton, QCheckBox
from PyQt5.QtCore import QRect
import sys


def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.frame = QFrame(self)
        self.button = QPushButton("Toggle", self)
        self.button.setCheckable(True)
        self.button.setChecked(True)
        self.switched = False
        self.vPolicy = None
        # self.button.setStyleSheet("background-color: lightBlue;")
        self.button.setStyleSheet("""
        QPushButton{
            background-color: #BBB;
            border: none;
            padding: 2px;
        }
        QPushButton:checked, QPushButton:hover{
            font-style:italic;
            background-color:lightBlue;
        }""")

__init__()