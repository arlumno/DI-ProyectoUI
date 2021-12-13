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
            print("Error: " + error)

    def salir():
        try:
            var.dSalir.show()
            if var.dSalir.exec():
                sys.exit()
            else:
                var.dSalir.hide()
        except Exception as error:
            print("error s%:" % str(error))