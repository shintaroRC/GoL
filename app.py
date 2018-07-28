#!/usr/bin/env python3
# -*- coding: utf8 -*-
from gol import game_of_life
import tkinter as tk

class GoLPainter:
    def __init__(self, master, cell_size, alive_color, dead_color, gol):
        self.master = master
        self.cell_size = cell_size
        self.alive_color = alive_color
        self.dead_color = dead_color
        self.gol = gol
        self.width = cell_size*gol.width
        self.height = cell_size*gol.height
        self.view = self._create_cells_view(master)
        self.view.pack()

    def _create_cells_view(self, master):
        cells_view = tk.Frame(master, width=self.width, height=self.height)
        for cells_row_index in range(self.gol.height):
            self._create_cells_row_view(cells_view, cells_row_index).pack(side='top')

        return cells_view

    def _create_cells_row_view(self, master, cells_row_index):
        cells_row_view = tk.Frame(master, width=self.width, height=self.cell_size)
        for cells_column_index in range(self.gol.width):
            cell_view = self._create_cell_view(cells_row_view, cells_row_index, cells_column_index)
            cell_view.bind('<Button-1>', self.change_cell_state_on_click)
            cell_view.pack(side='left')

        return cells_row_view

    def _create_cell_view(self, master, cells_row_index, cells_column_index):
        return CellWidget(master, self.cell_size, self.alive_color, self.dead_color,
                            self.gol.cells[cells_row_index][cells_column_index],
                            cells_row_index, cells_column_index)


    def upadate_cells_generation(self):
        pass

    def change_cell_state_on_click(self, event):
        row_index = event.widget.row_index
        column_index = event.widget.column_index
        self.gol.cells[row_index][column_index] = not self.gol.cells[row_index][column_index]
        event.widget['bg'] = self.alive_color if self.gol.cells[row_index][column_index] else self.dead_color

class CellWidget(tk.Frame):
    def __init__(self, master, cell_size, alive_color, dead_color, cell_state, row_index, column_index):
        super().__init__(master,width=cell_size, height=cell_size,bg=alive_color if cell_state else dead_color)
        self.row_index = row_index
        self.column_index = column_index


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Game of Life Simulator')

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

    example_painter = GoLPainter(root, cell_size=10, alive_color='#000000', dead_color='#ffffff', gol=example_cells)
    root.geometry(str(example_painter.width) + 'x' + str(example_painter.height))

    root.mainloop()
