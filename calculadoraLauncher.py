import sys, var

from calculadora import *

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.menu = Ui_Calculadora()
        var.menu.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    wMain = Main()
    wMain.show()
    sys.exit(app.exec())

