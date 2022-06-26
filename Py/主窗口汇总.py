import sys
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QApplication
from PyQt6.QtGui import QIcon, QAction


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exit_Action = QAction(QIcon('exit21.png'), "Exit", self)
        exit_Action.setShortcut("Ctrl+Q")
        exit_Action.setStatusTip("Exit application")
        exit_Action.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exit_Action)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_Action)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Main window")
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
