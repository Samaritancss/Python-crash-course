#PyQt5 layouts
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, Qlabel, Qwidget, QVBoxLayout, QHBoxlayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.initUI()

    




