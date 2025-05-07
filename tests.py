import unittest
from maze import Maze
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_one(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_cell_instances(self):
        m = Maze(0, 0, 2, 2, 10, 10)
        for col in m._cells:
            for cell in col:
                self.assertIsInstance(cell, Cell)

    def test_draw_cell_without_window(self):
        m = Maze(0, 0, 2, 2, 10, 10)
        try:
            m._draw_cell(0, 0)  # should not raise
        except Exception as e:
            self.fail(f"_draw_cell raised an exception with no window: {e}")

    def test_maze_entrance_exit(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        entrance = m1._cells[0][0]
        exit = m1._cells[len(m1._cells)-1][len(m1._cells[0])-1]
        self.assertFalse(entrance.has_left_wall)
        self.assertFalse(exit.has_right_wall)

    def test_maze_reset_visited(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertFalse(m1._cells[i][j].visited)

if __name__ == "__main__":
    unittest.main()