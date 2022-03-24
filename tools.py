from datetime import datetime

from PyQt5.QtWidgets import QMessageBox


class Tools():
    def fechaActual(format= "%d/%m/%Y"):
        fecha = datetime.today()
        fecha = fecha.strftime(format)
        return str(fecha)

    def ventanaAdvertencia(mensaje = "", titulo="Atención", descripcion=""):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        # msg.setInformativeText("This is additional information")
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
        msg.setDetailedText(descripcion)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

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

    def validarDni(dni):
        resultado= False
        if len(dni) == 9:
            letra = dni[-1]
            numeros = dni[0:8]
            if numeros.isdigit():
                letrasDni= 'TRWAGMYFPDXBNJZSQVHLCKE';
                indiceLetra = int(numeros)%23
                if letrasDni[indiceLetra] == letra.upper():
                    resultado= True
        return resultado

    def formatearDni(dni):
        dni = dni.upper()
        if len(dni) > 9:
            dni = dni.replace("-","")
            dni = dni.replace(" ", "")
        return dni
