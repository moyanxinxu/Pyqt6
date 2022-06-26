from PyQt6.QtWidgets import (QWidget, QCalendarWidget, QLabel, QApplication, QVBoxLayout)
from PyQt6.QtCore import QDate
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showData)

        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        data = cal.selectedDate()
        self.lbl.setText(data.toString())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showData(self, data):
        self.lbl.setText(data.toString())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

