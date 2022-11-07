from UI_Main import Ui_MainWindow

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from sqlite3_connection import con


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tasksTable.setColumnWidth(0, 235)
        self.tasksTable.horizontalHeader().setStretchLastSection(True)
        self.tasksTable.setWordWrap(True)
        self.initTable()
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
        self.tasksTable.setColumnCount(len(result[0]))
        self.tasksTable.setHorizontalHeaderLabels(['Task Name', 'Est. Laps', 'Is Done'])
        print(result)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tasksTable.setItem(i, j, QTableWidgetItem(str(val)))

    def changeState(self):
        pass

    def addTask(self):
        from addtaskwindow.addtask import AddTaskApp
        self.AddTaskWidget = AddTaskApp(self.x() + 50, self.y() + 50)
        self.AddTaskWidget.show()

    def removeTask(self):
        pass

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

app = QApplication(sys.argv)
ex = MainApp()

if __name__ == '__main__':
    ex.show()
    sys.exit(app.exec())
