import sys
import os
import csv


class File:

    def __init__(self, name):
        self.name = name

    def resource_path(self):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, self.name)
        else:
            return os.path.join(os.path.abspath("."), self.name)

    def add_(self, text):
        with open(self.resource_path(), 'a', encoding='utf-8') as file:
            file.write(text)

    def read_(self):

        with open(self.resource_path(), 'r', encoding='utf-8') as file:
            return "".join(file.readlines())

    def write_(self, arr, cursor):
        with open(self.resource_path(), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(arr)
            writer.writerows(cursor)

    def create(self):
        with open(self.resource_path(), 'a'):
            pass
