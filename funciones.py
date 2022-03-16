
from itertools import product


class Drawing:
    def __init__(self, x: int = 6, y: int = 6):
        self.data = [[" " for _ in range(x * 5)] for _ in range(y * 2 + 1)]
        self.x = x
        self.y = y
        self.draw_interior()
        self.draw_contour()

    def __str__(self) -> str:
        return "\n".join("".join(e) for e in self.data)

    def draw_interior(self):
        for p, i, s in product(range(2), range(self.x - 1), range(2)):
            self.data[-p][4 + 5 * i + s] = "╧" if p == 1 else "╤"
        for p, i, s in product(range(2), range(self.y - 1), range(2)):
            self.data[2 + 2 * i][-p] = "╣" if p == 1 else "╠"
        for p, i, s in product(range(self.y - 1), range(self.x), range(2)):
            self.data[2 + 2 * p][1 + 5 * i + 2 * s] = "═"
        for p, i, s in product(range(self.y - 1), range(self.x - 1), range(2)):
            self.data[2 + 2 * p][4 + 5 * i + s] = "╪"

    def draw_contour(self):
        for p, i in product(range(2), range(self.y)):
            self.data[1 + 2 * i][-p] = "║"
        for p, i, s in product(range(2), range(self.x), range(3)):
            self.data[-p][1 + 5 * i + s] = "═"
        for i, e in enumerate(["╔", "╗", "╚", "╝"]):
            self.data[-1 * int(i > 1)][-1 * (i % 2)] = e

    def draw_upper_cells(self, cells):
        for y, row in enumerate(cells):
            for x, cell in enumerate(row):
                self.data[1 + 2 * y][2 + 5 * x] = str(cell.objetivo).lower()

    def draw_players(self, players):
        assert len(players) == 2
        for i, p in enumerate(players):
            self.data[1 + 2 * p.fila][1 + i * 2 +
                                      5 * p.columna] = p.nombre[0].upper()

    def draw_player(self, player):
        for i, p in enumerate(player):
            self.data[1 + 2 * p.fila][1 + i * 2 +
                                      5 * p.columna] = p.nombre[0].upper()

    def draw_lower_cells(self, cells):
        for y, row in enumerate(cells):
            for x, cell in enumerate(row):
                # Lados
                if cell.izquierda:
                    self.data[1 + 2 * y][5 * x] = "│"
                if cell.derecha:
                    self.data[1 + 2 * y][4 + 5 * x] = "│"
                # superior inferior
                if y + 1 < self.y:
                    a = cells[y][x].abajo
                    b = cells[y + 1][x].arriba
                    if a or b:
                        wall_repr = "═" if a and b else "?"
                        self.data[2 + 2 * y][2 + 5 * x] = wall_repr

    def draw_game(self, game, *, show_hidden=False):
        self.draw_players(game.magos)
        self.draw_upper_cells(game.tablero.nivel_superior)
        if show_hidden:
            self.draw_lower_cells(game.tablero.nivel_inferior)

    def draw_board(self, board, show_hidden=False):
        self.draw_upper_cells(board.nivel_superior)
        if show_hidden:
            self.draw_lower_cells(board.nivel_inferior)


def representacion_tablero(tablero):
    drawing = Drawing(
        len(tablero.nivel_superior[0]), len(tablero.nivel_superior))
    drawing.draw_board(tablero, show_hidden=True)
    return str(drawing)


def imprimir_tablero_mago(tablero, mago):
    drawing = Drawing(
        len(tablero.nivel_superior[0]), len(tablero.nivel_superior))
    drawing.draw_board(tablero, show_hidden=True)
    drawing.draw_player([mago])

    print(drawing)


def imprimir_juego(juego):
    x = len(juego.tablero.nivel_superior[0])
    y = len(juego.tablero.nivel_superior)
    drawing = Drawing(x, y)
    drawing.draw_game(juego, show_hidden=True)
    print(drawing)
