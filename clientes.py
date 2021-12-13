class Clientes:
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


