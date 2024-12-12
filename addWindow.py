from datetime import datetime

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog

from addWindowUI import Ui_AddWindow
from db import Db


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

        with open('history.txt', 'a') as file:
            file.write(f"Добавить {number}\n")

        with open('/home/nikita/Python_Projects/Project/history.txt', 'a') as file:
            file.write(
                f"{datetime.now()} Добавить {number}\n")

        db.add_(number, name, phone, flat)  # добавление в БД
        db.close_()  # применение изменений
        self.destroy()
