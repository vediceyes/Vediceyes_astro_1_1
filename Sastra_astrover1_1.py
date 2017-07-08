import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import swisseph as swe
import collections
from Swiss_eph_constants import *
from geopy.geocoders import Nominatim
from ChartCalculations import Chart


import ui_samainwindow
import sys


class UI(QMainWindow, ui_samainwindow.Ui_SAMainWindow,Chart,Nominatim):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.__index = 0
        self.setupUi(self)

        #Class creation
        self.geolocator = Nominatim(scheme='http')
        self.Hscope = Chart()

        # Object connections:

        self.setEPH.clicked.connect(self.setEPHLocation)
        self.CalcBirth.clicked.connect(self.CalculateBirth)


    def setEPHLocation(self):


        self.location = self.geolocator.geocode(self.locstring.text())
        self.Hscope.Setup_eph(self.location.latitude, self.location.longitude)

        self.latDisplay.setText(str(self.location.latitude))
        self.longDisplay.setText(str(self.location.longitude))


    def CalculateBirth(self):


        year=

        self.Bday_accurate = self.Hscope.DateTime(1983, 11, 7, 9, 22, 0)


















app = QApplication(sys.argv)

window = UI()
window.show()
app.exec_()

