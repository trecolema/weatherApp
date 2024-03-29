# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weatherGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import requests
from weatherDisplay import weatherUI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):

    def openWeatherDisplay(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = weatherUI()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(614, 411)
        self.weatherAppLabel = QtWidgets.QLabel(Form)
        self.weatherAppLabel.setGeometry(QtCore.QRect(200, 40, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.weatherAppLabel.setFont(font)
        self.weatherAppLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherAppLabel.setObjectName("weatherAppLabel")
        self.submitBtn = QtWidgets.QPushButton(Form, clicked = lambda : self.getWeather())
        self.submitBtn.setGeometry(QtCore.QRect(410, 320, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submitBtn.setFont(font)
        self.submitBtn.setObjectName("submitBtn")
        self.EnterCityLabel = QtWidgets.QLabel(Form)
        self.EnterCityLabel.setGeometry(QtCore.QRect(100, 210, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EnterCityLabel.setFont(font)
        self.EnterCityLabel.setObjectName("EnterCityLabel")
        self.cityEntry = QtWidgets.QLineEdit(Form)
        self.cityEntry.setGeometry(QtCore.QRect(220, 210, 291, 41))
        self.cityEntry.setObjectName("cityEntry")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def getWeather(self):
        api_key = '30d4741c779ba94c470ca1f63045390a'

        user_input = self.cityEntry.text()

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

        if weather_data.json()['cod'] == '404':
            print("No City Found")
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])

        msg = QMessageBox()
        msg.setWindowTitle("weather")
        msg.setText(f"temp : {temp} \nweather: {weather} ")
        x = msg.exec_()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.weatherAppLabel.setText(_translate("Form", "Weather App"))
        self.submitBtn.setText(_translate("Form", "submit"))
        self.EnterCityLabel.setText(_translate("Form", "Enter City:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
