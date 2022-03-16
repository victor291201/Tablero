import funciones

class CeldaInferior:
    def __init__(self):
        self.arriba = False
        self.abajo = False
        self.derecha = False
        self.izquierda = False
    def __str__(self):
        ret = "Pared arriba: " + str(self.arriba)+"\n"+"Pared abajo: " + str(self.abajo)+"\n"+"Pared derecha: " + str(self.derecha)+"\n"+"Pared izquierda: " + str(self.izquierda)
        return ret

    def poner_paredes(self,x):
        if(x.rstrip('\n') == "abajo"):
            self.abajo = True
        if(x.rstrip('\n') == "arriba"):
            self.arriba = True
        if(x.rstrip('\n') == "derecha"):
            self.derecha = True
        if(x.rstrip('\n') == "izquierda"):
            self.izquierda = True
                
class CeldaSuperior:
    def __init__(self,x):
        self.n_jugadores = 0
        self.objetivo = x
    def __str__(self):
        ret = "esta celda contiene al objetivo {"+self.objetivo+"}"
        if(self.n_jugadores > 0):
            ret += " y esta ocupada por {"+str(self.n_jugadores)+"} jugador(es)"
        return ret


class Tablero:
    def __init__(self, x, y):
        self.ancho = x
        self.alto = y
        self.nivel_superior = []
        self.nivel_inferior = []
        
    def cargar_tablero(self):
        for i in range(self.alto):
            vari = []
            vars = []
            for e in range(self.ancho):
                vars.append(CeldaSuperior(" "))
                vari.append(CeldaInferior())
            self.nivel_inferior.append(vari)
            self.nivel_superior.append(vars)
        inf = open("tablero_inferior.txt","r")
        sup = open("tablero_superior.txt","r")
        for i in sup.readlines():
                var = i.split(" ")
                self.nivel_superior[int(var[0])][int(var[1])]= CeldaSuperior(var[2].rstrip('\n'))
        for i in inf.readlines():
            var = i.split(",")
            for f in var[2].split(";"):
                self.nivel_inferior[int(var[0])][int(var[1])].poner_paredes(f)
            
    

ancho = int(input(""))
alto = int(input(""))
tablero = Tablero(ancho,alto)
tablero.cargar_tablero()
print(funciones.representacion_tablero(tablero))
