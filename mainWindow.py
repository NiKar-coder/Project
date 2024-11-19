from PyQt6.QtWidgets import QMainWindow

from addWindow import AddWindow
from db import Db
from deleteWindow import DeleteWindow
from mainWindowUI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.aw = None
        self.dw = None
        self.setupUi(self)
        action_base = self.menubar.addMenu("Редактировать базу")
        action_base.addAction("Добавить", lambda: AddWindow().exec())
        action_base.addAction("Удалить", lambda: DeleteWindow().exec())
        action_base.addAction("Записать БД в файл", self.write_in_file)

        self.number.toggled.connect(self.find_)
        self.phone.toggled.connect(self.find_)
        self.name.toggled.connect(self.find_)
        self.flat.toggled.connect(self.find_)
        action_base.addAction("Посмотреть историю", self.showHistory)

    def find_(self):
        self.result.setText(None)
        db = Db()

        self.result.setText(db.find_(self.input_.text().lower(), self.sender().text()))

        self.result.setText(
            db.find_(self.input_.text().lower(), self.sender().text()))

        db.close_()

    def showHistory(self):
        try:
            with open("/home/nikita/Python_Projects/Project/history.txt", 'r') as file:

                self.result.setText("".join(file.readlines()))

                self.result.setText(
                    "".join(file.readlines()))

        except Exception:
            self.result.setText("История пуста!")

    def write_in_file(self):
        self.result.setText("")
        db = Db()
        db.write_()
        self.result.setText("Успешно!")
        db.close_()
