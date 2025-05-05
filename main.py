from graphics import Window
from maze import Maze


def main():
    # window = Window(800, 600)
    # win.draw_line(Line(Point(100,100), Point(200,200)), fill_color='red')
    # win.draw_line(Line(Point(100,100), Point(600,400)), fill_color='blue')
    # c1 = Cell((100,100), (200,200), window)
    # c2 = Cell((150,150), (700,500), window)
    # c1.has_left_wall = False
    # c2.has_bottom_wall = False
    # c1.draw()
    # c2.draw()
    # c1.draw_move(c2, undo=False)

    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    window = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window)

    window.wait_for_close()

if __name__ == "__main__":
    main()