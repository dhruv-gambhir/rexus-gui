from PyQt5.QtWidgets import *
from PyQt5 import uic
import yuz

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui', self)
        self.show()

        

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    app.exec_()






    