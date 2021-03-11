# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import clientui


class MessengerWindow(QtWidgets.QMainWindow, clientui.Ui_Messanger):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QtWidgets.QApplication([])
window = MessengerWindow()
window.show()
app.exec()
