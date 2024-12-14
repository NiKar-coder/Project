import sys

from file import File
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication

from mainWindow import MainWindow

sys.argv += ['-platform', 'windows:darkmode=2']
# добавление except_hook для более удобной отладки


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


history = File("history.txt")
history.create()
db = File("db.csv")
db.create()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setWindowIcon(QtGui.QIcon(File('CarNumbers.ico').resource_path()))
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
