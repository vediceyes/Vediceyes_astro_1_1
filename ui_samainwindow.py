# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'samainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SAMainWindow(object):
    def setupUi(self, SAMainWindow):
        SAMainWindow.setObjectName("SAMainWindow")
        SAMainWindow.resize(1046, 592)
        self.centralWidget = QtWidgets.QWidget(SAMainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(50, 40, 991, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 20, 401, 341))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(11, 11, 20, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.NameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NameInput.setObjectName("NameInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.NameInput)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.DateInput = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.DateInput.setObjectName("DateInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.DateInput)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.locstring = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.locstring.setObjectName("locstring")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.locstring)
        self.setEPH = QtWidgets.QPushButton(self.formLayoutWidget)
        self.setEPH.setObjectName("setEPH")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.setEPH)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_9)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.latDisplay = QtWidgets.QLabel(self.formLayoutWidget)
        self.latDisplay.setText("")
        self.latDisplay.setObjectName("latDisplay")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.latDisplay)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.longDisplay = QtWidgets.QLabel(self.formLayoutWidget)
        self.longDisplay.setText("")
        self.longDisplay.setObjectName("longDisplay")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.longDisplay)
        self.TimeInput = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.TimeInput.setObjectName("TimeInput")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.TimeInput)
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(460, 20, 521, 341))
        self.tableView.setObjectName("tableView")
        self.CalcBirth = QtWidgets.QPushButton(self.tab)
        self.CalcBirth.setGeometry(QtCore.QRect(140, 360, 99, 32))
        self.CalcBirth.setObjectName("CalcBirth")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        SAMainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(SAMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1046, 22))
        self.menuBar.setObjectName("menuBar")
        SAMainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(SAMainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        SAMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(SAMainWindow)
        self.statusBar.setObjectName("statusBar")
        SAMainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(SAMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SAMainWindow)

    def retranslateUi(self, SAMainWindow):
        _translate = QtCore.QCoreApplication.translate
        SAMainWindow.setWindowTitle(_translate("SAMainWindow", "MainWindow"))
        self.label.setText(_translate("SAMainWindow", "Name"))
        self.label_2.setText(_translate("SAMainWindow", "Date"))
        self.DateInput.setDisplayFormat(_translate("SAMainWindow", "M/d/yyyy"))
        self.label_4.setText(_translate("SAMainWindow", "Time"))
        self.label_3.setText(_translate("SAMainWindow", "Location"))
        self.setEPH.setText(_translate("SAMainWindow", "SetupEPH"))
        self.label_9.setText(_translate("SAMainWindow", "Enter: City, State, Country"))
        self.label_7.setText(_translate("SAMainWindow", "Long"))
        self.label_10.setText(_translate("SAMainWindow", "Lat"))
        self.TimeInput.setDisplayFormat(_translate("SAMainWindow", "hh:mm"))
        self.CalcBirth.setText(_translate("SAMainWindow", "Calculate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SAMainWindow", "Birth data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SAMainWindow", "Chart"))

