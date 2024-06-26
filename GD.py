# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GD.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 883)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QWidget(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(-20, -10, 1321, 361))
        self.header.setStyleSheet("#header{\n"
"    background-color: #f1f2f2;\n"
"}")
        self.header.setObjectName("header")
        self.search_results_list = QtWidgets.QListView(self.header)
        self.search_results_list.setGeometry(QtCore.QRect(230, 171, 761, 180))
        self.search_results_list.setObjectName("search_results_list")
        self.search_results_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.search_results_list.hide()
        self.THEME = QtWidgets.QLabel(self.header)
        self.THEME.setGeometry(QtCore.QRect(10, 10, 1251, 101))
        self.THEME.setText("")
        self.THEME.setPixmap(QtGui.QPixmap("theme.png"))
        self.THEME.setScaledContents(True)
        self.THEME.setObjectName("THEME")
        self.TITLE = QtWidgets.QWidget(self.header)
        self.TITLE.setGeometry(QtCore.QRect(60, 130, 171, 41))
        self.TITLE.setStyleSheet("#TITLE{\n"
"    background-color: #f97d36;\n"
"}")
        self.TITLE.setObjectName("TITLE")
        self.TITLE_2 = QtWidgets.QLabel(self.TITLE)
        self.TITLE_2.setGeometry(QtCore.QRect(40, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.TITLE_2.setFont(font)
        self.TITLE_2.setObjectName("TITLE_2")
        self.search_input = QtWidgets.QLineEdit(self.header)
        self.search_input.setGeometry(QtCore.QRect(230, 130, 761, 41))
        self.search_input.setObjectName("search_input")
        searchfont = QtGui.QFont()
        searchfont.setPointSize(11)
        self.search_input.setFont(searchfont)
        self.bt_search = QtWidgets.QPushButton(self.header)
        self.bt_search.setGeometry(QtCore.QRect(990, 130, 101, 41))
        self.bt_search.setStyleSheet("#bt_search{\n"
"    background-color: #f97d36;\n"
"}")
        self.bt_search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_search.setIcon(icon)
        self.bt_search.setObjectName("bt_search")
        self.TILTE = QtWidgets.QLabel(self.header)
        self.TILTE.setGeometry(QtCore.QRect(20, 190, 1121, 131))
        self.TILTE.setText("")
        self.TILTE.setPixmap(QtGui.QPixmap("service.png"))
        self.TILTE.setScaledContents(True)
        self.TILTE.setObjectName("TILTE")
        self.TITLE_4 = QtWidgets.QLabel(self.header)
        self.TITLE_4.setGeometry(QtCore.QRect(60, 250, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.TITLE_4.setFont(font)
        self.TITLE_4.setObjectName("TITLE_4")
        self.TILTE_2 = QtWidgets.QLabel(self.header)
        self.TILTE_2.setGeometry(QtCore.QRect(60, 330, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.TILTE_2.setFont(font)
        self.TILTE_2.setObjectName("TILTE_2")
        self.TITLE_3 = QtWidgets.QLabel(self.header)
        self.TITLE_3.setGeometry(QtCore.QRect(110, 330, 151, 16))
        self.TITLE_3.setObjectName("TITLE_3")
        self.body = QtWidgets.QWidget(self.centralwidget)
        self.body.setGeometry(QtCore.QRect(0, 350, 1131, 601))
        self.body.setStyleSheet("#body{\n"
"    background-color: #fafafa;\n"
"}")
        self.body.setObjectName("body")
        self.input_userdata = QtWidgets.QTableWidget(self.body)
        self.input_userdata.setGeometry(QtCore.QRect(40, 40, 1031, 192))
        self.input_userdata.setObjectName("input_userdata")
        self.TITLE_5 = QtWidgets.QLabel(self.body)
        self.TITLE_5.setGeometry(QtCore.QRect(40, 10, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.TITLE_5.setFont(font)
        self.TITLE_5.setObjectName("TITLE_5")
        self.bt_submit = QtWidgets.QPushButton(self.body)
        self.bt_submit.setGeometry(QtCore.QRect(890, 250, 181, 41))
        self.bt_submit.setStyleSheet("#bt_submit{\n"
"    background-color: #f97d36; color: #ffffff;\n"
"}")
        self.bt_submit.setText("SUBMIT")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_submit.setFont(font)
        self.bt_submit.setObjectName("bt_submit")
        
        self.output_bookrcm = QtWidgets.QTableWidget(self.body)
        self.output_bookrcm.setGeometry(QtCore.QRect(40, 310, 1031, 192))
        self.output_bookrcm.setObjectName("output_bookrcm")
        self.output_bookrcm.setColumnCount(0)
        self.output_bookrcm.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TITLE_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">ON SEARCH</span></p></body></html>"))
        self.TITLE_4.setText(_translate("MainWindow", "BOOK RECOMMENTDATION"))
        self.TILTE_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5a98b2;\">Home</span></p></body></html>"))
        self.TITLE_3.setText(_translate("MainWindow", "/ Book Recommentdation"))
        self.TITLE_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f97d36;\">BOOK REVIEW SCORES</span></p></body></html>"))
        
    

        
        

