# import sys
# from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QPushButton, QGridLayout, QGroupBox
# from PyQt5.QtCore import QDateTime, Qt
#
# # Subclass QMainWindow to customise your application's main window
# class MainWindow(QMainWindow):
#
#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#         self.setWindowTitle("Smart Mirror GUI")
#
#
#     now = QDateTime.currentDateTime()
#
#     print('Local datetime: ', now.toString(Qt.ISODate))
#     print('Universal datetime: ', now.toUTC().toString(Qt.ISODate))
#
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.showFullScreen()
# window.setStyleSheet("background-color: black;")
#
# app.exec_()


import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QPushButton, QGridLayout, QGroupBox



def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0,0,1080, 1920)
    win.setWindowTitle("Smart Mirror GUI")

    label = QtWidgets.QLabel(win)
    label.setText("a label")
    label.move(50,50)




    win.showFullScreen()
    sys.exit(app.exec_())

window()





