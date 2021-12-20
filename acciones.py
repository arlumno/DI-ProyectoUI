import datetime
import sys, clientes

import var
class Acciones():
    # def ejemploPulsar():
    #     var.menu.pushButton_2.setText("miau")
    # def ejemplo02():
    #     var.menu.pushButton.setText("muaheahhea")
    # def slider():
    #     print("slider")
    #     var.menu.lcdNumber.setProperty("value", var.menu.horizontalSlider.value())
    # def dial():
    #     print("dial")
    #     # var.menu.lcdNumber.setText("2323")
    #     # var.menu.textBrowser.setTextsetText(var.menu.dial.value())
    #     var.menu.label.setText(var.menu.dial.value())
    #     # print(var.menu.horizontalSlider.value())
    def comprobarCampoDni():
        try:
            dni = clientes.Clientes.formatearDni(var.menu.etDni.text())
            var.menu.etDni.setText(dni)
            # dni.toUpper()
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
        try:
            if var.menu.rbFemenino.isChecked():
                print('Marcado Femenino')
                Acciones.addToLog('Marcado Femenino')
            elif var.menu.rbMasculino.isChecked():
                print('Marcado Masculino')
                Acciones.addToLog('Marcado Masculino')
        except Exception as error:
            print("Error al seleccionar sexo: " + str(error))

    def selPago():
        try:
            msg = '--- Pagos seleccionados: '
            if var.menu.chkEfectivo.isChecked():
                msg += '\n    Efectivo'
            if var.menu.chkTarjeta.isChecked():
                msg += '\n    Tarjeta'
            if var.menu.chkTransfer.isChecked():
                msg += '\n    Transferencia'
            print(msg)
            Acciones.addToLog(msg)

        except Exception as error:
            print("Error al seleccionar el pago: " + str(error))

    def cargarPronvincias():
        try:
            provincias = ['','Pontevedra','Ourense','Lugo','A Coruña']
            for i in provincias:
                var.menu.cbProvincia.addItem(i)
        except Exception as error:
            print("Error al cargar pronvincias: " + str(error))

    def selProvincia(provincia):
        try:
            print('Provincia seleccionada: ' + provincia)
            #return provincia # no necesario
        except Exception as error:
            print("Error al seleccionar la provincia: " + str(error))

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
            cabecera = str(datetime.datetime.now())
            var.dLog.ui.etLog.appendPlainText("[" + cabecera +"] \n   "+ str(msg))
            #var.dLog.setPlainText(QtCore.QCoreApplication.translate("DialogLog", texto))
            # var.dLog.show()
        except Exception as error:
            print("Error en el Log" + str(error))