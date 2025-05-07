import time
import random
from cell import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        if seed:
            random.seed(seed)
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)

    def _create_cells(self):
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                # xy1 = (j * self._cell_size_x, i * self._cell_size_y)
                # xy2 = (xy1[0] + self._cell_size_x, xy1[1] + self._cell_size_y)
                self._cells[i].extend([Cell(self._window)])

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._window is None:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        if not self._cells:
            return
        # Break entrance
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        # Break exit
        exit_col, exit_row = len(self._cells) - 1, len(self._cells[0]) - 1
        self._cells[exit_col][exit_row].has_right_wall = False
        self._draw_cell(exit_col, exit_row)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            directions = []

            # Check each direction for unvisited neighbors
            if i > 0 and not self._cells[i - 1][j].visited:
                directions.append(("left", i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                directions.append(("right", i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                directions.append(("up", i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                directions.append(("down", i, j + 1))

            # If no unvisited neighbors, draw and return
            if not directions:
                self._draw_cell(i, j)
                return

            # Choose random direction and get target cell
            direction, ni, nj = random.choice(directions)
            next_cell = self._cells[ni][nj]

            # Knock down the walls between current and next cell
            if direction == "left":
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif direction == "right":
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif direction == "up":
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif direction == "down":
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False

            self._break_walls_r(ni, nj)