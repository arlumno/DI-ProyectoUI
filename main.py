import sys, var
import acciones
from UiDialogSalir import *
from UiGestionClientes import *
from UiDialogLog import *

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.menu = Ui_MainWindow()
        var.menu.setupUi(self)

        var.menu.actionSalir.triggered.connect(acciones.Acciones.salir)
        var.menu.bSalir.clicked.connect(acciones.Acciones.salir)
        var.menu.etDni.editingFinished.connect(acciones.Acciones.comprobarCampoDni)

        var.menu.rbgSexo.buttonClicked.connect(acciones.Acciones.selSexo)
        #var.menu.rbFemenino.toggled.connect(acciones.Acciones.selSexo)
        #var.menu.rbMasculino.toggled.connect(acciones.Acciones.selSexo)

        var.menu.chkEfectivo.stateChanged.connect(acciones.Acciones.selPago)
        var.menu.chkTarjeta.stateChanged.connect(acciones.Acciones.selPago)
        var.menu.chkTransfer.stateChanged.connect(acciones.Acciones.selPago)

        acciones.Acciones.cargarPronvincias()
        var.menu.cbProvincia.activated[str].connect(acciones.Acciones.selProvincia)


class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        dSalir = Ui_DialogSalir()
        dSalir.setupUi(self)

class DialogLog(QtWidgets.QDialog):
    def __init__(self):
        super(DialogLog, self).__init__()
        dLog = Ui_DialogLog()
        dLog.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    windows = Main()
    var.dSalir = DialogSalir()
    var.dLog = DialogLog()
    windows.show()
   # var.dLog.show() #en proceso

    #acciones.Acciones.addToLog()
    sys.exit(app.exec())

