
class Grid:

    empty_cell = 0
    bomb_cell = 1
    flag_cell = 2

    def __init__(self, rows, cols, mines) -> None:
        self.rows = rows
        self.cols = cols
        self.mines = mines

    def create_grid(self):
        grid = []
        for _ in range(self.rows):
            grid.append([])
            for k in range(self.cols):
                k.append(self.empty_cell)
        return grid

result = Grid(10, 10, 10)

print(result.create_grid())