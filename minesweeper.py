import random
from typing import Tuple
import numpy as np

class GridCell:
    '''
    Usage
    -
    '''
    empty_cell = ' '
    mine_cell = '*'
    flag_cell = 'F'

    def __init__(self, coord : Tuple) -> None:
        # initlal GridCell is set to be 'empty'
        self.coord = coord
        self.name = 'empty'
        self.repr = self.empty_cell
        self.is_mine = False
        self.is_empty = True
        self.is_flag = False
        self.adj_mines = 0
        self.has_adj_mines = True
        self.adj_empty = 0
        self.all_adj_cells_empty = True
        self.is_revealed = False

    def __repr__(self) -> str:
        return f'[{self.repr}]'

    def __str__(self) -> str:
        return str(self.__repr__())

    def convert_to_mine(self):
        self.name = 'mine'
        self.repr = self.mine_cell
        self.is_mine = True
        self.is_empty = False

    def add_flag(self):
        self.is_flag = True

    def remove_flag(self):
        self.is_flag = False

    def reveal_empty_cell(self):
        self.is_revealed = True

class Grid:
    offset_3 = np.array([-1, 0 , 1])
    offset_5 = np.array([-2, -1, 0 , 1, 2])

    def __init__(self, rows, cols, mine_count) -> None:
        self.rows = rows
        self.cols = cols
        self.mine_count = mine_count
        self.grid = self.create_grid()

    def create_grid(self):
        # creates nested lists to represent the columns and rows of the grid.
        # A GridCell class instance is created per cell, and is initially set to empty
        grid = [[GridCell((j, i)) for i in range(self.rows)] for j in range(self.cols)]
        return grid

    def display_grid(self):
        # The data is in a nested list format
        # This stacks the lists on top of each other to get a grid
        display_rows = [' '.join(map(str, i)) for i in self.grid]
        return '\n'.join(map(str, display_rows))

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f'grid: {self.rows} x {self.cols}\nmines: {self.mine_count}\n{self.display_grid()}'

    def add_mines(self):
        # the below loop is checking if the randomly chosen cell is a mine
        # is not, it will run the convert_to_mine method and increment the mine counter
        mines_planted = 0
        grid = self.grid
        while mines_planted <= self.mine_count:
            row = random.randint(0, self.rows-1)
            col = random.randint(0, self.cols-1)
            if not grid[row][col].is_mine:
                grid[row][col].convert_to_mine()
                mines_planted += 1
        return grid

    def get_adj_cells(self, coord, offset):
        row, col = coord
        # the below is using np vectorization to take the offset grid and move it to the coordinates provided
        rows = row + offset
        cols = col + offset
        # We need to remove the out of bounds coords
        valid_rows = rows[(rows>=0) & (rows<self.rows)]        
        valid_cols = cols[(cols>=0) & (cols<self.cols)]
        adj_cells = []
        for i in valid_rows:
            adj_cells.append([self.grid[i][j] for j in valid_cols])
        return adj_cells

    def set_adj_counts(self):
        [[self.add_adj_count_values((j, i), self.offset_3) for i in range(self.cols)] for j in range(self.rows)]

           
    def add_adj_count_values(self, coord, offset):
        row, col = coord
        array = self.get_adj_cells(coord, offset)
        flat_array = self.flatten(array)

        mines = self.count_mines(flat_array)
        self.grid[row][col].adj_mines = mines

        empty = self.count_empty(flat_array)
        self.grid[row][col].adj_empty = empty


        all_empty = len(flat_array) == empty
        self.grid[row][col].all_adj_cells_empty = all_empty


    def count_mines(self, array):
        result = [x for x in array if x.is_mine]
        return len(result)

    def count_empty(self, array):
        result = [x for x in array if x.is_empty]
        return len(result)

    def cascade_empty_cells(self, cell : GridCell, offset):
        for i in self.get_adj_cells(cell.coord, offset):
            if cell.adj_mines == 0 and cell.is_empty and not cell.is_revealed:
                cell.reveal_empty_cell()
                self.cascade_empty_cells(i, offset)

    @staticmethod
    def flatten(t):
        return [item for sublist in t for item in sublist]


result = Grid(20, 20, 50)

result.add_mines()

print(result)
result.set_adj_counts()
print(result)

result.cascade_empty_cells(result.grid[0][0], result.offset_3)

print(result)