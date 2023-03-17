# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 612)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(".QWidget {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit {\n"
"    font = 12pt;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    font = 12pt;\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font = 12pt;\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    font = 12pt;\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font = 12pt;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"       font = 12pt;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    font = 12pt;\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    font = 12pt;\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"\n"
"QListView {\n"
"    font = 12pt;\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListWidget {\n"
"    font = 12pt;\n"
"    font = bold;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    font = 12pt;\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    font = 12pt;\n"
"    border-width: 2px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkkhaki;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    font = 12pt;\n"
"    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    font = 12pt;\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel ... */\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    font = 12pt;\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    font = 12pt;\n"
"    button-layout: 0;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 991, 561))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(".QWidget {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit {\n"
"    font = 12pt;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    font = 12pt;\n"
"    background-color: palegoldenrod;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font = 12pt;\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    font = 12pt;\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font = 12pt;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"       font = 12pt;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    font = 12pt;\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    font = 12pt;\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"\n"
"QListView {\n"
"    font = 12pt;\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListWidget {\n"
"    font = 12pt;\n"
"    font = bold;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    font = 12pt;\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    font = 12pt;\n"
"    border-width: 2px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkkhaki;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    font = 12pt;\n"
"    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    font = 12pt;\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    font = 12pt;\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    font = 12pt;\n"
"    button-layout: 0;\n"
"}\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_ogren = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tab_ogren.setFont(font)
        self.tab_ogren.setStyleSheet(".QWidget {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit {\n"
"    font = 12pt;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    font = 12pt;\n"
"    background-color: palegoldenrod;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font = 12pt;\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    font = 12pt;\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font = 12pt;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"       font = 12pt;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    font = 12pt;\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    font = 12pt;\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"\n"
"QListView {\n"
"    font = 12pt;\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListWidget {\n"
"    font = 12pt;\n"
"    font = bold;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    font = 12pt;\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    font = 12pt;\n"
"    border-width: 2px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkkhaki;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    font = 12pt;\n"
"    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    font = 12pt;\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel ... */\n"
"\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    font = 12pt;\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    font = 12pt;\n"
"    button-layout: 0;\n"
"}\n"
"\n"
"")
        self.tab_ogren.setObjectName("tab_ogren")
        self.label_11 = QtWidgets.QLabel(self.tab_ogren)
        self.label_11.setGeometry(QtCore.QRect(60, 50, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_ogren)
        self.label_12.setGeometry(QtCore.QRect(380, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_ogren)
        self.label_13.setGeometry(QtCore.QRect(740, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lbl_ing_sor = QtWidgets.QLabel(self.tab_ogren)
        self.lbl_ing_sor.setGeometry(QtCore.QRect(20, 240, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_ing_sor.setFont(font)
        self.lbl_ing_sor.setMouseTracking(False)
        self.lbl_ing_sor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_ing_sor.setAutoFillBackground(False)
        self.lbl_ing_sor.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.lbl_ing_sor.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_ing_sor.setMidLineWidth(0)
        self.lbl_ing_sor.setText("")
        self.lbl_ing_sor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ing_sor.setObjectName("lbl_ing_sor")
        self.lbl_tr_sor = QtWidgets.QLabel(self.tab_ogren)
        self.lbl_tr_sor.setGeometry(QtCore.QRect(340, 240, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_tr_sor.setFont(font)
        self.lbl_tr_sor.setMouseTracking(False)
        self.lbl_tr_sor.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.lbl_tr_sor.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_tr_sor.setMidLineWidth(0)
        self.lbl_tr_sor.setText("")
        self.lbl_tr_sor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_tr_sor.setObjectName("lbl_tr_sor")
        self.lbl_sf_sor = QtWidgets.QLabel(self.tab_ogren)
        self.lbl_sf_sor.setGeometry(QtCore.QRect(660, 240, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_sf_sor.setFont(font)
        self.lbl_sf_sor.setMouseTracking(False)
        self.lbl_sf_sor.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.lbl_sf_sor.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_sf_sor.setMidLineWidth(0)
        self.lbl_sf_sor.setText("")
        self.lbl_sf_sor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sf_sor.setObjectName("lbl_sf_sor")
        self.line_ing_cvb = QtWidgets.QLineEdit(self.tab_ogren)
        self.line_ing_cvb.setEnabled(False)
        self.line_ing_cvb.setGeometry(QtCore.QRect(60, 290, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_ing_cvb.setFont(font)
        self.line_ing_cvb.setText("")
        self.line_ing_cvb.setAlignment(QtCore.Qt.AlignCenter)
        self.line_ing_cvb.setObjectName("line_ing_cvb")
        self.line_tr_cvb = QtWidgets.QLineEdit(self.tab_ogren)
        self.line_tr_cvb.setEnabled(False)
        self.line_tr_cvb.setGeometry(QtCore.QRect(380, 290, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_tr_cvb.setFont(font)
        self.line_tr_cvb.setAlignment(QtCore.Qt.AlignCenter)
        self.line_tr_cvb.setObjectName("line_tr_cvb")
        self.line_sf_cvb = QtWidgets.QLineEdit(self.tab_ogren)
        self.line_sf_cvb.setEnabled(False)
        self.line_sf_cvb.setGeometry(QtCore.QRect(700, 290, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_sf_cvb.setFont(font)
        self.line_sf_cvb.setText("")
        self.line_sf_cvb.setAlignment(QtCore.Qt.AlignCenter)
        self.line_sf_cvb.setObjectName("line_sf_cvb")
        self.btn_ing_sor = QtWidgets.QPushButton(self.tab_ogren)
        self.btn_ing_sor.setEnabled(False)
        self.btn_ing_sor.setGeometry(QtCore.QRect(60, 180, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_ing_sor.setFont(font)
        self.btn_ing_sor.setObjectName("btn_ing_sor")
        self.btn_tr_sor = QtWidgets.QPushButton(self.tab_ogren)
        self.btn_tr_sor.setEnabled(False)
        self.btn_tr_sor.setGeometry(QtCore.QRect(380, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_tr_sor.setFont(font)
        self.btn_tr_sor.setObjectName("btn_tr_sor")
        self.btn_sf_sor = QtWidgets.QPushButton(self.tab_ogren)
        self.btn_sf_sor.setEnabled(False)
        self.btn_sf_sor.setGeometry(QtCore.QRect(700, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_sf_sor.setFont(font)
        self.btn_sf_sor.setObjectName("btn_sf_sor")
        self.btn_ing_kontrol = QtWidgets.QPushButton(self.tab_ogren)
        self.btn_ing_kontrol.setEnabled(False)
        self.btn_ing_kontrol.setGeometry(QtCore.QRect(60, 340, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_ing_kontrol.setFont(font)
        self.btn_ing_kontrol.setObjectName("btn_ing_kontrol")
        self.btn_tr_kontrol = QtWidgets.QPushButton(self.tab_ogren)
        self.btn_tr_kontrol.setEnabled(False)
        self.btn_tr_kontrol.setGeometry(QtCore.QRect(380, 340, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_tr_kontrol.setFont(font)
        self.btn_tr_kontrol.setObjectName("btn_tr_kontrol")
        self.btn_sf_kontrol = QtWidgets.QPushButton(self.tab_ogren)
        self.btn_sf_kontrol.setEnabled(False)
        self.btn_sf_kontrol.setGeometry(QtCore.QRect(700, 340, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_sf_kontrol.setFont(font)
        self.btn_sf_kontrol.setObjectName("btn_sf_kontrol")
        self.lbl_ing_sonuc = QtWidgets.QLabel(self.tab_ogren)
        self.lbl_ing_sonuc.setGeometry(QtCore.QRect(10, 380, 281, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_ing_sonuc.setFont(font)
        self.lbl_ing_sonuc.setMouseTracking(False)
        self.lbl_ing_sonuc.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_ing_sonuc.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_ing_sonuc.setLineWidth(1)
        self.lbl_ing_sonuc.setMidLineWidth(0)
        self.lbl_ing_sonuc.setText("")
        self.lbl_ing_sonuc.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ing_sonuc.setObjectName("lbl_ing_sonuc")
        self.lbl_tr_sonuc = QtWidgets.QLabel(self.tab_ogren)
        self.lbl_tr_sonuc.setGeometry(QtCore.QRect(330, 380, 291, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_tr_sonuc.setFont(font)
        self.lbl_tr_sonuc.setMouseTracking(False)
        self.lbl_tr_sonuc.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_tr_sonuc.setMidLineWidth(0)
        self.lbl_tr_sonuc.setText("")
        self.lbl_tr_sonuc.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_tr_sonuc.setObjectName("lbl_tr_sonuc")
        self.lbl_sf_sonuc = QtWidgets.QLabel(self.tab_ogren)
        self.lbl_sf_sonuc.setGeometry(QtCore.QRect(650, 380, 291, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_sf_sonuc.setFont(font)
        self.lbl_sf_sonuc.setMouseTracking(False)
        self.lbl_sf_sonuc.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_sf_sonuc.setMidLineWidth(0)
        self.lbl_sf_sonuc.setText("")
        self.lbl_sf_sonuc.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sf_sonuc.setObjectName("lbl_sf_sonuc")
        self.lbl_ing_sonuc_3 = QtWidgets.QLabel(self.tab_ogren)
        self.lbl_ing_sonuc_3.setGeometry(QtCore.QRect(10, 410, 281, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_ing_sonuc_3.setFont(font)
        self.lbl_ing_sonuc_3.setMouseTracking(False)
        self.lbl_ing_sonuc_3.setStyleSheet("")
        self.lbl_ing_sonuc_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_ing_sonuc_3.setMidLineWidth(0)
        self.lbl_ing_sonuc_3.setText("")
        self.lbl_ing_sonuc_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ing_sonuc_3.setObjectName("lbl_ing_sonuc_3")
        self.lbl_tr_sonuc_3 = QtWidgets.QLabel(self.tab_ogren)
        self.lbl_tr_sonuc_3.setGeometry(QtCore.QRect(270, 410, 411, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_tr_sonuc_3.setFont(font)
        self.lbl_tr_sonuc_3.setMouseTracking(False)
        self.lbl_tr_sonuc_3.setStyleSheet("")
        self.lbl_tr_sonuc_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_tr_sonuc_3.setMidLineWidth(0)
        self.lbl_tr_sonuc_3.setText("")
        self.lbl_tr_sonuc_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_tr_sonuc_3.setObjectName("lbl_tr_sonuc_3")
        self.lbl_sf_sonuc_3 = QtWidgets.QLabel(self.tab_ogren)
        self.lbl_sf_sonuc_3.setGeometry(QtCore.QRect(610, 410, 371, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_sf_sonuc_3.setFont(font)
        self.lbl_sf_sonuc_3.setMouseTracking(False)
        self.lbl_sf_sonuc_3.setStyleSheet("")
        self.lbl_sf_sonuc_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_sf_sonuc_3.setMidLineWidth(0)
        self.lbl_sf_sonuc_3.setText("")
        self.lbl_sf_sonuc_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sf_sonuc_3.setObjectName("lbl_sf_sonuc_3")
        self.btn_ing_basla = QtWidgets.QPushButton(self.tab_ogren)
        self.btn_ing_basla.setGeometry(QtCore.QRect(60, 100, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_ing_basla.setFont(font)
        self.btn_ing_basla.setObjectName("btn_ing_basla")
        self.btn_tr_basla = QtWidgets.QPushButton(self.tab_ogren)
        self.btn_tr_basla.setGeometry(QtCore.QRect(380, 100, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_tr_basla.setFont(font)
        self.btn_tr_basla.setObjectName("btn_tr_basla")
        self.btn_sf_basla = QtWidgets.QPushButton(self.tab_ogren)
        self.btn_sf_basla.setGeometry(QtCore.QRect(700, 100, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_sf_basla.setFont(font)
        self.btn_sf_basla.setObjectName("btn_sf_basla")
        self.tabWidget.addTab(self.tab_ogren, "")
        self.tab_kelime_list_2 = QtWidgets.QWidget()
        self.tab_kelime_list_2.setStyleSheet("QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"")
        self.tab_kelime_list_2.setObjectName("tab_kelime_list_2")
        self.listw_kelime = QtWidgets.QListWidget(self.tab_kelime_list_2)
        self.listw_kelime.setGeometry(QtCore.QRect(170, 50, 311, 421))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listw_kelime.setFont(font)
        self.listw_kelime.setObjectName("listw_kelime")
        item = QtWidgets.QListWidgetItem()
        self.listw_kelime.addItem(item)
        self.label_17 = QtWidgets.QLabel(self.tab_kelime_list_2)
        self.label_17.setGeometry(QtCore.QRect(170, 15, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.btn_ekle = QtWidgets.QPushButton(self.tab_kelime_list_2)
        self.btn_ekle.setGeometry(QtCore.QRect(750, 60, 81, 51))
        self.btn_ekle.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.btn_ekle.setObjectName("btn_ekle")
        self.label_21 = QtWidgets.QLabel(self.tab_kelime_list_2)
        self.label_21.setGeometry(QtCore.QRect(580, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.line_ing_ekle = QtWidgets.QLineEdit(self.tab_kelime_list_2)
        self.line_ing_ekle.setGeometry(QtCore.QRect(580, 50, 161, 31))
        self.line_ing_ekle.setObjectName("line_ing_ekle")
        self.line_tr_ekle = QtWidgets.QLineEdit(self.tab_kelime_list_2)
        self.line_tr_ekle.setGeometry(QtCore.QRect(580, 90, 161, 31))
        self.line_tr_ekle.setObjectName("line_tr_ekle")
        self.btn_sil = QtWidgets.QPushButton(self.tab_kelime_list_2)
        self.btn_sil.setGeometry(QtCore.QRect(750, 170, 81, 41))
        self.btn_sil.setObjectName("btn_sil")
        self.label_22 = QtWidgets.QLabel(self.tab_kelime_list_2)
        self.label_22.setGeometry(QtCore.QRect(580, 180, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.line_ing_duzelt = QtWidgets.QLineEdit(self.tab_kelime_list_2)
        self.line_ing_duzelt.setGeometry(QtCore.QRect(580, 290, 161, 31))
        self.line_ing_duzelt.setObjectName("line_ing_duzelt")
        self.line_tr_duzelt = QtWidgets.QLineEdit(self.tab_kelime_list_2)
        self.line_tr_duzelt.setGeometry(QtCore.QRect(580, 330, 161, 31))
        self.line_tr_duzelt.setObjectName("line_tr_duzelt")
        self.btn_duzelt_kaydet = QtWidgets.QPushButton(self.tab_kelime_list_2)
        self.btn_duzelt_kaydet.setGeometry(QtCore.QRect(750, 300, 81, 51))
        self.btn_duzelt_kaydet.setObjectName("btn_duzelt_kaydet")
        self.label_29 = QtWidgets.QLabel(self.tab_kelime_list_2)
        self.label_29.setGeometry(QtCore.QRect(580, 260, 191, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.btn_kelime_ogrenildi = QtWidgets.QPushButton(self.tab_kelime_list_2)
        self.btn_kelime_ogrenildi.setGeometry(QtCore.QRect(580, 420, 251, 51))
        self.btn_kelime_ogrenildi.setObjectName("btn_kelime_ogrenildi")
        self.label_20 = QtWidgets.QLabel(self.tab_kelime_list_2)
        self.label_20.setGeometry(QtCore.QRect(170, 480, 111, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.lbl_kelime_sayisi = QtWidgets.QLabel(self.tab_kelime_list_2)
        self.lbl_kelime_sayisi.setGeometry(QtCore.QRect(290, 480, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_kelime_sayisi.setFont(font)
        self.lbl_kelime_sayisi.setObjectName("lbl_kelime_sayisi")
        self.tabWidget.addTab(self.tab_kelime_list_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.tab.setObjectName("tab")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(170, 15, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.listw_ogrenilen = QtWidgets.QListWidget(self.tab)
        self.listw_ogrenilen.setGeometry(QtCore.QRect(170, 50, 311, 421))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listw_ogrenilen.setFont(font)
        self.listw_ogrenilen.setUniformItemSizes(False)
        self.listw_ogrenilen.setObjectName("listw_ogrenilen")
        self.btn_ogrenildi_sil = QtWidgets.QPushButton(self.tab)
        self.btn_ogrenildi_sil.setGeometry(QtCore.QRect(560, 130, 251, 51))
        self.btn_ogrenildi_sil.setObjectName("btn_ogrenildi_sil")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(170, 480, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(85, 0, 255);\n"
"color: rgb(0, 0, 222);")
        self.label_19.setObjectName("label_19")
        self.lbl_ogrenilen_sayisi = QtWidgets.QLabel(self.tab)
        self.lbl_ogrenilen_sayisi.setGeometry(QtCore.QRect(370, 480, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_ogrenilen_sayisi.setFont(font)
        self.lbl_ogrenilen_sayisi.setStyleSheet("\n"
"color: rgb(0, 0, 222);")
        self.lbl_ogrenilen_sayisi.setObjectName("lbl_ogrenilen_sayisi")
        self.btn_tekrar_ogren = QtWidgets.QPushButton(self.tab)
        self.btn_tekrar_ogren.setGeometry(QtCore.QRect(560, 50, 251, 51))
        self.btn_tekrar_ogren.setToolTipDuration(-1)
        self.btn_tekrar_ogren.setObjectName("btn_tekrar_ogren")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 23))
        self.menubar.setObjectName("menubar")
        self.menuHakkinda = QtWidgets.QMenu(self.menubar)
        self.menuHakkinda.setObjectName("menuHakkinda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHakkinda = QtWidgets.QAction(MainWindow)
        self.actionHakkinda.setObjectName("actionHakkinda")
        self.menuHakkinda.addAction(self.actionHakkinda)
        self.menubar.addAction(self.menuHakkinda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_11.setText(_translate("MainWindow", "İngilizce Kelime Sor"))
        self.label_12.setText(_translate("MainWindow", "Türkçe Kelime Sor"))
        self.label_13.setText(_translate("MainWindow", "Karışık Sor"))
        self.line_ing_cvb.setPlaceholderText(_translate("MainWindow", "Türkçesi ?"))
        self.line_tr_cvb.setPlaceholderText(_translate("MainWindow", "İngilizcesi ?"))
        self.line_sf_cvb.setPlaceholderText(_translate("MainWindow", "Cevabınız ?"))
        self.btn_ing_sor.setText(_translate("MainWindow", "SOR"))
        self.btn_tr_sor.setText(_translate("MainWindow", "SOR"))
        self.btn_sf_sor.setText(_translate("MainWindow", "SOR"))
        self.btn_ing_kontrol.setText(_translate("MainWindow", "KONTROL ET"))
        self.btn_tr_kontrol.setText(_translate("MainWindow", "KONTROL ET"))
        self.btn_sf_kontrol.setText(_translate("MainWindow", "KONTROL ET"))
        self.btn_ing_basla.setText(_translate("MainWindow", "BAŞLA"))
        self.btn_tr_basla.setText(_translate("MainWindow", "BAŞLA"))
        self.btn_sf_basla.setText(_translate("MainWindow", "BAŞLA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ogren), _translate("MainWindow", "Öğrenmeye Başla"))
        __sortingEnabled = self.listw_kelime.isSortingEnabled()
        self.listw_kelime.setSortingEnabled(False)
        item = self.listw_kelime.item(0)
        item.setText(_translate("MainWindow", "towed : çekilmek"))
        self.listw_kelime.setSortingEnabled(__sortingEnabled)
        self.label_17.setText(_translate("MainWindow", "Kelimeler"))
        self.btn_ekle.setText(_translate("MainWindow", "Ekle"))
        self.label_21.setText(_translate("MainWindow", "Ekle"))
        self.line_ing_ekle.setPlaceholderText(_translate("MainWindow", "İngilizcesi"))
        self.line_tr_ekle.setPlaceholderText(_translate("MainWindow", "Türkçesi"))
        self.btn_sil.setToolTip(_translate("MainWindow", "Shift + S"))
        self.btn_sil.setText(_translate("MainWindow", "Sil"))
        self.btn_sil.setShortcut(_translate("MainWindow", "Shift+S"))
        self.label_22.setText(_translate("MainWindow", "Kelimeyi Sil"))
        self.line_ing_duzelt.setPlaceholderText(_translate("MainWindow", "İngilizcesi"))
        self.line_tr_duzelt.setPlaceholderText(_translate("MainWindow", "Türkçesi"))
        self.btn_duzelt_kaydet.setText(_translate("MainWindow", "Düzelt"))
        self.label_29.setText(_translate("MainWindow", "Kelimeyi Düzenle"))
        self.btn_kelime_ogrenildi.setToolTip(_translate("MainWindow", "Shift + D"))
        self.btn_kelime_ogrenildi.setText(_translate("MainWindow", "Öğrenilenlere Ekle"))
        self.btn_kelime_ogrenildi.setShortcut(_translate("MainWindow", "Shift+D"))
        self.label_20.setText(_translate("MainWindow", "Kelime Sayısı:"))
        self.lbl_kelime_sayisi.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_kelime_list_2), _translate("MainWindow", "Kelime Listesi"))
        self.label_18.setText(_translate("MainWindow", "Öğrenilen Kelimeler"))
        self.btn_ogrenildi_sil.setToolTip(_translate("MainWindow", "Shift + X"))
        self.btn_ogrenildi_sil.setText(_translate("MainWindow", "Kelimeyi Sil"))
        self.btn_ogrenildi_sil.setShortcut(_translate("MainWindow", "Shift+X"))
        self.label_19.setText(_translate("MainWindow", "Öğrenilen Kelime Sayısı:"))
        self.lbl_ogrenilen_sayisi.setText(_translate("MainWindow", "..."))
        self.btn_tekrar_ogren.setToolTip(_translate("MainWindow", "Shift + C"))
        self.btn_tekrar_ogren.setText(_translate("MainWindow", "Kelimeyi Tekrar Öğren"))
        self.btn_tekrar_ogren.setShortcut(_translate("MainWindow", "Shift+C"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Öğrenilenler Listesi"))
        self.menuHakkinda.setTitle(_translate("MainWindow", "Hakkında"))
        self.actionHakkinda.setText(_translate("MainWindow", "Hakkında"))

