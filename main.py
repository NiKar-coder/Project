import os
import sys

import qdarktheme
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication

from mainWindow import MainWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("dark", corner_shape="sharp",
                           custom_colors={"primary": "#FFFFFF"})  # установка тёмной темы
    app.setWindowIcon(QtGui.QIcon(os.path.join(
        os.path.dirname(__file__), 'CarNumbers.ico')))
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
