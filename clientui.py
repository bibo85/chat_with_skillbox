# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Messenger(QtWidgets.QMainWindow):
    def setupUi(self, Messenger):
        Messenger.setObjectName("Messenger")
        Messenger.resize(411, 501)
        self.centralwidget = QtWidgets.QWidget(Messenger)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 0, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 110, 371, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 420, 311, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 430, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 60, 101, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 60, 101, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        Messenger.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Messenger)
        self.statusbar.setObjectName("statusbar")
        Messenger.setStatusBar(self.statusbar)

        self.retranslateUi(Messenger)
        QtCore.QMetaObject.connectSlotsByName(Messenger)

    def retranslateUi(self, Messenger):
        _translate = QtCore.QCoreApplication.translate
        Messenger.setWindowTitle(_translate("Messenger", "MainWindow"))
        self.label.setText(_translate("Messenger", "Skillbox Messenger"))
        self.pushButton.setText(_translate("Messenger", "Send"))
        self.label_2.setText(_translate("Messenger", "Username:"))
        self.label_3.setText(_translate("Messenger", "Password:"))


app = QtWidgets.QApplication([])
window = Ui_Messenger()
window.show()
app.exec()
