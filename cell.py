from graphics import Line, Point

class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._window = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._window is None:
            return
        
        walls = [
            (self.has_left_wall, Point(x1, y1), Point(x1, y2)),
            (self.has_right_wall, Point(x2, y1), Point(x2, y2)),
            (self.has_top_wall, Point(x1, y1), Point(x2, y1)),
            (self.has_bottom_wall, Point(x1, y2), Point(x2, y2)),
        ]

        for has_wall, p1, p2 in walls:
            color_arg = {} if has_wall else {'fill_color': 'white'}
            self._window.draw_line(Line(p1, p2), **color_arg)

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = 'gray'
        else:
            color = 'red'

        start_xy = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        end_xy = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)

        # Move left/right
        x_dist = abs(start_xy.x - end_xy.x)
        if start_xy.x < end_xy.x:
            mid_xy = Point(start_xy.x + x_dist, start_xy.y)
            # self.window.draw_line(Line(start_xy, Point(start_xy.x + x_dist, start_xy.y)), color)
        else:
            mid_xy = Point(start_xy.x - x_dist, start_xy.y)
            # self.window.draw_line(Line(start_xy, Point(start_xy.x - x_dist, start_xy.y)), color)
        self._window.draw_line(Line(start_xy, mid_xy), color)

        # Move up/down, from mid_xy
        self._window.draw_line(Line(mid_xy, end_xy), color)