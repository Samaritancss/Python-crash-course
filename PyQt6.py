# #PyQt6 introduction
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel
# from PyQt6.QtGui import QIcon
# from PyQt6.QtGui import QFont
# from PyQt6.QtCore import Qt 

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My cool GUI")
#         self.setGeometry(700, 300, 500, 500)  
#         self.setWindowIcon(QIcon("nfl me.png"))  

#         label = QLabel("Hello, PyQt6!", self)
#         label.setFont(QFont("Arial", 16))
#         label.setGeometry(0, 0, 500, 100)
#         label.setStyleSheet("color: blue;"
#                             "background-color: yellow;"
#                             "font-weight: bold;"
#                             "font-style: italic;"
#                             "text-decoration: underline;")
#         label.setAlignment(Qt.AlignmentFlag.AlignTop)
#         # label.setAlignment(Qt.AlignBottom)#vertically bottom
#         # label.setAlignment(Qt.AlignVCenter)#vertically center
#         # label.setAlignment(Qt.AlignRight)#horizontally right
#         # label.setAlignment(Qt.AlignHCenter)#horizontally center
#         # label.setAlignment(Qt.AlignLeft)#horizontally left
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)#center & top
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)#center & bottom
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
#         # #Center & Center
#         # label.setAlignment(Qt.AlignCenter)#Center & Center

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())

##########to insert picture#######
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel  # Fixed: Added QMainWindow import
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt  # Added Qt for alignment

class MainWindow(QMainWindow):  # Fixed: Now QMainWindow is properly imported
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")  # Added window title
        self.setGeometry(700, 300, 500, 500)
        
        # Create label
        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)
        
        # Load image
        pixmap = QPixmap("nfl me.png")
        
        # Check if image loaded successfully
        if not pixmap.isNull():
            label.setPixmap(pixmap)
            label.setScaledContents(True)
            
            # CORRECTED: Center the label within the window
            window_width = self.width()
            window_height = self.height()
            label_width = label.width()
            label_height = label.height()
            
            # Calculate center position
            x = (window_width - label_width) // 2
            y = (window_height - label_height) // 2
            
            # Set the label to center position
            label.setGeometry(x, y, label_width, label_height)
            
            # Alternative: Use move() instead of setGeometry()
            # label.move(x, y)
        else:
            label.setText("Image not found")
            label.setStyleSheet("color: red; font-size: 16px;")
            # Center the error message
            label.adjustSize()
            x = (self.width() - label.width()) // 2
            y = (self.height() - label.height()) // 2
            label.move(x, y)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
