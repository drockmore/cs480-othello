import tkinter as tk
from config import BOARD_SIZE, BLACK, WHITE, CELL_SIZE
from othello_ai import OthelloAI
import math


# This class was generated with the help of chatgpt 4.o
class OthelloRenderer:
    """Handles rendering the game board and interacting with the user."""

    def __init__(self, root, game, rules):
        self.game = game
        self.rules = rules
        self.root = root
        self.ai = OthelloAI(game, rules)

        # Create canvas for the board
        self.canvas = tk.Canvas(root, width=BOARD_SIZE * CELL_SIZE, height=BOARD_SIZE * CELL_SIZE)
        self.canvas.grid(row=1, column=0, columnspan=3)

        # Create labels for the score
        self.black_score_label = tk.Label(root, text="Black: 2", font=("Helvetica", 14), fg="black")
        self.black_score_label.grid(row=0, column=0, sticky="w")

        self.current_player_label = tk.Label(root, text="Black", font=("Helvetica", 14), fg="black")
        self.current_player_label.grid(row=0, column=1, sticky="n")
        
        self.white_score_label = tk.Label(root, text="White: 2", font=("Helvetica", 14), fg="black")
        self.white_score_label.grid(row=0, column=2, sticky="e")

        # Bind click event to the board
        self.canvas.bind("<Button-1>", self.handle_click)

        # Draw the initial board
        self.draw_board()

    def draw_board(self):
        """Render the board and pieces."""
        self.canvas.delete("all")
        board = self.game.get_board()

        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                x1 = i * CELL_SIZE
                y1 = j * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                # Draw the cell
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="black")

                # Draw the pieces
                if board[j][i] == BLACK:
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="black")
                elif board[j][i] == WHITE:
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="white")

        # Update the scores
        self.update_scores()

    def update_scores(self):
        """Update the score labels."""
        black_score, white_score = self.game.get_scores()
        self.black_score_label.config(text=f"Black: {black_score}")
        self.white_score_label.config(text=f"White: {white_score}")
        self.current_player_label.config(text=f"Black" if self.game.get_current_player() == BLACK else "White")
    

    def handle_click(self, event):
        """Handle click events on the board."""
        # If it's not the player's turn, exit
        if self.game.get_current_player() == WHITE:
            return  # Wait for AI's turn

        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE

        # Try to make a move
        if self.game.make_move(row, col, self.rules):
            self.draw_board()

            # Check if AI needs to skip its turn
            skip_player_turn, end_game = self.game.auto_skip_turn(self.rules)
           
            if skip_player_turn:
                self.draw_board()  # Update the board if a turn is skipped
                return 
            
            if end_game:
                self.current_player_label.config(text="Game Over")
                return 
            
            self.root.after(500, self.ai_move)  # Delay for AI move
            


    def ai_move(self):
        """Let the AI make a move."""
        _, best_move = self.ai.minimax(self.game.get_board(), depth=3, maximizing_player=True, alpha=-math.inf, beta=math.inf, player=WHITE)
        
        if best_move != None:
            self.game.make_move(best_move[0], best_move[1], self.rules)
            self.draw_board()
        else:
            self.game.switch_player()

