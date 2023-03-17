# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kelime_yok_uyarı.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KelimeYok(object):
    def setupUi(self, KelimeYok):
        KelimeYok.setObjectName("KelimeYok")
        KelimeYok.resize(422, 149)
        self.label = QtWidgets.QLabel(KelimeYok)
        self.label.setGeometry(QtCore.QRect(10, 50, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: Default;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(KelimeYok)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(120, 0, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(KelimeYok)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: Default;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(KelimeYok)
        QtCore.QMetaObject.connectSlotsByName(KelimeYok)

    def retranslateUi(self, KelimeYok):
        _translate = QtCore.QCoreApplication.translate
        KelimeYok.setWindowTitle(_translate("KelimeYok", "Bilgi Ekranı"))
        self.label.setText(_translate("KelimeYok", "Kayıtlı kelime yok. Lütfen kelime ekleyin.."))
        self.label_2.setText(_translate("KelimeYok", "UYARI !!"))
        self.label_3.setText(_translate("KelimeYok", "Puanınız"))

