from PyQt6.QtWidgets import QMainWindow

from addWindow import AddWindow
from db import Db
from deleteWindow import DeleteWindow
from mainWindowUI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
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
        db = Db()  # запуск экзумпляра класса Db

        self.result.setText(
            # вывод результата поиска по базе данных в переменную result
            db.find_(self.input_.text().lower(), self.sender().text()))

        db.close_()  # завершение работы с БД

    def showHistory(self):
        try:
            with open("history.txt", 'r') as file:

                self.result.setText("".join(file.readlines()))

        except Exception:
            self.result.setText("История пуста!")

    def write_in_file(self):
        self.result.setText("")
        db = Db()  # запуск экзумпляра класса Db
        db.write_()  # Запись в БД
        self.result.textCursor().insertImage(
            "OK.png")

        db.close_()  # завершение работы с БД
