from datetime import datetime

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog
from file import File
from addWindowUI import Ui_AddWindow
from db import Db
from PyQt6.QtWidgets import QMessageBox


class AddWindow(QDialog, Ui_AddWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.WindowType.SubWindow)
        self.addBtn.clicked.connect(self.add)
        self.cancelBtn.clicked.connect(lambda: self.destroy())

    def add(self):
        db = Db()  # запуск экземпляра класса Db
        number = self.number.text()
        name = self.name.text()
        phone = self.phone.text()
        flat = self.flat.text()
        try:
            db.add_(number, name, phone, flat)  # добавление в БД
            db.close_()  # применение изменений
            self.destroy()
            history = File("history.txt")
            history.add_(
                f"{'{:%d-%m-%Y %H:%M}'.format(datetime.now())} Добавить {number}\n")
        except Exception:
            db.close_()
            QMessageBox.critical(
                self,
                "Error!",
                "Ошибка!",
                buttons=QMessageBox.StandardButton.Discard,
                defaultButton=QMessageBox.StandardButton.Discard,
            )
