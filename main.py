from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui', self)
        self.show()

        # mock data
        self.M1V_lcd.display(5)
        self.M2V_lcd.display(5)
        self.M3V_lcd.display(4)
        self.M4V_lcd.display(4)
        self.M5V_lcd.display(5)
        self.M6V_lcd.display(5)

        self.M1A_lcd.display(12)
        self.M2A_lcd.display(10)
        self.M3A_lcd.display(10)
        self.M4A_lcd.display(10)
        self.M5A_lcd.display(10)
        self.M6A_lcd.display(12)

        self.M1amp_lcd.display(3)
        self.M2amp_lcd.display(2)
        self.M3amp_lcd.display(2)
        self.M4amp_lcd.display(2)
        self.M5amp_lcd.display(2)
        self.M6amp_lcd.display(3)

        self.dtLoad_lcd.display(10)
        self.armLoad_lcd.display(0)
        self.labLoad_lcd.display(5)
        self.overallLoad_lcd.display(15)

        self.fanOn.enabled = True

        self.batteryCapacity_lcd.display(100)
        self.batteryTemp_lcd.display(25)

        self.waterLevel_lcd.display(100)
        self.methaneGas_lcd.display(0)
        self.ambientLight_lcd.display(100)
        self.temperature_lcd.display(25)
        self.soilMoisture_lcd.display(100)
        self.npkSensor_lcd.display(100)

        self.s1_label.setText('S1')
        self.s2_label.setText('S2')
        self.s3_label.setText('S3')
        self.s4_label.setText('S4')
        self.s5_label.setText('S5')
        self.s6_label.setText('S6')


        scene = QtWidgets.QGraphicsScene(self)
        pixmap = QPixmap('resources/camera1.jpeg')
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.camera1.setScene(scene)

        scene = QtWidgets.QGraphicsScene(self)
        pixmap = QPixmap('resources/camera2.jpeg')
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.camera2.setScene(scene)

        scene = QtWidgets.QGraphicsScene(self)
        pixmap = QPixmap('resources/arm.jpeg')
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.armGraphic1.setScene(scene)






if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    app.exec_()






    