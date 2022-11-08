import sqlite3
import sys

from PyQt5.QtWidgets import QWidget, QApplication

from addtaskwindow.UI_AddTask import Ui_Form
from sqlite3_connection import con


class AddTaskApp(QWidget, Ui_Form):
    def __init__(self, xcoord, ycoord, main_app):
        super().__init__()
        self.main_app = main_app
        self.setupUi(self, xcoord, ycoord)
        self.addtaskAddButton.clicked.connect(self.addTask)

    def addTask(self):
        title = self.titleLineEdit.text()
        circ_count = self.CirclesCountLineEdit.text()
        cur = con.cursor()
        cur.execute("""INSERT INTO tasks VALUES(?, ?, ?)""", (title, circ_count, 'FALSE'))
        con.commit()
        self.main_app.initTable()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddTaskApp()
    ex.show()
    sys.exit(app.exec())
