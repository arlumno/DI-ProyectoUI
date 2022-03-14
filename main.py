import sys, var
from datetime import datetime

from UiDialogSalir import *
from UiGestionClientes import *
from UiDialogLog import *
from UiDialogCalendar import *
from UiDialogCalendar import *
import acciones, database

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
        database.Database.connect(var.fileDb)

        acciones.Acciones.cargarPronvincias()
        acciones.Acciones.cargarClientes()
        acciones.Acciones.limpiarCamposCliente()


        # acciones.Acciones.addToLog("prueba de texto 1")
        # acciones.Acciones.addToLog("prueba de texto 2")

        ### EVENTOS ###
        var.menu.cbProvincia.activated[str].connect(acciones.Acciones.selProvincia)

        # var.menu.tablaDatos.selectionModel().selectionChanged.connect(acciones.Acciones.modificarCliente)
        var.menu.tablaDatos.doubleClicked.connect(acciones.Acciones.abrirClienteSeleccionado)
        # print(var.menu.tablaDatos.selectedIndexes())

        var.menu.actionSalir.triggered.connect(acciones.Acciones.salir)
        var.menu.bSalir.clicked.connect(acciones.Acciones.salir)
        #var.menu.bAceptar.clicked.connect(acciones.Acciones.showClients)

        var.menu.bCargarClientes.clicked.connect(acciones.Acciones.cargarClientes)
        var.menu.bFiltrarClientes.clicked.connect(acciones.Acciones.filtrarClientes)
        var.menu.etFiltro.editingFinished.connect(acciones.Acciones.filtrarClientes)

        var.menu.bLimpiarClientes.clicked.connect(acciones.Acciones.limpiarListadoClientes)

        var.menu.bEliminarClienteSeleccionado.clicked.connect(acciones.Acciones.eliminarClienteSeleccionado)
        var.menu.bEliminarCliente.clicked.connect(acciones.Acciones.eliminarCliente)
        var.menu.bModificarCliente.clicked.connect(acciones.Acciones.abrirClienteSeleccionado)
        var.menu.bGuardarCambios.clicked.connect(acciones.Acciones.guardarCambiosCliente)
        var.menu.bNuevoCliente.clicked.connect(acciones.Acciones.grabarNuevoCliente)
        var.menu.bLimpiarCampos.clicked.connect(acciones.Acciones.limpiarCamposCliente)

        var.menu.etDni.editingFinished.connect(acciones.Acciones.comprobarCampoDni)

        var.menu.actionLog.triggered.connect(acciones.Acciones.abrirLog)

        var.menu.rbgSexo.buttonClicked.connect(acciones.Acciones.selSexo)
        # var.menu.rbFemenino.toggled.connect(acciones.Acciones.selSexo)
        # var.menu.rbMasculino.toggled.connect(acciones.Acciones.selSexo)

        var.menu.chkEfectivo.stateChanged.connect(acciones.Acciones.selPago)
        var.menu.chkTarjeta.stateChanged.connect(acciones.Acciones.selPago)
        var.menu.chkTransfer.stateChanged.connect(acciones.Acciones.selPago)

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

