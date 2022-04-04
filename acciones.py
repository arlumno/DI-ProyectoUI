import os.path
import shutil
import zipfile
import xlrd
import sys

from PyQt5 import QtWidgets

import database
import var
from tools import Tools


class Acciones():

    def comprobarCampoDni():
        try:
            dni = Tools.formatearDni(var.menu.etDni.text())
            var.menu.etDni.setText(dni)
            if Tools.validarDni(dni):
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

        except Exception as error:
            print("Error al seleccionar el pago: " + str(error))

    def cargarProvincias():
        try:
            # provincias = ['','Pontevedra','Ourense','Lugo','A Coruña']
            # He cargado una tabla de provincias en la base de datos.
            database.Database.cargarProvincias()

            for i in var.listadoProvincias:
                var.menu.cbProvincia.addItem(i)
        except Exception as error:
            print("Error al cargar pronvincias: " + str(error))

    def selProvincia(prov):
        global provincia
        provincia = prov
        # print('Provincia seleccionada: ' + prov)

    def cargarEnvios():
        var.listadoEnvios = ['Recogida por cliente',
                              'Envío nacional paquetería exprés urgente',
                              'Envío nacional paquetería normal',
                              'Envío internacional']
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
            var.dLog.ui.etLog.appendPlainText("[" + Tools.fechaActual("%H:%M:%S %d/%m/%Y") +"] \n   "+ str(msg))
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
                                    var.sexo,
                                    var.menu.sbEnvio.value()]

                    clienteBd = database.Database.obtenerCliente(nuevoCliente[0])
                    if clienteBd is not None:
                        Acciones.cargarCliente(clienteBd)

                    if not Acciones.isClientecargado():
                        if database.Database.guardarCliente(nuevoCliente) :
                            Tools.ventanaAdvertencia("Nuevo cliente grabado con éxito.")
                            Acciones.anunciarStatusBar("Cliente con dni "+ nuevoCliente[0]+ " grabado con éxito")
                        else:
                            Tools.ventanaAdvertencia("Error al guardar el cliente.")
                    else:
                        if Tools.ventanaConfirmacion("Confirma Modificar el Cliente:", "Modificar Cliente",str(nuevoCliente)):
                            if database.Database.modificarCliente(nuevoCliente):
                                Tools.ventanaAdvertencia("Cliente modificado con éxito.")
                                Acciones.anunciarStatusBar("Cliente con dni " + nuevoCliente[0] + " modificado con éxito")
                            else:
                             Tools.ventanaAdvertencia("Error al modificar el cliente.")
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
                                    var.menu.etFechaAlta.text(),
                                    var.menu.cbProvincia.currentText(),
                                    var.pago,
                                    var.sexo,
                                    var.menu.sbEnvio.value()]

                clienteBd = database.Database.obtenerCliente(clienteModificado[0])
                if clienteBd is not None:
                    Acciones.cargarCliente(clienteBd)

                if Acciones.isClientecargado():
                    if clienteModificado != var.clienteCargado:
                        if Tools.ventanaConfirmacion("Confirma Modificar el Cliente:", "Modificar Cliente", str(clienteModificado)):
                            database.Database.modificarCliente(clienteModificado)
                            Acciones.cargarClientes()
                            Tools.ventanaAdvertencia("Cliente modificado con éxito.")
                            Acciones.anunciarStatusBar("Cliente con dni " + clienteModificado[0] + " modificado con éxito")

                    else:
                        Tools.ventanaAdvertencia("No hay cambios")

                else:
                    Tools.ventanaAdvertencia("No hay clientes seleccionados")

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
        if Tools.ventanaConfirmacion("Confirma Eliminar el Cliente:","Eliminar Cliente", str(var.clienteCargado)):
            if database.Database.eliminarCliente(var.clienteCargado[0]):
                Acciones.anunciarStatusBar("Clientes con dni "+var.clienteCargado[0]+ " Eliminado")
            else:
                Tools.ventanaAdvertencia("Error al eliminar el cliente con dni: " + var.clienteCargado[0])
                database.Database.eliminarCliente(var.clienteCargado[0])
            Acciones.limpiarCamposCliente()
            Acciones.cargarClientes()

    def importarListadoClientes(listadoClientesImportar):
        if Tools.ventanaConfirmacion("Hay un total de " + str(len(listadoClientesImportar)) + " clientes para importar. Los clientes existentes se actualizarán. \n¿Está seguro?", "Importar Clientes", None, str(listadoClientesImportar)):
            database.Database.importarListadoClientes(listadoClientesImportar)
            Acciones.limpiarCamposCliente()
            Acciones.cargarClientes()

    def abrirClienteSeleccionado():
        try:
            rowCliente = var.menu.tablaDatos.selectedIndexes()[0].row()
            Acciones.abrirCliente(var.listadoClientes[rowCliente])
        except IndexError as error:
            Tools.ventanaAdvertencia("No hay clientes seleccionados.")

    def eliminarClienteSeleccionado():
        try:
            rowCliente = var.menu.tablaDatos.selectedIndexes()[0].row()
            Acciones.cargarCliente(var.listadoClientes[rowCliente])
            Acciones.eliminarCliente()
        except IndexError as error:
            Tools.ventanaAdvertencia("No hay clientes seleccionados.")

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

        if cliente[8] != "":
            var.menu.sbEnvio.setValue(cliente[8])

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
        var.menu.sbEnvio.setValue(0)
        var.menu.etEnvio.setText(var.listadoEnvios[0])

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
        elif not Tools.validarDni(var.menu.etDni.text()):
            errores += "\n  Dato no válido: DNI"
            resultado = False

        if var.menu.etNombre.text() == "":
            errores += "\n  Camplo Vacio: Nombre"
            resultado = False

        if var.menu.etApellido.text() == "":
            errores += "\n  Camplo Vacio: Apellidos"
            resultado = False

        #opcional
        #opcional
        # if var.menu.etDireccion.text() == "":
        #     errores += "\n  Camplo Vacio: Direccion"
        #     resultado = False

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
            Tools.ventanaAdvertencia("Operación no realizada. Faltan datos.\n Debe rellenar todos los campos.", "Error en los camplos", errores)

        return resultado

    def anunciarStatusBar(msg):
        var.menu.lbStatus.setText("["+ Tools.fechaActual() + "] "+msg)
        Acciones.addToLog(msg)

    def abrirCarpeta():
        try:
            return var.dFileOpen.show()
        except Exception as error:
            print("Error al abrir el explorador: " + str(error))

    def descargarBd():
        try:
            archivoSalida = str(Tools.fechaActual('%Y.%m.%d.%H.%M.%S')) + '_backup.zip'
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

            if dirName and Tools.ventanaConfirmacion("Estas seguro de restaurar la BD","¡Atención!",None,dirName):
                archivoZip = zipfile.ZipFile(dirName, 'r')

                database.Database.disconnect()  #desconectamos para poder renombrar la base de datos actual
                os.replace(var.fileDb, var.fileDb + "_last") #le cambiamos el nombre y la dejamos como copia de seguridad

                try:
                    archivoZip.extract(var.fileDb) #extraemos la base de datos del archivo zip.
                    Acciones.anunciarStatusBar("Base de datos restaurada")
                    Acciones.cargarListaClientes()
                    Tools.ventanaAdvertencia("Base de datos restaurada con éxito.")
                except Exception as error: #si da error, deshacemos el cambio.
                    os.replace(var.fileDb + "_last", var.fileDb)  # le cambiamos el nombre y la dejamos como copia de seguridad
                    Tools.ventanaAdvertencia("No se ha podido restaurar la Base de datos","error",str(error))

                database.Database.connect() #conectamos de nuevo la bd.
                Acciones.cargarClientes()


        except Exception as error:
            Tools.ventanaAdvertencia("No se ha podido restaurar la Base de datos","error",str(error))

    def borrarClientesBd():
        if Tools.ventanaConfirmacion("¿Estas seguro de Borrar todos los clientes la Base De Datos?", "¡Atención!"):
            ## esto borra el archivo de BD. incluida la tabla de Provincias....
            # try:
            #     database.Database.disconnect()
            #     os.remove(var.fileDb)
            #     Tools.ventanaAdvertencia("Base de datos BORRADA")
            #     Acciones.anunciarStatusBar("Base de datos eliminada")
            # except Exception as error:
            #     Tools.ventanaAdvertencia("Error al Borrar la Base de datos", "error", str(error))
            # database.Database.connect()  # conectamos de nuevo la bd
            if database.Database.borrarClientes():
                Tools.ventanaAdvertencia("Se han eliminado todos los registros de clientes.")
                Acciones.anunciarStatusBar("Eliminados todos los clientes")
            else:
                Tools.ventanaAdvertencia("Error al eliminar registros")
            Acciones.cargarClientes()

    def importarDatos():
        try:
            dirName, fileName = var.dFileOpen.getOpenFileName(None, None, None, "*.xls *.XLS", )
            archivoXls = xlrd.open_workbook(dirName)
            hoja1 = archivoXls.sheet_by_index(0)
            if hoja1.nrows > 0 and hoja1.ncols >0:
                #cabeceras
                dniIndex = apellidosIndex = nombreIndex = direccionIndex = fecha_altaIndex = provinciaIndex = forma_pagoIndex = sexoIndex = None
                for i in range(hoja1.ncols):
                    cabecera = str(hoja1.cell_value(0,i)).upper()
                    if cabecera == "DNI": dniIndex = i
                    elif cabecera == "APELLIDOS": apellidosIndex = i
                    elif cabecera == "APELIDOS": apellidosIndex = i
                    elif cabecera == "NOMBRE": nombreIndex = i
                    elif cabecera == "NOME": nombreIndex = i
                    elif cabecera == "DIRECCION": direccionIndex = i
                    elif cabecera == "FECHA_ALTA": fecha_altaIndex = i
                    elif cabecera == "PROVINCIA": provinciaIndex = i
                    elif cabecera == "FORMA_PAGO": forma_pagoIndex = i
                    elif cabecera == "SEXO": sexoIndex = i
                #campos obligatorios
                if dniIndex is None or apellidosIndex is None or nombreIndex is None or direccionIndex is None or provinciaIndex is None or sexoIndex is None :
                    Tools.ventanaAdvertencia("Faltan campos obligatorios en el archivo")
                else:
                    listadoClientesImportar = []
                    for e in range(1, hoja1.nrows):
                        dni = str(hoja1.cell_value(e,dniIndex))
                        apellidos = str(hoja1.cell_value(e,apellidosIndex))
                        nombre = str(hoja1.cell_value(e,nombreIndex))
                        direccion = str(hoja1.cell_value(e,direccionIndex))
                        if fecha_altaIndex is None:
                            fecha_alta = ""
                        else:
                            fecha_alta = str(hoja1.cell_value(e,fecha_altaIndex))
                        provincia = str(hoja1.cell_value(e,provinciaIndex))
                        if forma_pagoIndex is None:
                            forma_pago = ""
                        else:
                            forma_pago = str(hoja1.cell_value(e,forma_pagoIndex))
                        sexo = str(hoja1.cell_value(e,sexoIndex))
                        clienteImportar = [dni,apellidos,nombre,direccion,fecha_alta,provincia,forma_pago,sexo,None]
                        # print(clienteImportar)
                        listadoClientesImportar.append(clienteImportar)
                    Acciones.importarListadoClientes(listadoClientesImportar)

            else:
                Tools.ventanaAdvertencia("No hay datos para importar en el archivo")

        except Exception as error:
            Tools.ventanaAdvertencia("No se han podido importar los datos", "error", str(error))

    def asignarEnvio():
        # print(var.menu.sbEnvio.value())
        # print("cosas")
        var.menu.etEnvio.setText(var.listadoEnvios[var.menu.sbEnvio.value()])