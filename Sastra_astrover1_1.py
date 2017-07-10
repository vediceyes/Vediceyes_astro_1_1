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
import pytz
from pytz import timezone
import datetime
import openpyxl

from openpyxl import load_workbook


Timezone_list= []

Timezone_list= pytz.all_timezones

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

        self.Timezone.addItems(Timezone_list)
        self.setEPH.clicked.connect(self.setEPHLocation)
        self.CalcBirth.clicked.connect(self.CalculateBirth)


    def setEPHLocation(self):


        self.location = self.geolocator.geocode(self.locstring.text())
        self.Hscope.Setup_eph(self.location.latitude, self.location.longitude)

        self.latDisplay.setText(str(self.location.latitude))
        self.longDisplay.setText(str(self.location.longitude))


    def CalculateBirth(self):
        wb = load_workbook('BirthChart.xlsx')
        ws = wb.active

        year=self.DateInput.date().year()
        month=self.DateInput.date().month()
        day = self.DateInput.date().day()

        hour = self.TimeInput.time().hour()
        minute= self.TimeInput.time().minute()

        local_tz = timezone(self.Timezone.currentText())

        t = local_tz.localize(datetime.datetime(year, month, day, hour, minute))

        t_utc = t.astimezone(pytz.UTC)

        hour_utc= t_utc.hour
        minute_utc= t_utc.minute

        Bday_accurate = self.Hscope.DateTime(year, month, day, hour_utc, minute_utc, 0)

        (HouseDict, HousePosList) = self.Hscope.CaclHouses(Bday_accurate, self.location.latitude, self.location.longitude)

        self.Hscope.CalcPlanets(HouseDict, Bday_accurate, ws)

        self.Hscope.getASC(HouseDict)

        wb.save('BirthChart.xlsx')




app = QApplication(sys.argv)

window = UI()
window.show()
app.exec_()

