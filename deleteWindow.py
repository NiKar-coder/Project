from datetime import datetime
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QMessageBox

from db import Db
from deleteWindowUI import Ui_DeleteWindow


class DeleteWindow(QDialog, Ui_DeleteWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.WindowType.SubWindow)
        self.cancelBtn.clicked.connect(lambda: self.destroy())
        self.delBtn.clicked.connect(self.delete)

    def delete(self):
        db = Db()
        try:

            number = self.number.text()
            db.rm(number)
            with open('/home/nikita/Python_Projects/Project/history.txt', 'a') as file:

                file.write(
                    f"{"{:%d-%m-%Y %H:%M}".format(datetime.now())} Удалить {number}\n")

            db.close_()
            self.destroy()

        except Exception:
            db.close_()
            QMessageBox.critical(
                self,
                "Error!",
                "Ошибка!",
                buttons=QMessageBox.StandardButton.Discard,
                defaultButton=QMessageBox.StandardButton.Discard,
            )

            self.destroy()
