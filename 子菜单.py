import sys
from PyQt6.QtWidgets import QMainWindow, QMenu, QApplication
from PyQt6.QtGui import QAction


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")

        impMenu = QMenu("Import", self)
        impAct = QAction("Import mail", self)
        impMenu.addAction(impAct)

        newAct = QAction("New", self)

        fileMenu.addMenu(impMenu)
        fileMenu.addAction(newAct)

        self.setGeometry(30, 30, 350, 700)
        self.setWindowTitle("Submenu")
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
