import sys
from PyQt5 import QtWidgets, uic

#import pyqtgraph as pygraph
from InterfacePuissanceGant import Ui_MainWindow



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.Button_ModeManuel.clicked.connect(boutonAppuye)
        #self.Button_ModeManuel.released.connect(boutonRelache)


app = QtWidgets.QApplication(sys.argv)


def boutonAppuye():
    if window.Button_ModeManuel.isChecked():
        window.Text_EtatDuRobot.setText("Mode manuel activé \nEntrer le pourcentage du moteur choisi \n\nFormat : 50")
    else:
        window.Text_EtatDuRobot.setText("Mode automatique activé")

def boutonRelache():
    window.Text_EtatDuRobot.setText("no benis")


window = MainWindow()

window.show()
app.exec()
