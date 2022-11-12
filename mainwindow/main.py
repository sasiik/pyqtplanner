import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView
from sqlite3_connection import con

from UI_Main import Ui_MainWindow


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tasksTable.setColumnCount(4)
        self.tasksTable.setColumnWidth(0, 225)
        self.tasksTable.setColumnHidden(3, True)
        self.tasksTable.horizontalHeader().setStretchLastSection(True)
        self.tasksTable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tasksTable.setWordWrap(True)
        self.initTable()
        self.tasksTable.setHorizontalHeaderLabels(['Task Name', 'Est. Laps', 'Is Done'])
        self.changeStateButton.clicked.connect(self.changeState)
        self.mainAddTaskButton.clicked.connect(self.addTask)
        self.removeButton.clicked.connect(self.removeTask)
        self.setTimeSchedule.triggered.connect(self.popupTimeScheduleWindow)
        for elem in self.ChangePeriod.actions():
            elem.triggered.connect(self.ChangePeriodFunction)
        self.Pause_Unpause.triggered.connect(self.PauseUnpauseFunction)
        self.ClearData.triggered.connect(self.clearDataFunction)

    def closeEvent(self, event):
        for window in QApplication.topLevelWidgets():
            window.close()

    def initTable(self):
        cur = con.cursor()
        result = cur.execute(f"SELECT * FROM tasks").fetchall()
        self.tasksTable.setRowCount(len(result))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tasksTable.setItem(i, j, QTableWidgetItem(str(val)))

    def changeState(self):
        pass
    def addTask(self):
        from addtaskwindow.addtask import AddTaskApp
        self.AddTaskWidget = AddTaskApp(self.x() + 50, self.y() + 50, main_app=self)
        self.AddTaskWidget.show()

    def removeTask(self):
        rows = list(set([i.row() for i in self.tasksTable.selectedItems()]))
        ids = [self.tasksTable.item(i, 3).text() for i in rows]
        valid = QMessageBox.question(
            self, '', "Действительно удалить выбранные элементы?",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = con.cursor()
            cur.execute("DELETE FROM tasks WHERE id IN (" + ", ".join(
                '?' * len(ids)) + ")", ids)
            con.commit()
            self.initTable()

    def popupTimeScheduleWindow(self):
        from settingswindow.settings import SettingsApp
        self.TimeScheduleWidget = SettingsApp(self.x() + 20, self.y() + 20)
        self.TimeScheduleWidget.show()

    def ChangePeriodFunction(self):
        pass

    def PauseUnpauseFunction(self):
        pass

    def clearDataFunction(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec())
