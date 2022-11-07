import sqlite3
import sys

from PyQt5.QtWidgets import QWidget, QApplication

from addtaskwindow.UI_AddTask import Ui_Form
from sqlite3_connection import con


class AddTaskApp(QWidget, Ui_Form):
    def __init__(self, xcoord, ycoord):
        super().__init__()
        self.setupUi(self, xcoord, ycoord)
        self.addtaskAddButton.clicked.connect(self.addTask)

    def addTask(self):
        from mainwindow.main import MainApp, ex

        title = self.titleLineEdit.text()
        circ_count = self.CirclesCountLineEdit.text()
        cur = con.cursor()
        cur.execute("""INSERT INTO tasks VALUES(?, ?, ?)""", (title, circ_count, 'FALSE'))
        con.commit()
        MainApp.initTable(ex)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddTaskApp()
    ex.show()
    sys.exit(app.exec())