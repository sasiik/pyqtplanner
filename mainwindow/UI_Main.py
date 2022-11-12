# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(634, 782)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 20, 451, 691))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timer = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(70)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.timer.setFont(font)
        self.timer.setAlignment(QtCore.Qt.AlignCenter)
        self.timer.setObjectName("timer")
        self.verticalLayout.addWidget(self.timer)
        self.periodInfo = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.periodInfo.setFont(font)
        self.periodInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.periodInfo.setObjectName("periodInfo")
        self.verticalLayout.addWidget(self.periodInfo)
        self.changeStateButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.changeStateButton.setObjectName("changeStateButton")
        self.verticalLayout.addWidget(self.changeStateButton)
        self.tasksTable = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tasksTable.setObjectName("tasksTable")
        self.tasksTable.setColumnCount(0)
        self.tasksTable.setRowCount(0)
        self.verticalLayout.addWidget(self.tasksTable)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainAddTaskButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.mainAddTaskButton.setObjectName("mainAddTaskButton")
        self.horizontalLayout.addWidget(self.mainAddTaskButton)
        self.removeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout.addWidget(self.removeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 22))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.ChangePeriod = QtWidgets.QMenu(self.menubar)
        self.ChangePeriod.setObjectName("ChangePeriod")
        self.Pause_Unpause = QtWidgets.QAction(MainWindow)
        self.Pause_Unpause.setObjectName("menuPause_Unpause")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.setTimeSchedule = QtWidgets.QAction(MainWindow)
        self.setTimeSchedule.setObjectName("setTimeSchedule")
        self.ChangeToFocusTime = QtWidgets.QAction(MainWindow)
        self.ChangeToFocusTime.setObjectName("ChangeToFocusTime")
        self.ChangeToShortBreak = QtWidgets.QAction(MainWindow)
        self.ChangeToShortBreak.setObjectName("ChangeToShortBreak")
        self.ChangeToLongBreak = QtWidgets.QAction(MainWindow)
        self.ChangeToLongBreak.setObjectName("ChangeToLongBreak")
        self.ClearData = QtWidgets.QAction(MainWindow)
        self.ClearData.setObjectName("ClearData")
        self.menuSettings.addAction(self.setTimeSchedule)
        self.menuSettings.addAction(self.ClearData)
        self.ChangePeriod.addAction(self.ChangeToFocusTime)
        self.ChangePeriod.addAction(self.ChangeToShortBreak)
        self.ChangePeriod.addAction(self.ChangeToLongBreak)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.ChangePeriod.menuAction())
        self.menubar.insertAction(self.Pause_Unpause, self.Pause_Unpause)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yandex.Planner"))
        self.timer.setStyleSheet("QLabel { color : red; }")
        self.periodInfo.setText(_translate("MainWindow", "Focus Time"))
        self.periodInfo.setStyleSheet("QLabel { color : red; }")
        self.changeStateButton.setText(_translate("MainWindow", "Mark selected tasks as completed/uncompleted"))
        self.mainAddTaskButton.setText(_translate("MainWindow", "Add task"))
        self.removeButton.setText(_translate("MainWindow", "Remove tasks"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.ChangePeriod.setTitle(_translate("MainWindow", "Change period"))
        self.Pause_Unpause.setText(_translate("MainWindow", "Pause/Continue"))
        self.setTimeSchedule.setText(_translate("MainWindow", "Time Schedule"))
        self.ChangeToFocusTime.setText(_translate("MainWindow", "Focus Time"))
        self.ChangeToShortBreak.setText(_translate("MainWindow", "Short Break"))
        self.ChangeToLongBreak.setText(_translate("MainWindow", "Long Break"))
        self.ClearData.setText(_translate("MainWindow", "Clear data"))
