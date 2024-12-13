from file import File
import sqlite3 as sql


class Db:

    def __init__(self):

        self.con = sql.connect(
            File('CarNumbers.db').resource_path())  # подключению к БД

        self.cursor = self.con.cursor()  # установка курсора

    def find_(self, input_, option):  # поиск по БД
        self.cursor.execute("SELECT * FROM CarNumbers")
        res = ""
        for el in self.cursor.fetchall():
            number = f'Номер: {el[0]}'
            name = f'Имя: {el[1]}'
            flat = f'Квартира: {el[2]}'
            phone = f'Тел. номер: {el[3]}'

            if option == "Номер":
                if input_ == el[0]:
                    res += f'{name}\n{flat}\n{phone}\n'
                    for _ in range(max([len(name), len(flat), len(phone)])):
                        res += "o"
                    res += "\n"

            elif option == "Тел. номер":
                if input_ == el[3]:
                    res += f'{number}\n{name}\n{flat}\n'
                    for _ in range(max([len(number), len(flat), len(phone)])):
                        res += "o"
                    res += "\n"

            elif option == "Квартира":
                if input_ == el[2]:
                    res += f'{number}\n{name}\n{phone}\n'
                    for _ in range(max([len(number), len(name), len(phone)])):
                        res += "o"
                    res += "\n"

            elif option == "ФИО":

                if input_ == el[1].lower():

                    res += f'{number}\n{flat}\n{phone}\n'
                    for _ in range(max([len(number), len(flat), len(phone)])):
                        res += "o"
                    res += "\n"

        return res

    def rm(self, number):  # удаление из БД

        self.cursor.execute(
            'DELETE from CarNumbers where number = ?', (number,))
        self.con.commit()

    def close_(self):  # функция закрытия
        self.cursor.close()
        self.con.close()

    def add_(self, number, name, phone, flat):  # добавление в БД
        self.cursor.execute('INSERT INTO CarNumbers (number, name, flat, phone) VALUES (?, ?, ?, ?)',
                            (number, name, flat, phone))
        self.con.commit()

    def write_(self):  # запись в бд
        self.cursor.execute("SELECT * FROM CarNumbers")

        db = File("db.csv")
        db.write_([i[0] for i in self.cursor.description],
                  self.cursor.fetchall())
