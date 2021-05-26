# This Python file uses the following encoding: utf-8
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
import random


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.remove.clicked.connect(self.Remove)
        self.setWindowTitle("Remove Redundant Paragraph")

    def Remove(self):
        new = ""
        f = self.ui.box1.toPlainText().split('\n')
        for item in f:
            new += item
            new += ' '
        self.ui.box2.setText(str(new))


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    # window.show()
    sys.exit(app.exec_())
