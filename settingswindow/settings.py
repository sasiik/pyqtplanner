import sys

from PyQt5.QtWidgets import QWidget, QApplication

from settingswindow.UI_Settings import Ui_Form

import mainwindow.main

class SettingsApp(QWidget, Ui_Form):
    def __init__(self, xcoord, ycoord):
        super().__init__()
        self.setupUi(self, xcoord, ycoord)
        self.settingsSaveButton.clicked.connect(self.saveChanges)

    def saveChanges(self):
        print('saved')
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SettingsApp()
    ex.show()
    sys.exit(app.exec())

