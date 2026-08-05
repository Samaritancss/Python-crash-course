#PyQt6 introduction
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt 

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool GUI")
        self.setGeometry(700, 300, 500, 500)  
        self.setWindowIcon(QIcon("nfl me.png"))  

        label = QLabel("Hello, PyQt6!", self)
        label.setFont(QFont("Arial", 16))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: blue;"
                            "background-color: yellow;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        label.setAlignment(Qt.AlignmentFlag.AlignTop)
        # label.setAlignment(Qt.AlignBottom)#vertically bottom
        # label.setAlignment(Qt.AlignVCenter)#vertically center
        # label.setAlignment(Qt.AlignRight)#horizontally right
        # label.setAlignment(Qt.AlignHCenter)#horizontally center
        # label.setAlignment(Qt.AlignLeft)#horizontally left
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)#center & top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)#center & bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # #Center & Center
        # label.setAlignment(Qt.AlignCenter)#Center & Center

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())