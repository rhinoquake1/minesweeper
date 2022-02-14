import random
import numpy as np

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

    def display_grid(self):
        display_rows = [' '.join(map(str, i)) for i in self.grid]
        return '\n'.join(map(str, display_rows))

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f'grid: {self.rows} x {self.cols}\nmines: {self.mine_count}\n{self.display_grid()}'

    def add_mines(self):
        mines_planted = 0
        grid = self.grid
        while mines_planted <= self.mine_count:
            row = random.randint(0, self.rows-1)
            col = random.randint(0, self.cols-1)
            if grid[row][col] != self.mine_cell:
                grid[row][col] = self.mine_cell
                mines_planted += 1
        return result

    def get_adj_mines(self, coord):
        row, col = coord
        adjacent = []
        mine_count = 0
        for col_offset in range(-1, 2, 1):
            col_final = col+col_offset
            if col_final > 0 and col_final < self.cols:
                for row_offset in range(-1, 2, 1):
                    row_final = row+row_offset
                    if row_final > 0 and row_final < self.rows:
                        adjacent.append(self.grid[row_final][col_final])
                        if self.grid[row_final][col_final].is_mine:
                            mine_count += 1
        return mine_count

    def get_adj_mines2(self, coord):
        offset = np.array([-1, 0 , 1])
        row, col = coord
        rows = row + offset
        cols = col + offset
        valid_rows = offset[(offset>=0) & (offset<=self.rows)]        
        valid_cols = offset[(offset>=0) & (offset<=self.cols)]

    
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

print(result)

print(result.get_adj_mines2((2,2)))