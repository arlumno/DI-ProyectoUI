import sys, var
import acciones
from UiDialogSalir import *
from UiGestionClientes import *

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.menu = Ui_MainWindow()
        var.menu.setupUi(self)
        var.menu.actionSalir.triggered.connect(acciones.Acciones.salir)
        var.menu.bSalir.clicked.connect(acciones.Acciones.salir)
        var.menu.etDni.editingFinished.connect(acciones.Acciones.comprobarCampoDni)
        # var.menu.etDni.editingFinished.connect(clientes.Clientes.comprobarCampoDni)

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        dSalir = Ui_Dialog()
        dSalir.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    windows = Main()
    var.dSalir = DialogSalir()
    windows.show()
    sys.exit(app.exec())

