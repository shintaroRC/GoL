class game_of_life:
    def __init__(self, width=None, height=None, cells=None):
        self.width = width
        self.height = height
        if cells is None:
            self.cells = [[0 for x in range(width)] for y in range(height)]
        else:
            self.cells = cells

        if width is None:
            self.width = len(cells[0])

        if height is None:
            self.height = len(cells)

    def update_cells(self):
        width = self.width
        height = self.height
        new_cells = [[0 for x in range(width)] for y in range(height)]
        for i in range(height):
            for j in range(width):
                new_cells[i][j] = self._next_cell_state(i, j)

        self.cells = new_cells[:]

    def _num_of_nbhd(self, i, j):
        return (self.cells[(i-1+self.height)%self.height][(j-1+self.width)%self.width]
        +self.cells[i][(j-1+self.width)%self.width]+self.cells[(i+1)%self.height][(j-1+self.width)%self.width]
        +self.cells[(i-1+self.height)%self.height][j]+self.cells[(i+1)%self.height][j]
        +self.cells[(i-1+self.height)%self.height][(j+1)%self.width]+self.cells[i][(j+1)%self.width]
        +self.cells[(i+1)%self.height][(j+1)%self.height])

    def _next_cell_state(self, i, j):
        if self.cells[i][j]==0:
            if self._num_of_nbhd(i, j)==3:
                return 1
            else:
                return 0
        else:
            if ((self._num_of_nbhd(i, j)==2) or (self._num_of_nbhd(i, j)==3)):
                return 1
            else:
                return 0
