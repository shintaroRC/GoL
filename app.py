#!/usr/bin/env python3
# -*- coding: utf8 -*-
from gol import game_of_life
import tkinter as tk
import ast

class GoLPainter:
    def __init__(self, master, cell_size, alive_color, dead_color, margin, gol):
        self.master = master
        self.cell_size = cell_size
        self.alive_color = alive_color
        self.dead_color = dead_color
        self.margin = margin
        self.gol = gol
        self.width = cell_size*gol.width+margin*2
        self.height = cell_size*gol.height+margin*2
        self.view = self._create_cells_view(master)
        self.view.bind('<space>', self.upadate_cells_generation)
        self.view.focus_set()
        self.view.place(x=0,y=0)

    def _create_cells_view(self, master):
        cells_view = tk.Canvas(master, width=self.width, height=self.height)
        for row_index in range(self.gol.height):
            for column_index in range(self.gol.width):
                cell_color = self.alive_color if self.gol.cells[row_index][column_index] else self.dead_color
                cell_tag = (str(row_index), str(column_index))
                cells_view.create_rectangle(column_index*self.cell_size+self.margin,
                                            row_index*self.cell_size+self.margin,
                                            (column_index+1)*self.cell_size+self.margin,
                                            (row_index+1)*self.cell_size+self.margin,
                                            width=0,
                                            fill= cell_color,
                                            tag= cell_tag)
        cells_view.tag_bind('all', '<Button-1>', self.change_cell_state_on_click)
        return cells_view

    def upadate_cells_generation(self, event):
        self.gol.update_cells()
        canvas = event.widget
        for item in canvas.find_withtag('all'):
            cell_tag = canvas.gettags(item)
            row_index = int(cell_tag[0])
            column_index = int(cell_tag[1])
            new_cell_color = self.alive_color if self.gol.cells[row_index][column_index] else self.dead_color
            canvas.itemconfig(item, fill=new_cell_color   )

    def change_cell_state_on_click(self, event):
        canvas = event.widget
        cell = canvas.find_withtag('current')
        row_index =  int(canvas.gettags(cell)[0])
        column_index = int(canvas.gettags(cell)[1])

        self.gol.cells[row_index][column_index] = not self.gol.cells[row_index][column_index]
        new_cell_color = self.alive_color if self.gol.cells[row_index][column_index] else self.dead_color
        canvas.itemconfig(cell,fill=new_cell_color)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Game of Life Simulator')

    # example_cells = game_of_life(cells=[[False,True,False,False,False,False,False,False,False,False],
    #                                     [False,False,True,False,False,False,False,False,False,False],
    #                                     [True,True,True,False,False,False,False,False,False,False],
    #                                     [False,False,False,False,False,False,False,False,False,False],
    #                                     [False,False,False,False,False,False,False,False,False,False],
    #                                     [False,False,False,False,False,False,False,False,False,False],
    #                                     [False,False,False,False,False,False,False,False,False,False],
    #                                     [False,False,False,False,False,False,False,False,False,False],
    #                                     [False,False,False,False,False,False,False,False,False,False],
    #                                     [False,False,False,False,False,False,False,False,False,False]])

    example_cells = game_of_life(50,50)

    example_painter = GoLPainter(root, cell_size=20, alive_color='#000000', dead_color='#ffffff', margin=3, gol=example_cells)
    root.geometry(str(example_painter.width) + 'x' + str(example_painter.height))

    root.mainloop()
