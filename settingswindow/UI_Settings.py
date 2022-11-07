# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form, xcoord, ycoord):
        Form.setObjectName("Form")
        Form.setFixedSize(551, 413)
        Form.move(xcoord, ycoord)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(35, 90, 481, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FocusTimeDurationLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.FocusTimeDurationLabel.setObjectName("FocusTimeDurationLabel")
        self.horizontalLayout.addWidget(self.FocusTimeDurationLabel)
        self.FocusTimeDurationLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.FocusTimeDurationLineEdit.setObjectName("FocusTimeDurationLineEdit")
        self.horizontalLayout.addWidget(self.FocusTimeDurationLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BreakDurationLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.BreakDurationLabel.setObjectName("BreakDurationLabel")
        self.horizontalLayout_2.addWidget(self.BreakDurationLabel)
        self.BreakDurationLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.BreakDurationLineEdit.setObjectName("BreakDurationLineEdit")
        self.horizontalLayout_2.addWidget(self.BreakDurationLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LongBreakDurationLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.LongBreakDurationLabel.setObjectName("LongBreakDurationLabel")
        self.horizontalLayout_3.addWidget(self.LongBreakDurationLabel)
        self.LongBreakDurationLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.LongBreakDurationLineEdit.setObjectName("LongBreakDurationLineEdit")
        self.horizontalLayout_3.addWidget(self.LongBreakDurationLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.settingsSaveButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.settingsSaveButton.setObjectName("settingsSaveButton")
        self.verticalLayout.addWidget(self.settingsSaveButton)
        self.settingsAppLabel = QtWidgets.QLabel(Form)
        self.settingsAppLabel.setGeometry(QtCore.QRect(120, 10, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.settingsAppLabel.setFont(font)
        self.settingsAppLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.settingsAppLabel.setObjectName("settingsAppLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Settings"))
        self.FocusTimeDurationLabel.setText(_translate("Form", "Focus time duration(min):"))
        self.BreakDurationLabel.setText(_translate("Form", "Break duration(min):"))
        self.LongBreakDurationLabel.setText(_translate("Form", "Long break duration(min):"))
        self.settingsSaveButton.setText(_translate("Form", "Save"))
        self.settingsAppLabel.setText(_translate("Form", "Settings"))