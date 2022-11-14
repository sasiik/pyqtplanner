import os
import sys

from PyQt5.QtCore import QTimer, QUrl
from PyQt5 import QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView, QAbstractItemView
from sqlite3_connection import con

from UI_Main import Ui_MainWindow
import datetime as dt
import csv


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # some tasksTable changes
        self.tasksTable.setColumnCount(4)
        self.tasksTable.setColumnWidth(0, 225)
        self.tasksTable.setColumnHidden(3, True)
        self.tasksTable.horizontalHeader().setStretchLastSection(True)
        self.tasksTable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tasksTable.setWordWrap(True)
        self.tasksTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.initTable()
        self.tasksTable.setHorizontalHeaderLabels(['Task Name', 'Est. Laps', 'Is Done'])

        # Loading sound
        self.load_mp3(os.getcwd() + '/alarm.wav')

        # Connecting buttons
        self.changeStateButton.clicked.connect(self.changeState)
        self.mainAddTaskButton.clicked.connect(self.addTask)
        self.removeButton.clicked.connect(self.removeTask)
        self.setTimeSchedule.triggered.connect(self.popupTimeScheduleWindow)
        for elem in self.ChangePeriod.actions():
            elem.triggered.connect(self.ChangePeriodFunction)
        self.Pause_Unpause.triggered.connect(self.PauseUnpauseFunction)
        self.ClearData.triggered.connect(self.clearDataFunction)

        # Connecting timer
        self.qttimer = QTimer()
        self.qttimer.timeout.connect(self.showTime)
        self.qttimer.start(1000)

        # Initializing time periods data (time in sec, name of period, color properties for period)
        self.focus_time = {'in_sec': 1500, 'label': 'Focus Time', 'properties': 'QLabel { color : red; }'}
        self.break_time = {'in_sec': 300, 'label': 'Break Time', 'properties': 'QLabel { color : green; }'}
        self.long_break_time = {'in_sec': 900, 'label': 'Long Break Time', 'properties': 'QLabel { color : blue; }'}

        # Reading config.csv file and modifying periods values accordingly
        self.personalDataReader()
        # Constructing Pomodoro cycle
        self.periods = [self.focus_time, self.break_time] * 3 + [self.focus_time, self.long_break_time]

        self.counter = 0  # Counter of periods. Useful when calling a certain period
        self.current_period = self.periods[0].copy()  # Setting current period (Focus time)
        self.timer.setText(str((dt.datetime.min + dt.timedelta(seconds=self.current_period['in_sec'])).time()))
        # Setting time on the MainWindow timer

    # Closes all windows if main is closed
    def closeEvent(self, event):
        for window in QApplication.topLevelWidgets():
            window.close()

    # Config.csv file reader
    def personalDataReader(self):
        with open('config.csv', encoding="utf8") as csvfile:
            reader = list(csv.reader(csvfile, delimiter=';'))
            self.focus_time['in_sec'] = int(reader[0][0])
            self.break_time['in_sec'] = int(reader[0][1])
            self.long_break_time['in_sec'] = int(reader[0][2])

    # Loads the alarm sound
    def load_mp3(self, filename):
        media = QUrl.fromLocalFile(filename)
        self.content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer(flags=QtMultimedia.QMediaPlayer.LowLatency)

    # Timer function
    def showTime(self):
        if self.current_period['in_sec'] == 0:
            self.counter += 1
            self.PeriodSwap()
            self.player.setMedia(self.content)
            self.player.play()
        else:
            self.current_period['in_sec'] -= 1
            value = dt.timedelta(seconds=self.current_period['in_sec'])
            self.timer.setText(str((dt.datetime.min + value).time()))

    def initTable(self):
        cur = con.cursor()
        result = cur.execute(f"SELECT * FROM tasks").fetchall()
        self.tasksTable.setRowCount(len(result))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tasksTable.setItem(i, j, QTableWidgetItem(str(val)))

    # Changes FALSE value to TRUE and vice versa
    def changeState(self):
        cur = con.cursor()
        rows = list(set([i.row() for i in self.tasksTable.selectedItems()]))
        ids = [self.tasksTable.item(i, 3).text() for i in rows]
        cur.execute("""UPDATE tasks
        SET completed = CASE completed WHEN 'FALSE' THEN 'TRUE' ELSE 'FALSE' END
        WHERE id IN (""" + """, """.join(
            '?' * len(ids)) + """)""", ids)
        self.initTable()

    def addTask(self):
        from addtaskwindow.addtask import AddTaskApp
        self.AddTaskWidget = AddTaskApp(self.x() + 50, self.y() + 50, main_app=self)
        self.AddTaskWidget.show()

    def removeTask(self):
        rows = list(set([i.row() for i in self.tasksTable.selectedItems()]))
        if rows:
            ids = [self.tasksTable.item(i, 3).text() for i in rows]
            valid = QMessageBox.question(
                self, 'Yandex.Planner', "Delete these elements?",
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                cur = con.cursor()
                cur.execute("DELETE FROM tasks WHERE id IN (" + ", ".join(
                    '?' * len(ids)) + ")", ids)
                con.commit()
                self.initTable()

    # Calls SettingsApp
    def popupTimeScheduleWindow(self):
        from settingswindow.settings import SettingsApp
        self.TimeScheduleWidget = SettingsApp(self.x() + 20, self.y() + 20, main_app=self)
        self.TimeScheduleWidget.show()

    # Time periods swapping main logic is here
    def PeriodSwap(self):
        self.current_period = self.periods[self.counter % len(self.periods)].copy()
        self.timer.setText(str((dt.datetime.min + dt.timedelta(seconds=self.current_period['in_sec'])).time()))
        # Setting period info and color when period changes
        self.periodInfo.setText(self.current_period['label'])
        self.timer.setStyleSheet(self.current_period['properties'])
        self.periodInfo.setStyleSheet(self.current_period['properties'])

    # Changing periods function
    def ChangePeriodFunction(self):
        if self.sender().objectName() == "ChangeToLongBreak":
            self.counter = 7
        elif self.sender().objectName() == 'ChangeToShortBreak':
            self.counter = 1
        else:
            self.counter = 0
        # Changing counter value helps to swap between periods
        self.PeriodSwap()
        self.pause()

    # modified version of self.qttimer.pause()
    def pause(self):
        self.qttimer.stop()
        self.periodInfo.setText(self.current_period['label'] + ' (Paused)')

    def PauseUnpauseFunction(self):
        if self.qttimer.isActive():
            self.pause()
        else:
            self.qttimer.start(1000)
            self.periodInfo.setText(self.current_period['label'])

    def clearDataFunction(self):
        valid = QMessageBox.question(
            self, 'Yandex.Planner', "Delete all?",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = con.cursor()
            cur.execute("DELETE FROM tasks")
            con.commit()
            self.initTable()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec())
