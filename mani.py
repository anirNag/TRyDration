import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLineEdit, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic
from matplotlib import pyplot as plt
import numpy as np

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('idea.ui', self)

        self.apple = self.findChild(QPushButton, 'apple')
        if self.apple:
            self.apple.setIcon(QIcon(QPixmap("apple.png").scaled(120, 120)))

        self.google = self.findChild(QPushButton, 'google')
        if self.google:
            self.google.setIcon(QIcon(QPixmap("google.png").scaled(120, 120)))

        self.linedit = self.findChild(QLineEdit, 'lineEdit')

        self.sign_button = self.findChild(QPushButton, 'sign')
        self.sign_button.clicked.connect(self.open_main_window)

        self.main_window = None
        self.user_name = None  # Initialize user_name attribute

        self.show()

    def open_main_window(self):
        self.user_name = self.linedit.text().strip()
        
        if not self.main_window:
            self.main_window = MainWindow(self.user_name)  # Pass username to MainWindow
            self.close()

        self.main_window.show()


class MainWindow(QMainWindow):
    def __init__(self, user_name):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.user_name = user_name  # Store username in MainWindow instance

        self.show()



def login():
    app = QApplication(sys.argv)
    main_window = LoginWindow()
    sys.exit(app.exec_())

# Execute login window
login()
