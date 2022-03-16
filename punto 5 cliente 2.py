import funciones
import random 
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
class Mago:
    def __init__(self,x):
        self.nombre = x
        self.objetivos_completados= []
        self.objetivo = input("")
        self.fila = 0
        self.columna = 0
        self.numero_caidas = 0
        self.espacios_avanzados = 0
        print("nuevo objetivo de ", self.nombre,": ",self.objetivo)
        
    def __str__(self):
        res = "jugador "+ self.nombre + " | puntaje: "+ str(len(self.objetivos_completados)) + " objetivo: "+self.objetivo+" | caidas: "+ str(self.numero_caidas)+" pasos: "+ str(self.espacios_avanzados)
        return res
    def sacar_nuevo_objetivo(self):
        if(self.objetivo != " "):
            print(self.nombre," ha llegado a su objetivo: ",self.objetivo)
            self.objetivos_completados.append(self.objetivo)
            print("ha recolectado ", str(len(self.objetivos_completados))," en total")
        ob = input("")
        self.objetivo = ob
        print("nuevo objetivo de ", self.nombre,": ",self.objetivo)
        
    
    def jugar_turno(self):
        mov = random.randint(1, 6)
        movimientos = []
        for i in range(mov):
            move = input("")
            movimientos.append(move)
            if(move == "derecha"):
               break 
        return movimientos


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
    def mover_jugador(self,jugador,movimiento):
        if(movimiento == "abajo"):
            if(jugador.fila + 1 > self.alto-1):
                return "fuera"
            elif(self.nivel_superior[jugador.fila + 1][jugador.columna].n_jugadores > 0):
                return "espacio ocupado"
            elif(self.nivel_inferior[jugador.fila][jugador.columna].abajo):
                jugador.columna = 0
                jugador.fila = 0
                return "pared"
            elif(self.nivel_superior[jugador.fila + 1][jugador.columna].objetivo == jugador.objetivo):
                jugador.sacar_nuevo_objetivo()
                return "movimiento exitoso"
            else:
                jugador.fila = jugador.fila + 1
                return "movimiento exitoso"
        if(movimiento == "arriba"):
            if(jugador.fila -1 > self.alto-1):
                return "fuera"
            elif(self.nivel_superior[jugador.fila + -1][jugador.columna].n_jugadores > 0):
                return "espacio ocupado"
            elif(self.nivel_inferior[jugador.fila][jugador.columna].arriba):
                jugador.columna = 0
                jugador.fila = 0
                return "pared"
            elif(self.nivel_superior[jugador.fila + -1][jugador.columna].objetivo == jugador.objetivo):
                jugador.sacar_nuevo_objetivo()
                return "movimiento exitoso"
            else:
                jugador.fila = jugador.fila + -1
                return "movimiento exitoso"
        if(movimiento == "derecha"):
            if(jugador.columna - 1 > self.ancho-1):
                return "fuera"
            elif(self.nivel_superior[jugador.fila][jugador.columna-1].n_jugadores > 0):
                return "espacio ocupado"
            elif(self.nivel_inferior[jugador.fila][jugador.columna].derecha):
                jugador.columna = 0
                jugador.fila = 0
                return "pared"
            elif(self.nivel_superior[jugador.fila][jugador.columna-1].objetivo == jugador.objetivo):
                jugador.sacar_nuevo_objetivo()
                return "movimiento exitoso"
            else:
                jugador.columna = jugador.columna + 1
                return "movimiento exitoso"
        if(movimiento == "izquierda"):
            if(jugador.columna + 1 > self.ancho-1):
                return "fuera"
            elif(self.nivel_superior[jugador.fila][jugador.columna+1].n_jugadores > 0):
                return "espacio ocupado"
            elif(self.nivel_inferior[jugador.fila][jugador.columna].izquierda):
                jugador.columna = 0
                jugador.fila = 0
                return "pared"
            elif(self.nivel_superior[jugador.fila][jugador.columna+1].objetivo == jugador.objetivo):
                jugador.sacar_nuevo_objetivo()
                return "movimiento exitoso"
            else:
                jugador.columna = jugador.columna - 1
                return "movimiento exitoso"
        

ancho = int(input())
alto = int(input())
tablero = Tablero(ancho,alto)
tablero.cargar_tablero()
nombre_mago = input()

jugador = Mago(nombre_mago)

tablero.nivel_superior[0][0].n_jugadores = 1

jugadas = jugador.jugar_turno()
for jugada in jugadas:
    print(tablero.mover_jugador(jugador,jugada))
    funciones.imprimir_tablero_mago(tablero,jugador)
