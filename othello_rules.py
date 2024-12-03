from config import EMPTY, BLACK, WHITE, BOARD_SIZE, DIRECTIONS

# This class was generated with the help of chat gpt 4.o
class OthelloRules:
    """Encapsulates the rules of Othello."""

    def is_valid_move(self, board, row, col, player):
        """Check if the move is valid."""
        
        # Return if the position is not empty
        if board[row][col] != EMPTY:
            return []

        return self.get_valid_flips(board, row, col, player)
        

    def get_valid_flips(self, board, row, col, player):
        """Get the coordinates of tiles that would be flipped if a move is valid.
    Args:
        board: The current Othello board state.
        row: The row index of the move.
        col: The column index of the move.
        player: The current player's color (BLACK or WHITE).
    
    Returns:
        A list of tuples with coordinates of tiles to flip if the move is valid.
        If the move is invalid, an empty list is returned.
        """
        if board[row][col] != EMPTY:
            return []  # The position must be empty to place a piece.

        opponent = WHITE if player == BLACK else BLACK
        tiles_to_flip = []

        for dr, dc in DIRECTIONS:
            flips = []
            curr_row, curr_col = row + dr, col + dc

            while 0 <= curr_row < BOARD_SIZE and 0 <= curr_col < BOARD_SIZE:
                if board[curr_row][curr_col] == opponent:
                    flips.append((curr_row, curr_col))
                elif board[curr_row][curr_col] == player:
                    # If we find the player's piece, add all flips to the main list.
                    tiles_to_flip.extend(flips)
                    break
                else:
                    # Encounter an empty space, invalid direction.
                    break

                # Move in the current direction
                curr_row += dr
                curr_col += dc

        return tiles_to_flip

