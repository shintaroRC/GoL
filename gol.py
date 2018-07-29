#!/usr/bin/env python3
# -*- coding: utf8 -*-

class game_of_life:
    def __init__(self, width=None, height=None, cells=None):
        self.width = width
        self.height = height
        if cells is None:
            self.cells = [[False for x in range(width)] for y in range(height)]
        else:
            self.cells = cells

        if width is None:
            self.width = len(cells[0])

        if height is None:
            self.height = len(cells)

    def __str__(self):
        return "\n".join(["".join(['■'if x else '□' for x in row]) for row in self.cells])

    def update_cells(self):
        width = self.width
        height = self.height
        new_cells = [[False for x in range(width)] for y in range(height)]
        for i in range(height):
            for j in range(width):
                new_cells[i][j] = self._next_cell_state(i, j)

        self.cells = new_cells[:]

    def _num_of_nbhd(self, i, j):
        above = i-1
        below = (i+1)%self.height
        left = j-1
        right = (j+1)%self.width
        list_of_nbhd = [self.cells[above][left], self.cells[i][left],
                        self.cells[below][left],
                        self.cells[above][j],
                        self.cells[below][j],
                        self.cells[above][right],
                        self.cells[i][right],
                        self.cells[below][right]]

        return len(list(filter(lambda x:x, list_of_nbhd)))

    def _next_cell_state(self, i, j):
        if not self.cells[i][j]:
            if self._num_of_nbhd(i, j)==3:
                return True
            else:
                return False
        else:
            if ((self._num_of_nbhd(i, j)==2) or (self._num_of_nbhd(i, j)==3)):
                return True
            else:
                return False

if __name__ == "__main__":
    example_cells = game_of_life(cells=[[False,True,False,False,False],
                                        [False,False,True,False,False],
                                        [True,True,True,False,False],
                                        [False,False,False,False,False],
                                        [False,False,False,False,False]])
    print(example_cells)
    print("")
    example_cells.update_cells()
    print(example_cells)
    print("")
    example_cells.update_cells()
    print(example_cells)
    print("")
    example_cells.update_cells()
    print(example_cells)
    print("")
    example_cells.update_cells()
    print(example_cells)
    print("")
    example_cells.update_cells()
    print(example_cells)
    print("")
