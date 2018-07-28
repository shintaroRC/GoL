#!/usr/bin/env python3
# -*- coding: utf8 -*-
from gol import game_of_life
import tkinter as tk

class GoLPainter:
    def __init__(self, master, cell_size, alive_color, dead_color, gol):
        self.cell_size = cell_size
        self.alive_color = alive_color
        self.dead_color = dead_color
        self.gol = gol
        self.width = cell_size*gol.width
        self.height = cell_size*gol.height
        self.view = self._create_cells_view(master, gol.cells)

    def _create_cells_view(self, master, cells_state):
        cells_view = tk.Frame(master, width=self.width, height=self.height)
        for cells_row_state in cells_state:
            self._create_cells_row_view(cells_view, cells_row_state).pack(side='top')

        return cells_view

    def _create_cells_row_view(self, master, cells_row_state):
        cells_row_view = tk.Frame(master, width=self.width, height=self.cell_size)
        for cell_state in cells_row_state:
            self._create_cell_view(cells_row_view, cell_state).pack(side='left')

        return cells_row_view

    def _create_cell_view(self, master, cell_state):
        if cell_state:
            cell_color = self.alive_color
        else:
            cell_color = self.dead_color
        cell_view = tk.Frame(master,
                        width  = self.cell_size,
                        height = self.cell_size,
                        bg  = cell_color)

        return cell_view

    def change_cell_state(self, event):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Game of Life')

    example_cells = game_of_life(cells=[[False,True,False,False,False,False,False,False,False,False],
                                        [False,False,True,False,False,False,False,False,False,False],
                                        [True,True,True,False,False,False,False,False,False,False],
                                        [False,False,False,False,False,False,False,False,False,False],
                                        [False,False,False,False,False,False,False,False,False,False],
                                        [False,False,False,False,False,False,False,False,False,False],
                                        [False,False,False,False,False,False,False,False,False,False],
                                        [False,False,False,False,False,False,False,False,False,False],
                                        [False,False,False,False,False,False,False,False,False,False],
                                        [False,False,False,False,False,False,False,False,False,False]])

    example_painter = GoLPainter(root, 10, '#000000', '#ffffff', example_cells)

    root.geometry(str(example_painter.width) + 'x' + str(example_painter.height))

    example_view_of_cells = example_painter.view

    example_view_of_cells.pack(anchor=tk.NE, side='left')

    root.mainloop()
