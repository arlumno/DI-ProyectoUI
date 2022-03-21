from PyQt5 import QtWidgets, QtSql

import acciones
import var
class Database():
        def connect():
            var.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            var.db.setDatabaseName(var.fileDb)
            if not var.db.open():
                QtWidgets.QMessageBox.critical(None, "No se puede abrir la base ded datos", 'No se puede establecer conexión.', QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print("Conexión realizada con éxito")
            return True

        def disconnect():
            var.db.close()
            # del var.db
            # QtSql.QSqlDatabase.removeDatabase(var.fileDb)
            print("Base de datos desconectada.")

        def guardarCliente(cliente):
            q = QtSql.QSqlQuery()

            q.prepare("INSERT INTO clientes (dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo)  "
                                "VALUES ( :dni, :apellidos, :nombre, :direccion, :fecha_alta, :provincia, :pago, :sexo)")

            q.bindValue(":dni", str(cliente[0]))
            q.bindValue(":apellidos",  str(cliente[1]))
            q.bindValue(":nombre", str(cliente[2]))
            q.bindValue(":direccion", str(cliente[3]))
            q.bindValue(":fecha_alta",  str(cliente[4]))
            q.bindValue(":provincia", str(cliente[5]))
            q.bindValue(":pago", str(cliente[6]))
            q.bindValue(":sexo",  str(cliente[7]))

            if q.exec_():
                acciones.Acciones.ventanaAdvertencia("El cliente se ha guardado con éxito")
            else:
                print("Error al guardar cliente: ", q.lastError().text())

        def modificarCliente(cliente):
            q = QtSql.QSqlQuery()
            q.prepare(
                "UPDATE clientes "
                "SET apellidos = :apellidos,  nombre = :nombre, direccion = :direccion, provincia = :provincia, fecha_alta = :fecha_alta, forma_pago = :pago, sexo = :sexo "
                "WHERE dni = :dni ")

            q.bindValue(":dni", str(cliente[0]))
            q.bindValue(":apellidos", str(cliente[1]))
            q.bindValue(":nombre", str(cliente[2]))
            q.bindValue(":direccion", str(cliente[3]))
            q.bindValue(":fecha_alta", str(cliente[4]))
            q.bindValue(":provincia", str(cliente[5]))
            q.bindValue(":pago", str(cliente[6]))
            q.bindValue(":sexo", str(cliente[7]))

            if q.exec_():
                acciones.Acciones.ventanaAdvertencia("El cliente se ha modificado con éxito")
            else:
                print("Error al modificar cliente: ", q.lastError().text())

        def cargarCliente(dni):
            q = QtSql.QSqlQuery()
            q.prepare("SELECT dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo FROM clientes WHERE dni = :dni")
            q.bindValue(":dni", str(dni))

            if q.exec_():
                q.next()
                cliente = [q.value(0), q.value(1), q.value(2), q.value(3), q.value(5), q.value(6), q.value(7),q.value(4)]
                acciones.Acciones.cargarCliente(cliente)
            else:
                print("Error al cargar el cliente: ", q.lastError().text())

        def eliminarCliente(dni):
            q = QtSql.QSqlQuery()
            if acciones.Acciones.isClientecargado():
                Database.cargarCliente(dni)
                q.prepare(
                    "DELETE FROM clientes "                
                    "WHERE dni = :dni ")
                q.bindValue(":dni", dni)

                if q.exec_():
                    acciones.Acciones.ventanaAdvertencia("El cliente con dni: " +dni + " se ha eliminado con éxito")
                    # acciones.Acciones.descargarCliente()
                else:
                    print("Error al eliminar cliente: ", q.lastError().text())
            else:
                acciones.Acciones.ventanaAdvertencia("El cliente que se intenta borrar no Existe")

        def cargarClientes():
            q = QtSql.QSqlQuery()
            q.prepare("SELECT dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo FROM clientes")
            var.listadoClientes = []
            if q.exec_():
                while q.next():
                    var.listadoClientes.append([q.value(0),q.value(1),q.value(2),q.value(3),q.value(5),q.value(6),q.value(7),q.value(4)])

            else:
                print("Error al cargar clientes: ", q.lastError().text())

        def cargarProvincias():
            q = QtSql.QSqlQuery()
            q.prepare("SELECT provincia FROM provincias")
            var.listadoProvincias = [""]
            if q.exec_():
                while q.next():
                    var.listadoProvincias.append(q.value(0))
            else:
                print("Error al cargar provincias: ", q.lastError().text())


        def filtrarClientes(filtro):
            q = QtSql.QSqlQuery()

            # q.prepare("SELECT dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo FROM clientes WHERE nombre = :filtro")
            q.prepare("SELECT dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo FROM clientes WHERE nombre LIKE :filtro or apellidos LIKE :filtro")

            q.bindValue(":filtro", "%"+str(filtro) + "%")

            var.listadoClientes = []
            if q.exec_():
                while q.next():
                    var.listadoClientes.append([q.value(0),q.value(1),q.value(2),q.value(3),q.value(5),q.value(6),q.value(7),q.value(4)])
            else:
                print("Error al cargar clientes: ", q.lastError().text())
