import csv
import sys

from PyQt5.QtWidgets import QWidget, QApplication

from settingswindow.UI_Settings import Ui_Form


class SettingsApp(QWidget, Ui_Form):
    def __init__(self, xcoord, ycoord, main_app):
        super().__init__()
        self.setupUi(self, xcoord, ycoord)
        self.settingsSaveButton.clicked.connect(self.saveChanges)
        self.main_app = main_app

    def personalDataWriter(self, *values_list):
        with open('config.csv', 'w', encoding="utf8") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(values_list)

    def saveChanges(self):
        try:
            focusTimeVal = int(self.FocusTimeDurationLineEdit.text()) * 60
            breakVal = int(self.BreakDurationLineEdit.text()) * 60
            LongBreakVal = int(self.LongBreakDurationLineEdit.text()) * 60
            if any(elem <= 0 for elem in [focusTimeVal, breakVal, LongBreakVal]):
                raise Exception
            self.errorLabel.setText('')
            self.personalDataWriter(focusTimeVal, breakVal, LongBreakVal)
            self.main_app.personalDataReader()
            self.main_app.ChangePeriodFunction()
            self.close()
        except Exception:
            self.errorLabel.setText('Error: incorrect input')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SettingsApp(0, 0, None)
    ex.show()
    sys.exit(app.exec())
