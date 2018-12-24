# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Flips.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt.FlipCoin.MatplotlibWidget import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 342)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 20, 221, 205))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.flipcoin = QtWidgets.QPushButton(self.formLayoutWidget)
        self.flipcoin.setObjectName("flipcoin")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.flipcoin)
        self.flip_fcoins = QtWidgets.QPushButton(self.formLayoutWidget)
        self.flip_fcoins.setObjectName("flip_fcoins")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.flip_fcoins)
        self.exit_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.exit_button.setObjectName("exit_button")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.exit_button)
        self.coin_number = QtWidgets.QLabel(self.formLayoutWidget)
        self.coin_number.setObjectName("coin_number")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.coin_number)
        self.coin_number_up = QtWidgets.QLabel(self.formLayoutWidget)
        self.coin_number_up.setObjectName("coin_number_up")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.coin_number_up)
        self.coin_number_down = QtWidgets.QLabel(self.formLayoutWidget)
        self.coin_number_down.setObjectName("coin_number_down")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.coin_number_down)
        self.p_up = QtWidgets.QLabel(self.formLayoutWidget)
        self.p_up.setObjectName("p_up")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.p_up)
        self.coin_number_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.coin_number_le.setObjectName("coin_number_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.coin_number_le)
        self.coin_number_up_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.coin_number_up_le.setObjectName("coin_number_up_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.coin_number_up_le)
        self.coin_number_down_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.coin_number_down_le.setObjectName("coin_number_down_le")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.coin_number_down_le)
        self.p_up_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.p_up_le.setObjectName("p_up_le")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.p_up_le)
        self.p_down = QtWidgets.QLabel(self.formLayoutWidget)
        self.p_down.setObjectName("p_down")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.p_down)
        self.p_down_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.p_down_le.setObjectName("p_down_le")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.p_down_le)
        self.flip_tcoins = QtWidgets.QPushButton(self.formLayoutWidget)
        self.flip_tcoins.setObjectName("flip_tcoins")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.flip_tcoins)
        self.matplotwidget = MatplotlibWidget(self.centralwidget)
        self.matplotwidget.setGeometry(QtCore.QRect(300, 10, 351, 231))
        self.matplotwidget.setObjectName("matplotwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.flipcoin.setText(_translate("MainWindow", "flip"))
        self.flip_fcoins.setText(_translate("MainWindow", "50 coins"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.coin_number.setText(_translate("MainWindow", "硬币总数"))
        self.coin_number_up.setText(_translate("MainWindow", "硬币向上数量"))
        self.coin_number_down.setText(_translate("MainWindow", "硬币向下数量"))
        self.p_up.setText(_translate("MainWindow", "硬币向上概率"))
        self.p_down.setText(_translate("MainWindow", "硬币向下概率"))
        self.flip_tcoins.setText(_translate("MainWindow", "10 coins"))

from MatplotlibWidget import MatplotlibWidget
