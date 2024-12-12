import os
import sys


from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication

from mainWindow import MainWindow


# добавление except_hook для более удобной отладки
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(
        os.path.dirname(__file__), 'CarNumbers.ico')))
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
