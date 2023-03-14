import csv
import sys

from PyQt5.QtWidgets import QWidget, QApplication

from settingswindow.UI_Settings import Ui_Form
from initfiles import config_path


class SettingsApp(QWidget, Ui_Form):
    def __init__(self, xcoord, ycoord, main_app):
        super().__init__()
        # Setting main app source and position
        self.setupUi(self, xcoord, ycoord)
        self.main_app = main_app

        self.settingsSaveButton.clicked.connect(self.saveChanges)

    # Fuction to write data to user config
    def personalDataWriter(self, *values_list):
        with open(config_path, 'w', encoding="utf8") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(values_list)

    # Saving new user config data
    def saveChanges(self):
        try:
            # Fetching and checking values
            focusTimeVal = int(self.FocusTimeDurationLineEdit.text()) * 60
            breakVal = int(self.BreakDurationLineEdit.text()) * 60
            LongBreakVal = int(self.LongBreakDurationLineEdit.text()) * 60
            if any(elem <= 0 for elem in [focusTimeVal, breakVal, LongBreakVal]):
                raise Exception
            self.errorLabel.setText('')
            self.personalDataWriter(focusTimeVal, breakVal, LongBreakVal)
            # Reading new data in main app, and changing period to Focus Time
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
