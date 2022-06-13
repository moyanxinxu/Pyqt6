import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QAction


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.statusbar = None
        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Ready")

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        viewStatusAct = QAction('View statusbar', self, checkable=True)
        viewStatusAct.setStatusTip('View statusbar')
        viewStatusAct.setChecked(True)
        viewStatusAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatusAct)

        self.setGeometry(0, 0, 350, 250)
        self.setWindowTitle("Check menu")
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusbar.hide()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
