import tkinter as tk

from othello_game import OthelloGame
from othello_renderer import OthelloRenderer
from othello_rules import OthelloRules

# This class was generated with the help of chatgpt 4.o
class OthelloController:
    """Main entry point for the game, manages the game loop."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Othello Game")

        # Create game components
        self.game = OthelloGame()
        self.rules = OthelloRules()
        self.renderer = OthelloRenderer(self.root, self.game, self.rules)

    def run(self):
        """Start the game loop."""
        self.root.mainloop()
