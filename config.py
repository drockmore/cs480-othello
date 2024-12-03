BOARD_SIZE = 8  # 8x8 Othello board
CELL_SIZE = 60  # Cell size in pixels
EMPTY = 0
BLACK = 1
WHITE = 2


# Directions for traversal (8 directions)
DIRECTIONS = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1),   # Right
            (-1, -1), # Up-Left
            (-1, 1),  # Up-Right
            (1, -1),  # Down-Left
            (1, 1),   # Down-Right
        ]