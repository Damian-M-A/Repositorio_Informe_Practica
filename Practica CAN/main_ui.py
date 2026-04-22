import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
import ui_main
import ui_test
import random

import numpy as np
import pyqtgraph as pg
from datos import extraer_velocidad, extraer_combustible

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.vel = extraer_velocidad()
        self.tanq = extraer_combustible()
        self.ui = ui_test.Ui_MainWindow()
        self.ui.setupUi(self)
        

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.velocidad)
        self.timer.start(300) 

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tanque)
        self.timer.start(300)

        self.timerFuel = QTimer(self)
        self.timerFuel.timeout.connect(self.progressbar)
        self.timerFuel.start(300)  


    
    def progressbar(self):
        value = random.choice(self.vel)         
        stop = max(0.0, min(value / 100.0, 1.0))

        self.ui.frameFuelRing.setStyleSheet(f"""
                QFrame {{
                    border-radius: 100px;
                    border: 2px solid #00E676;
                    background: qconicalgradient(
                        cx:0.5, cy:0.5,
                        angle:90,
                        stop:0 rgba(0,230,118,255),
                        stop:{stop} rgba(0,230,118,255),
                        stop:{stop} rgba(0,0,0,0),
                        stop:1 rgba(0,0,0,0)
                    );
                }}
            """)
    def tanque(self):
        valor = random.choice(self.vel)
        self.ui.combustibleLCD.display(valor)
        self.ui.fuelBar.setValue(valor)
        self.ui.updateFuel(valor)
        ##print(valor)

    def velocidad(self):
        self.ui.velocimetro.setMinimum(0)
        self.ui.velocimetro.setMaximum(240)
        valor =random.choice(self.vel)
        self.ui.velocimetro.setValue(valor)
        if 0 <= valor <= 240:
            self.ui.updateSpeed(valor)

        
                
                

        

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = MainWindow()
    widget.addWidget(mainwindow)
    #widget.setWindowFlags(Qt.FramelessWindowHint)
    #widget.setAttribute(Qt.WA_TranslucentBackground)
    widget.show()
    widget.setFixedHeight(600)
    widget.setFixedWidth(1024)
    
    sys.exit(app.exec_())