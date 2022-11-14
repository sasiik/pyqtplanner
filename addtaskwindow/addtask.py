import sys

from PyQt5.QtWidgets import QWidget, QApplication

from addtaskwindow.UI_AddTask import Ui_Form
from sqlite3_connection import con


class AddTaskApp(QWidget, Ui_Form):
    def __init__(self, xcoord, ycoord, main_app):
        super().__init__()
        # Setting main app source and position
        self.main_app = main_app
        self.setupUi(self, xcoord, ycoord)

        self.addtaskAddButton.clicked.connect(self.addTask)

    # Adding a task to DB
    def addTask(self):
        try:
            title = self.titleLineEdit.text()
            circ_count = int(self.CirclesCountLineEdit.text())
            if circ_count <= 0:
                raise Exception
            cur = con.cursor()
            cur.execute("""INSERT INTO tasks(title, circ_count, completed) VALUES(?, ?, ?)""",
                        (title, circ_count, 'FALSE'))
            con.commit()
            self.titleLineEdit.setText('')
            self.CirclesCountLineEdit.setText('')
            self.main_app.initTable()
            self.errorLabel.setText('')
        except Exception:
            self.errorLabel.setText('Error: incorrect input')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddTaskApp(0, 0, None)
    ex.show()
    sys.exit(app.exec())
