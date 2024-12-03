import math
from config import BOARD_SIZE, BLACK, WHITE

# This class was generated with the help of chatgpt 4.o
class OthelloAI:
    """Handles AI decisions using Minimax with Alpha-Beta pruning."""

    def __init__(self, game, rules):
        self.game = game
        self.rules = rules

    def evaluate_board(self, board, player):
        """Evaluation function to score the board for the given player."""
        opponent = WHITE if player == BLACK else BLACK
        player_score = sum(row.count(player) for row in board)
        opponent_score = sum(row.count(opponent) for row in board)
        return player_score - opponent_score

    def minimax(self, board, depth, maximizing_player, alpha, beta, player):
        """Minimax algorithm with Alpha-Beta pruning."""
        if depth == 0 or not self.has_valid_moves(board, player):
            return self.evaluate_board(board, player), None

        best_move = None

        if maximizing_player:
            max_eval = -math.inf
            for move in self.get_all_valid_moves(board, player):
                new_board = self.simulate_move(board, move[0], move[1], player)
                eval_score, _ = self.minimax(new_board, depth - 1, False, alpha, beta, WHITE)
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = math.inf
            for move in self.get_all_valid_moves(board, player):
                new_board = self.simulate_move(board, move[0], move[1], player)
                eval_score, _ = self.minimax(new_board, depth - 1, True, alpha, beta, BLACK)
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def get_all_valid_moves(self, board, player):
        """Get all valid moves for the given player."""
        valid_moves = []
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.rules.is_valid_move(board, row, col, player):
                    valid_moves.append((row, col))
        return valid_moves

    def simulate_move(self, board, row, col, player):
        """Simulate making a move without altering the original board."""
        simulated_board = [row[:] for row in board]
        simulated_board[row][col] = player
        return simulated_board

    def has_valid_moves(self, board, player):
        """Check if the player has any valid moves."""
        return any(self.rules.is_valid_move(board, row, col, player)
            for row in range(BOARD_SIZE)
            for col in range(BOARD_SIZE))
