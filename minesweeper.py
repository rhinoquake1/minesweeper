import random

class GridCell:
    def __init__(self, name, repr, is_mine, is_empty, is_flag) -> None:
        self.name = name
        self.repr = repr
        self.is_mine = is_mine
        self.is_empty = is_empty
        self.is_flag = is_flag

    def __repr__(self) -> str:
        return str(self.repr)

    def __str__(self) -> str:
        return str(self.repr)

class Grid:

    empty_cell = GridCell('empty', '0', False, True, False)
    mine_cell = GridCell('mine', '*', True, False, False)
    flag_cell = GridCell('flag', 'F', False, False, True)

    def __init__(self, rows, cols, mine_count) -> None:
        self.rows = rows
        self.cols = cols
        self.mine_count = mine_count
        self.grid = self.create_grid()

    def create_grid(self):
        # single line imp
        # creates nested lists to represent the columns and rows of the grid
        grid = [[self.empty_cell for _ in range(self.rows)] for _ in range(self.cols)]
        return grid

    def add_mines(self):
        mines_planted = 0
        grid = self.grid
        row = random.randint(0, self.rows-1)
        col = random.randint(0, self.cols-1)
        grid[row][col] = self.mine_cell
        return result

    
        # multi line implementation of create grid - not used
    def create_grid_legacy(self):
        grid = []
        for _ in range(self.rows):
            grid.append([])
        for _ in range(self.cols):
            for i in grid:
                i.append(None)
        return grid

result = Grid(10, 10, 10)

result.add_mines()

print(result.grid)