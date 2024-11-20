import csv
import sqlite3 as sql


class Db:
    def __init__(self):

        self.con = sql.connect(
            '/home/nikita/Python_Projects/Project/CarNumbers.db')

        self.cursor = self.con.cursor()

    def find_(self, input_, option):
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

            elif option == "Тел. номер":
                if input_ == el[3]:
                    res += f'{number}\n{name}\n{flat}\n'
                    for _ in range(max([len(number), len(flat), len(phone)])):
                        res += "o"

            elif option == "Квартира":
                if input_ == el[2]:
                    res += f'{number}\n{name}\n{phone}\n'
                    for _ in range(max([len(number), len(name), len(phone)])):
                        res += "o"

            elif option == "ФИО":

                if input_ == el[1].lower():

                    res += f'{number}\n{flat}\n{phone}\n'
                    for _ in range(max([len(number), len(flat), len(phone)])):
                        res += "o"

        return res

    def rm(self, number):

        self.cursor.execute(
            'DELETE from CarNumbers where number = ?', (number,))

        self.cursor.execute(
            'DELETE from CarNumbers where number = ?', (number,))

        self.con.commit()

    def close_(self):
        self.cursor.close()
        self.con.close()

    def add_(self, number, name, phone, flat):
        self.cursor.execute('INSERT INTO CarNumbers (number, name, flat, phone) VALUES (?, ?, ?, ?)',
                            (number, name, flat, phone))
        self.con.commit()

    def write_(self):
        self.cursor.execute("SELECT * FROM CarNumbers")

        with open('/home/nikita/Python_Projects/Project/db.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([i[0] for i in self.cursor.description])
            writer.writerows(self.cursor.fetchall())
