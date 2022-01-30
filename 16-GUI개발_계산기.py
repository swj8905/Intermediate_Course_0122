from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic

ui_file = "./calculator.ui"
class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file, self)
        self.equalbutton.clicked.connect(self.calculate)

    def calculate(self):
        user_input = self.inputbox.text()
        self.inputbox.clear()
        result = eval(user_input)
        self.history.append(f"{user_input}\n= {result}\n")


QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())