from config import BOARD_SIZE, BLACK, WHITE, EMPTY

#This class was generated with the help of chatgpt 4.o
class OthelloGame:
    """Handles the game state and logic."""

    def __init__(self):
        # Initialize the board
        self.board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.black_score = 2
        self.white_score = 2
        self.current_player = BLACK
        self.initialize_board()


    def initialize_board(self):
        """Set up the initial game state."""
        self.board[3][3] = WHITE
        self.board[4][4] = WHITE
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        
        
    def get_board(self):
        """Return the current board state."""
        return self.board


    def switch_player(self):
        """Switch to the next player."""
        self.current_player = BLACK if self.current_player == BLACK else WHITE
        
        if self.current_player == BLACK:
            self.current_player = WHITE
        else:
            self.current_player = BLACK

        
    def skip_turn(self):
        """Skip the turn if no valid moves are available."""
        self.switch_player()
        return


    def get_scores(self):
        """Return the current scores."""
        return self.black_score, self.white_score
    

    def update_score(self, player, points):
        """Update the score for the player."""
        if player == BLACK:
            self.black_score += points
            self.white_score -= points - 1
        else:
            self.white_score += points
            self.black_score -= points - 1


    def make_move(self, row, col, rules):
        """Make a move if valid, and flip the pieces."""
        flips = rules.is_valid_move(self.board, row, col, self.current_player)
        
        if len(flips) == 0:
            return False
        
        self.board[row][col] = self.current_player
    
        for flip in flips:
            self.board[flip[0]][flip[1]] = self.current_player

        self.update_score(self.current_player, len(flips) + 1)
        self.switch_player()
        return True


    def get_current_player(self):
        """Return the current player."""
        return self.current_player


    def has_valid_moves(self, rules, player):
        """Check if the player has any valid moves."""
        move_black = False 
        move_white = False
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if len(rules.is_valid_move(self.get_board(), row, col, BLACK)) > 0:
                    move_black = True
                if len(rules.is_valid_move(self.get_board(), row, col, WHITE)) > 0:
                    move_white = True
        
        return move_black, move_white


    def auto_skip_turn(self, rules):
        """Check if the current player has moves. If not, skip their turn."""
        move_black, move_white = self.has_valid_moves(rules, self.current_player)
        
        if self.current_player == BLACK and not move_black:
            self.skip_turn()
            return True, False
        
        if self.current_player == WHITE and not move_white:
            self.skip_turn()
            return True, False 
        
        if not move_black and not move_white:
            return False, True             
        
        return False, False
