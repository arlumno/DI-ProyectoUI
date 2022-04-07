from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

import database
import tools
import var


class Informes():

    def configReport():
        var.configReport = {"rutaArchivoPdf" :'informes/listadoclientes.pdf',
                            "tituloInforme": "Listado de Clientes",
                            "autorInforme": "Armando Castro",
                            # "logoEmpresa": ".\\recursos\logo_ies_teis.jpg",
                            "logoEmpresa": "recursos/logo_ies_teis.jpg",
                            "cifEmpresa": "A-12345678",
                            "nombreEmpresa": "Ies de Teis s.l.",
                            "direccionEmpresa": "Avenida Galicia, 101 - 36216 Vigo (Pontevedra)",
                            "telefonoEmpresa": "886 12 04 64"
                            }

    def reportCli():
        try:
            Informes.configReport()
            var.report = canvas.Canvas(var.configReport['rutaArchivoPdf'], pagesize=A4)
            Informes.header()

            var.report.setFont('Helvetica-Bold', size=13)
            var.report.drawString(55,730, var.configReport['tituloInforme'])

            listadoClientes = database.Database.obtenerListadoClientes()

            Informes.body(listadoClientes)

            Informes.footer()

            var.report.save()
            os.startfile(".\\"+var.configReport['rutaArchivoPdf'])

        except Exception as error:
            print('Error reporcli %s ' % str(error))

    def header():
        try:
            var.report.setTitle(var.configReport['tituloInforme'])
            var.report.setAuthor(var.configReport['autorInforme'])
            var.report.setFont('Helvetica', size=10)
            var.report.line(45,820,525,820)
            var.report.line(45,745,525,745)

            var.report.drawString(50,805,var.configReport['cifEmpresa'])
            var.report.drawString(50,790,var.configReport['nombreEmpresa'])
            var.report.drawString(50,775,var.configReport['direccionEmpresa'])
            var.report.drawString(50,760,var.configReport['telefonoEmpresa'])
            var.report.drawImage(var.configReport['logoEmpresa'], 465, 752,60,60)
            Informes.subHeader()

        except Exception as error:
            print('Error reporcli header %s ' % str(error))

    def subHeader():
        var.report.line(45, 722, 525, 722)
        tituloColumnas = ['Código', 'Dni', "Apellidos", "Nombre", "Fecha Alta"]
        var.report.setFont("Helvetica", size=10)
        var.report.drawString(45, 710, tituloColumnas[0])
        var.report.drawString(100, 710, tituloColumnas[1])
        var.report.drawString(185, 710, tituloColumnas[2])
        var.report.drawString(325, 710, tituloColumnas[3])
        var.report.drawString(465, 710, tituloColumnas[4])
        var.report.line(45, 703, 525, 703)

    def body(listadoClientes):
        i = 675
        j = i
        var.report.setFont('Helvetica', size=10)
        for cliente in listadoClientes:
            var.report.drawString(52, j, str(cliente['codigo']))
            var.report.drawString(95, j, str(cliente['dni']))
            var.report.drawString(180, j, str(cliente['apellidos']))
            var.report.drawString(332, j, str(cliente['nombre']))
            var.report.drawRightString(515, j, str(cliente['fecha_alta']))
            j = j - 30
            if j < 70:
                Informes.footer()
                var.report.showPage()
                Informes.header()
                j = i

    def footer():
        try:
            var.report.setFont("Helvetica", size=7)
            var.report.line(50,50,525,50)
            fecha = tools.Tools.fechaActual('%d.%m.%Y %H.%M.%S')
            var.report.drawString(460,40, fecha)
            var.report.drawString(275,40, str('Página %s' % var.report.getPageNumber()))
            var.report.drawString(50,40, var.configReport['tituloInforme'] + "  Autor: " + var.configReport['autorInforme'])

        except Exception as error:
            print('Error reporcli footer %s ' % str(error))