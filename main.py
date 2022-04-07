import sys, var
from datetime import datetime

from UiDialogSalir import *
from UiGestionClientes import *
from UiDialogLog import *
from UiDialogCalendar import *
import acciones, database

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import informes


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.menu = Ui_MainWindow()
        var.menu.setupUi(self)

        var.dSalir = DialogSalir()
        var.dCalendar = DialogCalendar()
        var.dLog = DialogLog()
        var.dFileOpen = FileDialogAbrir()

        # var.dLog.show()
        database.Database.connect()

        acciones.Acciones.cargarProvincias()
        acciones.Acciones.cargarEnvios()

        acciones.Acciones.cargarClientes()

        acciones.Acciones.limpiarCamposCliente()
        var.menu.statusbar.addPermanentWidget(var.menu.lbStatus,1)
        acciones.Acciones.anunciarStatusBar("Bienvenido a 2º DAM - Adultos")

        var.menu.sbEnvio.setMinimum(0)
        var.menu.sbEnvio.setMaximum(len(var.listadoEnvios) - 1)
        # var.menu.sbEnvio.setValue(0)
        # var.menu.etEnvio.setText(var.listaEnvio[0])
        # acciones.Acciones.addToLog("prueba de texto 1")
        # acciones.Acciones.addToLog("prueba de texto 2")

        ### EVENTOS ###
        var.menu.cbProvincia.activated[str].connect(acciones.Acciones.selProvincia)

        # var.menu.tablaDatos.selectionModel().selectionChanged.connect(acciones.Acciones.modificarCliente)
        var.menu.tablaDatos.doubleClicked.connect(acciones.Acciones.abrirClienteSeleccionado)
        # print(var.menu.tablaDatos.selectedIndexes())
        #Botones
        var.menu.bSalir.clicked.connect(acciones.Acciones.salir)
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
        var.menu.sbEnvio.valueChanged.connect(acciones.Acciones.asignarEnvio)



        #Actions menú
        var.menu.actionSalir.triggered.connect(acciones.Acciones.salir)
        var.menu.actionLog.triggered.connect(acciones.Acciones.abrirLog)
        var.menu.actionAbrirCarpeta.triggered.connect(acciones.Acciones.abrirCarpeta)
        var.menu.actionDescargarBd.triggered.connect(acciones.Acciones.descargarBd)
        var.menu.actionRestaurarBD.triggered.connect(acciones.Acciones.restaurarBd)
        var.menu.actionBorrarBD.triggered.connect(acciones.Acciones.borrarClientesBd)
        var.menu.actionImportar_Datos.triggered.connect(acciones.Acciones.importarDatos)
        var.menu.actionGenerarInformeClientes.triggered.connect(informes.Informes.reportCli)

        #radiobuttons y checkboxs
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

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    wMain = Main()
    wMain.show()
    #var.dLog.show() #en proceso
    # acciones.Acciones.addToLog()
    sys.exit(app.exec())

