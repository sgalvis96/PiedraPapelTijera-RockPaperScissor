import random
class game:

###################################################
    def computadora():
        for i in range(1):
            compu = random.randint(0,2)
        return compu
##################################################
    def seleccion():
        print("Bienvendo a pieda papel o tijera: ")
        try:
            usuario = 8
            while usuario < 0 or usuario > 2:
                usuario = int(input("Seleccione:\n 0 - Piedra\n 1 - Papel\n 2 - Tijera: "))
        except ValueError:
            print("Error sintaxis")
        return usuario
##################################################
    def pelea(yo,pc):
        if yo == 0:
            if pc == 1:
                    resp = ("PERDISTE")
            elif pc == 2:
                    resp = ("GANASTE")
        if yo == 1:
            if pc == 2:
                    resp = ("PERDISTE")
            elif pc == 0:
                    resp = ("GANASTE")
        if yo == 2:
            if pc == 1:
                    resp = ("PERDISTE")
            elif pc == 0:
                    resp = ("GANASTE")

        return resp
###################################################
    user = 0
    compu = 0
    while user == compu:
        compu = computadora()
        user = seleccion()
    if user == compu:
        print = ("EMPATE")
    resultado= (pelea(user,compu))
    print(resultado)
