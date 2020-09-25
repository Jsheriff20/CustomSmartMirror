import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QPushButton, QGridLayout, QGroupBox

class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1080, 1920)
        self.setWindowTitle("Smart Mirror GUI")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("a label")
        self.label.move(50,50)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("click me")
        self.btn.clicked.connect(self.clickedBtn)

    def clickedBtn(self):
        self.label.setText("U pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = myWindow()
    win.show()
    sys.exit(app.exec_())

window()
