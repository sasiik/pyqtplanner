# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addtask.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form, xcoord, ycoord):
        Form.setObjectName("Form")
        Form.setFixedSize(392, 320)
        Form.move(xcoord, ycoord)
        self.addtaskAppLabel = QtWidgets.QLabel(Form)
        self.addtaskAppLabel.setGeometry(QtCore.QRect(40, 10, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.addtaskAppLabel.setFont(font)
        self.addtaskAppLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.addtaskAppLabel.setObjectName("addtaskAppLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 79, 351, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(62)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout.addWidget(self.titleLabel)
        self.titleLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.horizontalLayout.addWidget(self.titleLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.CirclesCountLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.CirclesCountLabel.setObjectName("CirclesCountLabel")
        self.horizontalLayout_3.addWidget(self.CirclesCountLabel)
        self.CirclesCountLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.CirclesCountLineEdit.setObjectName("CirclesCountLineEdit")
        self.horizontalLayout_3.addWidget(self.CirclesCountLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.addtaskAddButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addtaskAddButton.setObjectName("addtaskAddButton")
        self.verticalLayout.addWidget(self.addtaskAddButton)
        self.errorLabel = QtWidgets.QLabel(Form)
        self.errorLabel.setGeometry(QtCore.QRect(20, 280, 351, 21))
        font = QtGui.QFont()
        font.setItalic(True)
        self.errorLabel.setFont(font)
        self.errorLabel.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add a task"))
        self.addtaskAppLabel.setText(_translate("Form", "Add task"))
        self.titleLabel.setText(_translate("Form", "Title:"))
        self.CirclesCountLabel.setText(_translate("Form", "Circles count:"))
        self.addtaskAddButton.setText(_translate("Form", "Add"))
        self.errorLabel.setText(_translate("Form", ""))
