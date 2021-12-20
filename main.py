import sys, var
from datetime import datetime

import acciones
from UiDialogSalir import *
from UiGestionClientes import *
from UiDialogLog import *
from UiDialogCalendar import *

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.menu = Ui_MainWindow()
        var.menu.setupUi(self)

        var.dSalir = DialogSalir()
        var.dCalendar = DialogCalendar()

        var.dLog = DialogLog()
        # var.dLog.show()

        # acciones.Acciones.addToLog("prueba de texto 1")
        # acciones.Acciones.addToLog("prueba de texto 2")

        var.menu.actionSalir.triggered.connect(acciones.Acciones.salir)
        var.menu.bSalir.clicked.connect(acciones.Acciones.salir)
        var.menu.etDni.editingFinished.connect(acciones.Acciones.comprobarCampoDni)

        var.menu.actionLog.triggered.connect(acciones.Acciones.abrirLog)

        var.menu.rbgSexo.buttonClicked.connect(acciones.Acciones.selSexo)
        #var.menu.rbFemenino.toggled.connect(acciones.Acciones.selSexo)
        #var.menu.rbMasculino.toggled.connect(acciones.Acciones.selSexo)

        var.menu.chkEfectivo.stateChanged.connect(acciones.Acciones.selPago)
        var.menu.chkTarjeta.stateChanged.connect(acciones.Acciones.selPago)
        var.menu.chkTransfer.stateChanged.connect(acciones.Acciones.selPago)

        acciones.Acciones.cargarPronvincias()
        var.menu.cbProvincia.activated[str].connect(acciones.Acciones.selProvincia)

        var.menu.bCalendar.clicked.connect(acciones.Acciones.abrirCalendar)




class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        self.ui = Ui_DialogSalir()
        self.ui.setupUi(self)

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        self.ui = Ui_DialogCalendar()
        self.ui.setupUi(self)
        diaHoy = datetime.now().day
        mesHoy = datetime.now().month
        anhoHoy = datetime.now().year

        self.ui.calendarWidget.setSelectedDate(QtCore.QDate(anhoHoy,mesHoy,diaHoy))
        self.ui.calendarWidget.clicked.connect(acciones.Acciones.asignarFecha)

class DialogLog(QtWidgets.QDialog):
    def __init__(self):
        super(DialogLog, self).__init__()
        self.ui = Ui_DialogLog()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    wMain = Main()
    wMain.show()
    #var.dLog.show() #en proceso
    # acciones.Acciones.addToLog()
    sys.exit(app.exec())

