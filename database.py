from PyQt5 import QtWidgets, QtSql

class Database():
        def connect(fileDb):
            db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName(fileDb)
            if not db.open():
                QtWidgets.QMessageBox.critical(None, "No se puede abrir la base ded datos", 'No se puede establecer conexión.', QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print("Conexión realizada con éxito")
            return True

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
                print("El cliente se ha guardado con éxito")
            else:
                print("Error al guardar cliente: ", q.lastError().text())

        def cargarClientes():
            index = 0
            q = QtSql.QSqlQuery()
            q.prepare("SELECT dni, apellidos, nombre, direccion, fecha_alta, provincia, forma_pago, sexo FROM clientes")
            listado = []
            if q.exec_():
                while q.next():
                    listado = [q.value(0),q.value(1),q.value(2),q.value(3),q.value(4),q.value(5),q.value(6),q.value(7)]
                    print(listado)

            else:
                print("Error al cargar clientes: ", q.lastError().text())
