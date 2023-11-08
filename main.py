import sys
import self
from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class Myform(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


        self.show()

    def rezerwacja(self):
        koszt = 0

        if self.ui.checkBox .isChecked():
            cena = 200
        else:
            cena = 0

    def wyswietl(self):
        if self.ui.rezerwuj.isChecked():
            self.ui.wyswietl.show()


    def radio(self):
        lekarz = str

        if self.ui.internista.isChecked():
            lekarz.append("internista")
        if self.ui.pediatra.isChecked():
            lekarz.append("Pediatra")
        if self.ui.dermatolog.isChecked():
            lekarz.append("dermatolog")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Myform()
    window.show()
    sys.exit(app.exec())



