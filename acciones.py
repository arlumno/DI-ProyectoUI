import os.path
import shutil
import zipfile
import xlrd

import clientes
import datetime
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import database
import var


class Acciones():

    def comprobarCampoDni():
        try:
            dni = clientes.Clientes.formatearDni(var.menu.etDni.text())
            var.menu.etDni.setText(dni)
            if clientes.Clientes.validarDni(dni):
                var.menu.flagDni.setStyleSheet('QLabel {color: green;}')
                var.menu.flagDni.setText("V")
            else:
                var.menu.flagDni.setStyleSheet('QLabel {color: red;}')
                var.menu.flagDni.setText("X")
        except Exception as error:
            print("Error al comprobar dni: " + str(error))

    def salir():
        try:
            var.dSalir.show()
            if var.dSalir.exec():
                sys.exit()
            else:
                var.dSalir.hide()
        except Exception as error:
            print("error s%:" % str(error))

    def selSexo():
        var.sexo = ""
        try:
            if var.menu.rbFemenino.isChecked():
                var.sexo = "Mujer"
                Acciones.addToLog('Marcado Femenino')
            elif var.menu.rbMasculino.isChecked():
                var.sexo = "Hombre"
                Acciones.addToLog('Marcado Masculino')
        except Exception as error:
            print("Error al seleccionar sexo: " + str(error))

    def selPago():
        var.pago = ""
        try:
            msg = '--- Pagos seleccionados: '
            if var.menu.chkEfectivo.isChecked():
                var.pago += 'Efectivo '
            if var.menu.chkTarjeta.isChecked():
                var.pago += 'Tarjeta '
            if var.menu.chkTransfer.isChecked():
                var.pago += 'Transferencia '
            msg = msg + var.pago
            Acciones.addToLog(msg) #TODO cambiar a otros lados

        except Exception as error:
            print("Error al seleccionar el pago: " + str(error))

    def cargarProvincias():
        try:
            # provincias = ['','Pontevedra','Ourense','Lugo','A Coruña']
            database.Database.cargarProvincias()

            for i in var.listadoProvincias:
                var.menu.cbProvincia.addItem(i)
        except Exception as error:
            print("Error al cargar pronvincias: " + str(error))

    def selProvincia(prov):
        global provincia
        provincia = prov
        # print('Provincia seleccionada: ' + prov)

    def abrirCalendar():
        try:
            var.dCalendar.show()
        except Exception as error:
            print("Error al abrir la ventana de calendario: " + str(error))

    def asignarFecha(qDate):
        try:
            fecha = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.menu.etFechaAlta.setText(str(fecha))
            var.dCalendar.hide()
        except Exception as error:
            print("Error al asignar fecha de alta: " + str(error))

    def abrirLog():
        try:
            var.dLog.show()
        except Exception as error:
            print("Error al abrir la ventana de Log: " + str(error))

    def addToLog(msg):
        try:
            var.dLog.ui.etLog.appendPlainText("[" + Acciones.fechaActual("%H:%M:%S %d/%m/%Y") +"] \n   "+ str(msg))
        except Exception as error:
            print("Error en el Log" + str(error))


    def grabarNuevoCliente():
            try:
                if Acciones.validarCampos():
                    nuevoCliente = [var.menu.etDni.text(),
                                    var.menu.etApellido.text(),
                                    var.menu.etNombre.text(),
                                    var.menu.etDireccion.text(),
                                    var.menu.etFechaAlta.text(),
                                    var.menu.cbProvincia.currentText(),
                                    var.pago,
                                    var.sexo]

                    # print(nuevoCliente)
                    database.Database.cargarCliente(nuevoCliente[0])

                    if not Acciones.isClientecargado():
                        database.Database.guardarCliente(nuevoCliente)
                        Acciones.ventanaAdvertencia("Nuevo cliente grabado con éxito.")
                        Acciones.anunciarStatusBar("Cliente con dni "+ nuevoCliente[0]+ " grabado con éxito")
                    else:
                        if Acciones.ventanaConfirmacion("Confirma Modificar el Cliente:", "Modificar Cliente",str(nuevoCliente)):
                            database.Database.modificarCliente(nuevoCliente)
                            Acciones.ventanaAdvertencia("Cliente modificado con éxito.")
                            Acciones.anunciarStatusBar("Cliente con dni " + nuevoCliente[0] + " modificado con éxito")

                    Acciones.cargarClientes()
                else:
                    print("Operación no realizada, Faltan datos.")

            except Exception as error:
                print("Error al guardar cliente: " + str(error))

    def guardarCambiosCliente():
        try:
            if Acciones.validarCampos():
                clienteModificado = [var.menu.etDni.text(),
                                var.menu.etApellido.text(),
                                var.menu.etNombre.text(),
                                var.menu.etDireccion.text(),
                                var.menu.cbProvincia.currentText(),
                                var.pago,
                                var.sexo,
                                var.menu.etFechaAlta.text()]

                database.Database.cargarCliente(clienteModificado[0])
                if Acciones.isClientecargado():
                    if clienteModificado != var.clienteCargado:
                        if Acciones.ventanaConfirmacion("Confirma Modificar el Cliente:", "Modificar Cliente", str(clienteModificado)):
                            database.Database.modificarCliente(clienteModificado)
                            Acciones.cargarClientes()
                            Acciones.ventanaAdvertencia("Cliente modificado con éxito.")
                            Acciones.anunciarStatusBar("Cliente con dni " + clienteModificado[0] + " modificado con éxito")

                    else:
                        Acciones.ventanaAdvertencia("No hay cambios")

                else:
                    Acciones.ventanaAdvertencia("No hay clientes seleccionados")

        except Exception as error:
            print("Error al guardar cliente: " + str(error))

    def cargarListaClientes():
        var.menu.tablaDatos.setRowCount(0)
        if len(var.listadoClientes)>0:
            row = 0
            for registro in var.listadoClientes:
                var.menu.tablaDatos.insertRow(row)
                col = 0
                for campo in registro:
                    celda = QtWidgets.QTableWidgetItem(campo)
                    var.menu.tablaDatos.setItem(row, col, celda)
                    col += 1
                row += 1
            Acciones.anunciarStatusBar("Lista de clientes cargada con éxito")

    def cargarClientes():
        Acciones.limpiarCamposCliente()
        database.Database.cargarClientes()
        Acciones.cargarListaClientes()

    def cargarCliente(cliente):
        var.menu.bEliminarCliente.setVisible(True)
        var.menu.bGuardarCambios.setVisible(True)
        var.menu.bNuevoCliente.setVisible(False)
        var.clienteCargado = cliente

    def descargarCliente():
        var.menu.bEliminarCliente.setVisible(False)
        var.menu.bGuardarCambios.setVisible(False)
        var.menu.bNuevoCliente.setVisible(True)
        var.clienteCargado = []

    def isClientecargado():
        if len(var.clienteCargado) >0:
            return  True
        return False

    def filtrarClientes():
        filtro = str(var.menu.etFiltro.text())
        database.Database.filtrarClientes(filtro)
        Acciones.cargarListaClientes()

    def limpiarListadoClientes():
        var.menu.tablaDatos.setRowCount(0)

    def eliminarCliente():
        if Acciones.ventanaConfirmacion("Confirma Eliminar el Cliente:","Eliminar Cliente", str(var.clienteCargado)):
            database.Database.eliminarCliente(var.clienteCargado[0])
            Acciones.anunciarStatusBar("Clientes con dni "+var.clienteCargado[0]+ " Eliminado")
            Acciones.limpiarCamposCliente()
            Acciones.cargarClientes()

    def abrirClienteSeleccionado():
        try:
            rowCliente = var.menu.tablaDatos.selectedIndexes()[0].row()
            Acciones.abrirCliente(var.listadoClientes[rowCliente])
        except IndexError as error:
            Acciones.ventanaAdvertencia("No hay clientes seleccionados.")

    def eliminarClienteSeleccionado():
        try:
            rowCliente = var.menu.tablaDatos.selectedIndexes()[0].row()
            Acciones.cargarCliente(var.listadoClientes[rowCliente])
            Acciones.eliminarCliente()
        except IndexError as error:
            Acciones.ventanaAdvertencia("No hay clientes seleccionados.")

    def abrirCliente(cliente):
        Acciones.limpiarCamposCliente()
        Acciones.cargarCliente(cliente)

        var.menu.etDni.setText(cliente[0])
        Acciones.comprobarCampoDni()
        var.menu.etApellido.setText(cliente[1])
        var.menu.etNombre.setText(cliente[2])
        var.menu.etDireccion.setText(cliente[3])
        var.menu.etFechaAlta.setText(cliente[7])
        var.menu.cbProvincia.setCurrentText(cliente[4])

        var.sexo = cliente[6]
        if cliente[6] == "Hombre":
            var.menu.rbMasculino.setChecked(True)
        elif cliente[6] == "Mujer":
            var.menu.rbFemenino.setChecked(True)

        var.pago = cliente[5]
        pagos = cliente[5].split(" ")

        for pago in pagos:
            if pago == var.menu.chkEfectivo.text():
                var.menu.chkEfectivo.setChecked(True)
            if pago == var.menu.chkTarjeta.text():
                var.menu.chkTarjeta.setChecked(True)
            if pago == var.menu.chkTransfer.text():
                var.menu.chkTransfer.setChecked(True)


    def limpiarCamposCliente():
        var.menu.etDni.setText("")
        var.menu.etApellido.setText("")
        var.menu.etNombre.setText("")
        var.menu.etDireccion.setText("")
        var.menu.etFechaAlta.setText("")
        var.menu.flagDni.setText("")
        var.menu.cbProvincia.setCurrentText("")

        var.menu.rbgSexo.setExclusive(False)
        var.menu.rbMasculino.setChecked(False)
        var.menu.rbFemenino.setChecked(False)
        var.menu.rbgSexo.setExclusive(True)

        var.menu.chkEfectivo.setChecked(False)
        var.menu.chkTarjeta.setChecked(False)
        var.menu.chkTransfer.setChecked(False)

        Acciones.descargarCliente()

    def validarCampos():
        resultado = True
        errores = "Errores:"
        if var.menu.etDni.text() == "":
            errores += "\n  Camplo Vacio: DNI"
            resultado = False
        elif not clientes.Clientes.validarDni(var.menu.etDni.text()):
            errores += "\n  Dato no válido: DNI"
            resultado = False

        if var.menu.etNombre.text() == "":
            errores += "\n  Camplo Vacio: Nombre"
            resultado = False

        if var.menu.etApellido.text() == "":
            errores += "\n  Camplo Vacio: Apellidos"
            resultado = False

        if var.menu.etDireccion.text() == "":
            errores += "\n  Camplo Vacio: Direccion"
            resultado = False

        # if var.menu.etFechaAlta.text() == "":
        #     print("Campo incompleto (Fecha de Alta) - Optativo")
        #     #resultado = False

        if var.menu.cbProvincia.currentText() == "":
            errores += "\n  Sin seleccionar: Provincia"
            resultado = False


        if not (var.menu.rbMasculino.isChecked() or var.menu.rbFemenino.isChecked()):
            errores += "\n  Sin seleccionar: Sexo"
            resultado = False

        if not resultado:
            Acciones.ventanaAdvertencia("Operación no realizada. Faltan datos.\n Debe rellenar todos los campos.", "Error en los camplos", errores)

        return resultado

    def ventanaConfirmacion(mensaje ="", titulo ="Atención", descripcion ="",descripcionExtendida = ""):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
        msg.setInformativeText(descripcion)
        if descripcionExtendida != "":
            msg.setDetailedText(descripcionExtendida)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if msg.exec_() == QMessageBox.Ok:
            return True
        else:
            return False


    def ventanaAdvertencia(mensaje = "", titulo="Atención", descripcion=""):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        # msg.setInformativeText("This is additional information")
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
        msg.setDetailedText(descripcion)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def anunciarStatusBar(msg):

        var.menu.lbStatus.setText("["+ Acciones.fechaActual() + "]"+msg)
        Acciones.addToLog(msg)

    def abrirCarpeta():
        try:
            return var.dFileOpen.show()
        except Exception as error:
            print("Error al abrir el explorador: " + str(error))

    def descargarBd():
        try:
            archivoSalida = str(Acciones.fechaActual('%Y.%m.%d.%H.%M.%S')) + '_backup.zip'
            option = QtWidgets.QFileDialog.Options()
            directorio, archivo = var.dFileOpen.getSaveFileName(None,"Descargar Copia",archivoSalida, '.zip', options=option)
            if var.dFileOpen.Accepted and archivo != '':
                archivoZip = zipfile.ZipFile(archivoSalida,'w')
                archivoZip.write(var.fileDb, os.path.basename(var.fileDb),zipfile.ZIP_DEFLATED)
                archivoZip.close()
                Acciones.anunciarStatusBar("Base de datos descargada con éxito")
                shutil.move(str(archivoSalida),str(directorio))

        except Exception as error:
            print("Error al descargar la base de datos: " + str(error))

    def restaurarBd():
        try:
            dirName, fileName = var.dFileOpen.getOpenFileName(None,None,None,"*.zip *.ZIP",)

            if dirName and Acciones.ventanaConfirmacion("Estas seguro de restaurar la BD","¡Atención!",None,dirName):
                archivoZip = zipfile.ZipFile(dirName, 'r')

                database.Database.disconnect()  #desconectamos para poder renombrar la base de datos actual
                os.replace(var.fileDb, var.fileDb + "_last") #le cambiamos el nombre y la dejamos como copia de seguridad

                try:
                    archivoZip.extract(var.fileDb) #extraemos la base de datos del archivo zip.
                    Acciones.anunciarStatusBar("Base de datos restaurada")
                    Acciones.cargarListaClientes()
                    Acciones.ventanaAdvertencia("Base de datos restaurada con éxito.")
                except Exception as error: #si da error, deshacemos el cambio.
                    os.replace(var.fileDb + "_last", var.fileDb)  # le cambiamos el nombre y la dejamos como copia de seguridad
                    Acciones.ventanaAdvertencia("No se ha podido restaurar la Base de datos","error",str(error))

                database.Database.connect() #conectamos de nuevo la bd.
                Acciones.cargarClientes()


        except Exception as error:
            Acciones.ventanaAdvertencia("No se ha podido restaurar la Base de datos","error",str(error))

    def borrarBd():
        if Acciones.ventanaConfirmacion("¿Estas seguro de Borrar toda la Base De Datos?", "¡Atención!"):

            try:
                database.Database.disconnect()
                os.remove(var.fileDb)
                Acciones.ventanaAdvertencia("Base de datos BORRADA")
                Acciones.anunciarStatusBar("Base de datos eliminada")
            except Exception as error:
                Acciones.ventanaAdvertencia("Error al Borrar la Base de datos", "error", str(error))

            database.Database.connect()  # conectamos de nuevo la bd
            Acciones.cargarClientes()

    def importarDatos():
        try:
            dirName, fileName = var.dFileOpen.getOpenFileName(None, None, None, "*.xls *.XLS", )

            if dirName and Acciones.ventanaConfirmacion("Estas seguro de importar los datos la BD", "¡Atención!", None, dirName):
                archivoXls = xlrd.open_workbook(dirName)
                hoja1 = archivoXls.sheet_by_index(0)

        except Exception as error:
            Acciones.ventanaAdvertencia("No se han podido importar los datos", "error", str(error))

    def fechaActual(format= "%d/%m/%Y"):
        fecha = datetime.datetime.today()
        fecha = fecha.strftime(format)
        return str(fecha)