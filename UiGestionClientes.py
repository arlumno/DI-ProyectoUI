# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiGestionClientes.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 730)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(900, 730))
        MainWindow.setMaximumSize(QtCore.QSize(900, 730))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 881, 651))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setToolTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.tabClientes = QtWidgets.QWidget()
        self.tabClientes.setObjectName("tabClientes")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tabClientes)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(69, 151, 146, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.LayoutSexo = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.LayoutSexo.setContentsMargins(0, 0, 0, 0)
        self.LayoutSexo.setObjectName("LayoutSexo")
        self.rbFemenino = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbFemenino.setObjectName("rbFemenino")
        self.rbgSexo = QtWidgets.QButtonGroup(MainWindow)
        self.rbgSexo.setObjectName("rbgSexo")
        self.rbgSexo.addButton(self.rbFemenino)
        self.LayoutSexo.addWidget(self.rbFemenino)
        self.rbMasculino = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbMasculino.setObjectName("rbMasculino")
        self.rbgSexo.addButton(self.rbMasculino)
        self.LayoutSexo.addWidget(self.rbMasculino)
        self.etDni = QtWidgets.QLineEdit(self.tabClientes)
        self.etDni.setGeometry(QtCore.QRect(60, 90, 113, 20))
        self.etDni.setText("")
        self.etDni.setObjectName("etDni")
        self.label_9 = QtWidgets.QLabel(self.tabClientes)
        self.label_9.setGeometry(QtCore.QRect(610, 126, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.bSalir = QtWidgets.QPushButton(self.tabClientes)
        self.bSalir.setGeometry(QtCore.QRect(767, 585, 80, 31))
        self.bSalir.setObjectName("bSalir")
        self.label_5 = QtWidgets.QLabel(self.tabClientes)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 40, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.tabClientes)
        self.label_7.setGeometry(QtCore.QRect(29, 126, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(self.tabClientes)
        self.line_2.setGeometry(QtCore.QRect(20, 224, 841, 30))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.tabClientes)
        self.label_2.setGeometry(QtCore.QRect(220, 92, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.tabClientes)
        self.label_6.setGeometry(QtCore.QRect(546, 158, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.etNombre = QtWidgets.QLineEdit(self.tabClientes)
        self.etNombre.setGeometry(QtCore.QRect(630, 90, 211, 20))
        self.etNombre.setObjectName("etNombre")
        self.cbProvincia = QtWidgets.QComboBox(self.tabClientes)
        self.cbProvincia.setGeometry(QtCore.QRect(423, 124, 161, 20))
        self.cbProvincia.setObjectName("cbProvincia")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tabClientes)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(633, 151, 223, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.LayoutMetodosPago = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.LayoutMetodosPago.setContentsMargins(0, 0, 0, 0)
        self.LayoutMetodosPago.setObjectName("LayoutMetodosPago")
        self.chkEfectivo = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.chkEfectivo.setObjectName("chkEfectivo")
        self.LayoutMetodosPago.addWidget(self.chkEfectivo)
        self.chkTarjeta = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.chkTarjeta.setObjectName("chkTarjeta")
        self.LayoutMetodosPago.addWidget(self.chkTarjeta)
        self.chkTransfer = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.chkTransfer.setObjectName("chkTransfer")
        self.LayoutMetodosPago.addWidget(self.chkTransfer)
        self.etDireccion = QtWidgets.QLineEdit(self.tabClientes)
        self.etDireccion.setGeometry(QtCore.QRect(90, 124, 251, 20))
        self.etDireccion.setObjectName("etDireccion")
        self.bAceptar = QtWidgets.QPushButton(self.tabClientes)
        self.bAceptar.setGeometry(QtCore.QRect(677, 585, 81, 31))
        self.bAceptar.setObjectName("bAceptar")
        self.flagDni = QtWidgets.QLabel(self.tabClientes)
        self.flagDni.setGeometry(QtCore.QRect(178, 91, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setKerning(False)
        self.flagDni.setFont(font)
        self.flagDni.setText("")
        self.flagDni.setObjectName("flagDni")
        self.label_3 = QtWidgets.QLabel(self.tabClientes)
        self.label_3.setGeometry(QtCore.QRect(570, 92, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tabClientes)
        self.label.setGeometry(QtCore.QRect(30, 92, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.bCalendar = QtWidgets.QPushButton(self.tabClientes)
        self.bCalendar.setGeometry(QtCore.QRect(810, 118, 31, 31))
        self.bCalendar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/recursos/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCalendar.setIcon(icon)
        self.bCalendar.setIconSize(QtCore.QSize(30, 30))
        self.bCalendar.setObjectName("bCalendar")
        self.etFechaAlta = QtWidgets.QLineEdit(self.tabClientes)
        self.etFechaAlta.setGeometry(QtCore.QRect(700, 124, 101, 20))
        self.etFechaAlta.setText("")
        self.etFechaAlta.setObjectName("etFechaAlta")
        self.etApellido = QtWidgets.QLineEdit(self.tabClientes)
        self.etApellido.setGeometry(QtCore.QRect(280, 90, 251, 20))
        self.etApellido.setObjectName("etApellido")
        self.label_4 = QtWidgets.QLabel(self.tabClientes)
        self.label_4.setGeometry(QtCore.QRect(240, 6, 361, 51))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.tabClientes)
        self.line.setGeometry(QtCore.QRect(20, 60, 841, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_8 = QtWidgets.QLabel(self.tabClientes)
        self.label_8.setGeometry(QtCore.QRect(360, 126, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.tablaDatos = QtWidgets.QTableWidget(self.tabClientes)
        self.tablaDatos.setGeometry(QtCore.QRect(10, 290, 851, 281))
        self.tablaDatos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablaDatos.setObjectName("tablaDatos")
        self.tablaDatos.setColumnCount(8)
        self.tablaDatos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDatos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDatos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDatos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDatos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDatos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDatos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDatos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaDatos.setHorizontalHeaderItem(7, item)
        self.bFiltrarClientes = QtWidgets.QPushButton(self.tabClientes)
        self.bFiltrarClientes.setGeometry(QtCore.QRect(820, 248, 29, 31))
        self.bFiltrarClientes.setToolTip("")
        self.bFiltrarClientes.setToolTipDuration(10)
        self.bFiltrarClientes.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconos/recursos/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bFiltrarClientes.setIcon(icon1)
        self.bFiltrarClientes.setIconSize(QtCore.QSize(30, 30))
        self.bFiltrarClientes.setObjectName("bFiltrarClientes")
        self.etFiltro = QtWidgets.QLineEdit(self.tabClientes)
        self.etFiltro.setGeometry(QtCore.QRect(650, 258, 161, 20))
        self.etFiltro.setObjectName("etFiltro")
        self.bCargarClientes = QtWidgets.QPushButton(self.tabClientes)
        self.bCargarClientes.setGeometry(QtCore.QRect(30, 248, 31, 31))
        self.bCargarClientes.setToolTip("")
        self.bCargarClientes.setToolTipDuration(10)
        self.bCargarClientes.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconos/recursos/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCargarClientes.setIcon(icon2)
        self.bCargarClientes.setIconSize(QtCore.QSize(30, 30))
        self.bCargarClientes.setObjectName("bCargarClientes")
        self.bNuevoCliente = QtWidgets.QPushButton(self.tabClientes)
        self.bNuevoCliente.setGeometry(QtCore.QRect(720, 192, 80, 31))
        self.bNuevoCliente.setStyleSheet("background-color: rgb(0, 190, 0);\n"
"color: white;\n"
"font-weight: bold")
        self.bNuevoCliente.setObjectName("bNuevoCliente")
        self.bModificarCliente = QtWidgets.QPushButton(self.tabClientes)
        self.bModificarCliente.setGeometry(QtCore.QRect(110, 248, 81, 31))
        self.bModificarCliente.setStyleSheet("")
        self.bModificarCliente.setObjectName("bModificarCliente")
        self.bEliminarCliente = QtWidgets.QPushButton(self.tabClientes)
        self.bEliminarCliente.setGeometry(QtCore.QRect(30, 192, 81, 31))
        self.bEliminarCliente.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: white;\n"
"font-weight: bold")
        self.bEliminarCliente.setObjectName("bEliminarCliente")
        self.bLimpiarClientes = QtWidgets.QPushButton(self.tabClientes)
        self.bLimpiarClientes.setGeometry(QtCore.QRect(70, 248, 31, 31))
        self.bLimpiarClientes.setToolTipDuration(1)
        self.bLimpiarClientes.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconos/recursos/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bLimpiarClientes.setIcon(icon3)
        self.bLimpiarClientes.setIconSize(QtCore.QSize(30, 30))
        self.bLimpiarClientes.setObjectName("bLimpiarClientes")
        self.label_10 = QtWidgets.QLabel(self.tabClientes)
        self.label_10.setGeometry(QtCore.QRect(480, 258, 171, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.bLimpiarCampos = QtWidgets.QPushButton(self.tabClientes)
        self.bLimpiarCampos.setGeometry(QtCore.QRect(810, 192, 31, 30))
        self.bLimpiarCampos.setToolTipDuration(1)
        self.bLimpiarCampos.setText("")
        self.bLimpiarCampos.setIcon(icon3)
        self.bLimpiarCampos.setIconSize(QtCore.QSize(30, 30))
        self.bLimpiarCampos.setObjectName("bLimpiarCampos")
        self.label_11 = QtWidgets.QLabel(self.tabClientes)
        self.label_11.setGeometry(QtCore.QRect(20, 580, 501, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.bEliminarClienteSeleccionado = QtWidgets.QPushButton(self.tabClientes)
        self.bEliminarClienteSeleccionado.setGeometry(QtCore.QRect(200, 248, 141, 31))
        self.bEliminarClienteSeleccionado.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: white;\n"
"font-weight: bold")
        self.bEliminarClienteSeleccionado.setObjectName("bEliminarClienteSeleccionado")
        self.bGuardarCambios = QtWidgets.QPushButton(self.tabClientes)
        self.bGuardarCambios.setGeometry(QtCore.QRect(120, 192, 110, 31))
        self.bGuardarCambios.setStyleSheet("")
        self.bGuardarCambios.setObjectName("bGuardarCambios")
        self.sbEnvio = QtWidgets.QSpinBox(self.tabClientes)
        self.sbEnvio.setGeometry(QtCore.QRect(264, 155, 31, 22))
        self.sbEnvio.setObjectName("sbEnvio")
        self.label_12 = QtWidgets.QLabel(self.tabClientes)
        self.label_12.setGeometry(QtCore.QRect(225, 158, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.etEnvio = QtWidgets.QLineEdit(self.tabClientes)
        self.etEnvio.setGeometry(QtCore.QRect(300, 155, 221, 21))
        self.etEnvio.setText("")
        self.etEnvio.setAlignment(QtCore.Qt.AlignCenter)
        self.etEnvio.setReadOnly(True)
        self.etEnvio.setObjectName("etEnvio")
        self.tabWidget.addTab(self.tabClientes, "")
        self.tabFacturacion = QtWidgets.QWidget()
        self.tabFacturacion.setObjectName("tabFacturacion")
        self.tabWidget.addTab(self.tabFacturacion, "")
        self.tabProductos = QtWidgets.QWidget()
        self.tabProductos.setObjectName("tabProductos")
        self.tabWidget.addTab(self.tabProductos, "")
        self.lbStatus = QtWidgets.QLabel(self.centralwidget)
        self.lbStatus.setGeometry(QtCore.QRect(10, 630, 61, 21))
        self.lbStatus.setObjectName("lbStatus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHerramientas = QtWidgets.QMenu(self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        self.menuInformes = QtWidgets.QMenu(self.menubar)
        self.menuInformes.setObjectName("menuInformes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/iconos/recursos/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon4)
        self.actionSalir.setObjectName("actionSalir")
        self.actionLog = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/iconos/recursos/log.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLog.setIcon(icon5)
        self.actionLog.setObjectName("actionLog")
        self.actionAbrirCarpeta = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/iconos/recursos/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbrirCarpeta.setIcon(icon6)
        self.actionAbrirCarpeta.setObjectName("actionAbrirCarpeta")
        self.actionDescargarBd = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/iconos/recursos/Download Database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDescargarBd.setIcon(icon7)
        self.actionDescargarBd.setObjectName("actionDescargarBd")
        self.actionImportar_Datos = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("recursos/New Database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImportar_Datos.setIcon(icon8)
        self.actionImportar_Datos.setObjectName("actionImportar_Datos")
        self.actionRestaurarBD = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/iconos/recursos/Misc_Upload_Database_Icon_256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRestaurarBD.setIcon(icon9)
        self.actionRestaurarBD.setObjectName("actionRestaurarBD")
        self.actionBorrarBD = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/iconos/recursos/Remove_from_database_Icon_256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBorrarBD.setIcon(icon10)
        self.actionBorrarBD.setObjectName("actionBorrarBD")
        self.actionGenerarInformeClientes = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/iconos/recursos/read.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGenerarInformeClientes.setIcon(icon11)
        self.actionGenerarInformeClientes.setObjectName("actionGenerarInformeClientes")
        self.menuArchivo.addAction(self.actionAbrirCarpeta)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuArchivo.addAction(self.actionLog)
        self.menuHerramientas.addAction(self.actionImportar_Datos)
        self.menuHerramientas.addSeparator()
        self.menuHerramientas.addAction(self.actionDescargarBd)
        self.menuHerramientas.addAction(self.actionRestaurarBD)
        self.menuHerramientas.addSeparator()
        self.menuHerramientas.addAction(self.actionBorrarBD)
        self.menuInformes.addAction(self.actionGenerarInformeClientes)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuInformes.menuAction())
        self.toolBar.addAction(self.actionAbrirCarpeta)
        self.toolBar.addAction(self.actionSalir)
        self.toolBar.addAction(self.actionLog)
        self.toolBar.addAction(self.actionDescargarBd)
        self.toolBar.addAction(self.actionGenerarInformeClientes)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.etDni, self.etApellido)
        MainWindow.setTabOrder(self.etApellido, self.etNombre)
        MainWindow.setTabOrder(self.etNombre, self.etDireccion)
        MainWindow.setTabOrder(self.etDireccion, self.cbProvincia)
        MainWindow.setTabOrder(self.cbProvincia, self.etFechaAlta)
        MainWindow.setTabOrder(self.etFechaAlta, self.bCalendar)
        MainWindow.setTabOrder(self.bCalendar, self.rbFemenino)
        MainWindow.setTabOrder(self.rbFemenino, self.rbMasculino)
        MainWindow.setTabOrder(self.rbMasculino, self.chkEfectivo)
        MainWindow.setTabOrder(self.chkEfectivo, self.chkTarjeta)
        MainWindow.setTabOrder(self.chkTarjeta, self.chkTransfer)
        MainWindow.setTabOrder(self.chkTransfer, self.bEliminarCliente)
        MainWindow.setTabOrder(self.bEliminarCliente, self.bGuardarCambios)
        MainWindow.setTabOrder(self.bGuardarCambios, self.bNuevoCliente)
        MainWindow.setTabOrder(self.bNuevoCliente, self.bLimpiarCampos)
        MainWindow.setTabOrder(self.bLimpiarCampos, self.bCargarClientes)
        MainWindow.setTabOrder(self.bCargarClientes, self.bLimpiarClientes)
        MainWindow.setTabOrder(self.bLimpiarClientes, self.bModificarCliente)
        MainWindow.setTabOrder(self.bModificarCliente, self.bEliminarClienteSeleccionado)
        MainWindow.setTabOrder(self.bEliminarClienteSeleccionado, self.etFiltro)
        MainWindow.setTabOrder(self.etFiltro, self.bFiltrarClientes)
        MainWindow.setTabOrder(self.bFiltrarClientes, self.tablaDatos)
        MainWindow.setTabOrder(self.tablaDatos, self.bAceptar)
        MainWindow.setTabOrder(self.bAceptar, self.bSalir)
        MainWindow.setTabOrder(self.bSalir, self.tabWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestion de Clientes"))
        self.rbFemenino.setText(_translate("MainWindow", "Femenino"))
        self.rbMasculino.setText(_translate("MainWindow", "Masculino"))
        self.label_9.setText(_translate("MainWindow", "Fecha de Alta:"))
        self.bSalir.setText(_translate("MainWindow", "Salir"))
        self.label_5.setText(_translate("MainWindow", "Sexo:"))
        self.label_7.setText(_translate("MainWindow", "Dirección:"))
        self.label_2.setText(_translate("MainWindow", "Apellidos:"))
        self.label_6.setText(_translate("MainWindow", "Metodos Pago:"))
        self.chkEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.chkTarjeta.setText(_translate("MainWindow", "Tarjeta"))
        self.chkTransfer.setText(_translate("MainWindow", "Transferencia"))
        self.bAceptar.setText(_translate("MainWindow", "Aceptar"))
        self.label_3.setText(_translate("MainWindow", "Nombre:"))
        self.label.setText(_translate("MainWindow", "DNI:"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">GESTION CLIENTES</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Provincia:"))
        item = self.tablaDatos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.tablaDatos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.tablaDatos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tablaDatos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dirección"))
        item = self.tablaDatos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Provincia"))
        item = self.tablaDatos.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "F.Pago"))
        item = self.tablaDatos.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sexo"))
        item = self.tablaDatos.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "FechaAlta"))
        self.bNuevoCliente.setText(_translate("MainWindow", "Nuevo"))
        self.bModificarCliente.setText(_translate("MainWindow", "Modificar"))
        self.bEliminarCliente.setText(_translate("MainWindow", "Eliminar"))
        self.label_10.setText(_translate("MainWindow", "Filtar por nombre o apellidos:"))
        self.label_11.setText(_translate("MainWindow", "*Doble click en una fila para seleccionar el cliente"))
        self.bEliminarClienteSeleccionado.setText(_translate("MainWindow", "Eliminar Seleccionado"))
        self.bGuardarCambios.setText(_translate("MainWindow", "Guardar Cambios"))
        self.label_12.setText(_translate("MainWindow", "Envío:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabClientes), _translate("MainWindow", "Clientes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFacturacion), _translate("MainWindow", "Facturación"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProductos), _translate("MainWindow", "Productos"))
        self.lbStatus.setText(_translate("MainWindow", "TextLabel"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuHerramientas.setTitle(_translate("MainWindow", "Herramientas"))
        self.menuInformes.setTitle(_translate("MainWindow", "Informes"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setToolTip(_translate("MainWindow", "<html><head/><body><p>Exit</p></body></html>"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionLog.setText(_translate("MainWindow", "Ver Log"))
        self.actionLog.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionAbrirCarpeta.setText(_translate("MainWindow", "Abrir"))
        self.actionAbrirCarpeta.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionDescargarBd.setText(_translate("MainWindow", "Descargar Bd"))
        self.actionDescargarBd.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionImportar_Datos.setText(_translate("MainWindow", "Importar Datos"))
        self.actionRestaurarBD.setText(_translate("MainWindow", "Restaurar BD"))
        self.actionRestaurarBD.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionBorrarBD.setText(_translate("MainWindow", "Borrar Clientes BD"))
        self.actionGenerarInformeClientes.setText(_translate("MainWindow", "Generar Informe Clientes"))
import iconos_rc
