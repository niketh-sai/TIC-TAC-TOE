"""
AI Engine Module for Tic Tac Toe
Implements different difficulty levels including Minimax algorithm
"""

import random
from typing import List, Optional, Tuple
from game_logic import TicTacToeGame


class AIEngine:
    """AI opponent with multiple difficulty levels"""
    
    def __init__(self, difficulty: str = "medium"):
        self.difficulty = difficulty.lower()
        self.game = TicTacToeGame()
    
    def set_difficulty(self, difficulty: str) -> None:
        """
        Set AI difficulty level
        
        Args:
            difficulty: 'easy', 'medium', or 'hard'
        """
        self.difficulty = difficulty.lower()
    
    def make_move(self, board: List[str], ai_symbol: str) -> int:
        """
        Make a move based on difficulty level
        
        Args:
            board: Current board state
            ai_symbol: AI's symbol ('X' or 'O')
            
        Returns:
            Position (0-8) where AI will move
        """
        self.game.board = board.copy()
        available_moves = self.game.get_available_moves()
        
        if not available_moves:
            return -1
        
        if self.difficulty == "easy":
            return self._make_easy_move(available_moves)
        elif self.difficulty == "medium":
            return self._make_medium_move(board, ai_symbol, available_moves)
        elif self.difficulty == "hard":
            return self._make_hard_move(board, ai_symbol)
        else:
            return self._make_medium_move(board, ai_symbol, available_moves)
    
    def _make_easy_move(self, available_moves: List[int]) -> int:
        """
        Easy difficulty: Random move
        
        Args:
            available_moves: List of available positions
            
        Returns:
            Random position
        """
        return random.choice(available_moves)
    
    def _make_medium_move(self, board: List[str], ai_symbol: str, 
                         available_moves: List[int]) -> int:
        """
        Medium difficulty: Mix of random and strategic moves
        - 40% chance to make optimal move
        - 60% chance to make random move
        
        Args:
            board: Current board state
            ai_symbol: AI's symbol
            available_moves: List of available positions
            
        Returns:
            Selected position
        """
        # 40% chance to play optimally
        if random.random() < 0.4:
            return self._make_hard_move(board, ai_symbol)
        
        # Otherwise make a random move with some strategy
        # Try to block or win with 30% chance
        if random.random() < 0.3:
            # Check if AI can win
            for move in available_moves:
                board_copy = board.copy()
                board_copy[move] = ai_symbol
                if self._check_winner(board_copy) == ai_symbol:
                    return move
            
            # Check if need to block opponent
            opponent_symbol = "O" if ai_symbol == "X" else "X"
            for move in available_moves:
                board_copy = board.copy()
                board_copy[move] = opponent_symbol
                if self._check_winner(board_copy) == opponent_symbol:
                    return move
        
        # Default to random move
        return random.choice(available_moves)
    
    def _make_hard_move(self, board: List[str], ai_symbol: str) -> int:
        """
        Hard difficulty: Minimax algorithm for optimal play
        
        Args:
            board: Current board state
            ai_symbol: AI's symbol
            
        Returns:
            Optimal position
        """
        opponent_symbol = "O" if ai_symbol == "X" else "X"
        
        # Use minimax to find best move
        best_score = float('-inf')
        best_move = -1
        
        for move in range(9):
            if board[move] == " ":
                board[move] = ai_symbol
                score = self._minimax(board, 0, False, ai_symbol, opponent_symbol)
                board[move] = " "
                
                if score > best_score:
                    best_score = score
                    best_move = move
        
        return best_move
    
    def _minimax(self, board: List[str], depth: int, is_maximizing: bool,
                ai_symbol: str, opponent_symbol: str) -> int:
        """
        Minimax algorithm implementation
        
        Args:
            board: Current board state
            depth: Current depth in the tree
            is_maximizing: Whether it's maximizing player's turn
            ai_symbol: AI's symbol
            opponent_symbol: Opponent's symbol
            
        Returns:
            Score of the position
        """
        winner = self._check_winner(board)
        
        # Terminal states
        if winner == ai_symbol:
            return 10 - depth
        if winner == opponent_symbol:
            return depth - 10
        if " " not in board:
            return 0  # Draw
        
        if is_maximizing:
            best_score = float('-inf')
            for move in range(9):
                if board[move] == " ":
                    board[move] = ai_symbol
                    score = self._minimax(board, depth + 1, False, 
                                         ai_symbol, opponent_symbol)
                    board[move] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in range(9):
                if board[move] == " ":
                    board[move] = opponent_symbol
                    score = self._minimax(board, depth + 1, True, 
                                         ai_symbol, opponent_symbol)
                    board[move] = " "
                    best_score = min(score, best_score)
            return best_score
    
    def _check_winner(self, board: List[str]) -> Optional[str]:
        """
        Check if there's a winner on the board
        
        Args:
            board: Board state to check
            
        Returns:
            Winner symbol or None
        """
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combination in winning_combinations:
            if (board[combination[0]] == board[combination[1]] == 
                board[combination[2]] != " "):
                return board[combination[0]]
        
        return None
    
    def get_difficulty_description(self) -> str:
        """
        Get description of current difficulty
        
        Returns:
            Description string
        """
        descriptions = {
            "easy": "Easy - Computer makes random moves",
            "medium": "Medium - Computer uses basic strategy",
            "hard": "Hard - Computer uses Minimax algorithm (unbeatable)"
        }
        return descriptions.get(self.difficulty, "Medium")
