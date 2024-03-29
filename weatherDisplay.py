# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weatherDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets


class weatherUI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(389, 220)
        self.tempLabel = QtWidgets.QLabel(Form)
        self.tempLabel.setGeometry(QtCore.QRect(20, 70, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tempLabel.setFont(font)
        self.tempLabel.setObjectName("tempLabel")
        self.weatherLabel = QtWidgets.QLabel(Form)
        self.weatherLabel.setGeometry(QtCore.QRect(20, 140, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.weatherLabel.setFont(font)
        self.weatherLabel.setObjectName("weatherLabel")
        self.currentTempLabel = QtWidgets.QLabel(Form)
        self.currentTempLabel.setGeometry(QtCore.QRect(100, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currentTempLabel.setFont(font)
        self.currentTempLabel.setText("")
        self.currentTempLabel.setObjectName("currentTempLabel")
        self.currentWeatherLabel = QtWidgets.QLabel(Form)
        self.currentWeatherLabel.setGeometry(QtCore.QRect(100, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currentWeatherLabel.setFont(font)
        self.currentWeatherLabel.setText("")
        self.currentWeatherLabel.setObjectName("currentWeatherLabel")
        self.cityLabel = QtWidgets.QLabel(Form)
        self.cityLabel.setGeometry(QtCore.QRect(20, 20, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cityLabel.setFont(font)
        self.cityLabel.setObjectName("cityLabel")
        self.enteredCityLabel = QtWidgets.QLabel(Form)
        self.enteredCityLabel.setGeometry(QtCore.QRect(110, 25, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enteredCityLabel.setFont(font)
        self.enteredCityLabel.setText("")
        self.enteredCityLabel.setObjectName("enteredCityLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tempLabel.setText(_translate("Form", "Temp :"))
        self.weatherLabel.setText(_translate("Form", "Weather :"))
        self.cityLabel.setText(_translate("Form", "City :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = weatherUI()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
