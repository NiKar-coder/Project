from datetime import datetime
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QMessageBox
from file import File
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
        db = Db()  # запуск экзумпляра класса Db
        try:

            number = self.number.text()
            db.rm(number)  # удаление из БД
            db.close_()
            history = File("history.txt")
            history.add_(
                f"{'{:%d-%m-%Y %H:%M}'.format(datetime.now())} Удалить {number}\n")

            # применение изменений и закрытие БД
            self.destroy()

        except Exception:
            db.close_()  # применение изменений и закрытие БД
            QMessageBox.critical(
                self,
                "Error!",
                "Ошибка!",
                buttons=QMessageBox.StandardButton.Discard,
                defaultButton=QMessageBox.StandardButton.Discard,
            )

            self.destroy()
