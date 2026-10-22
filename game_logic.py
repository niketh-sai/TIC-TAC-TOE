"""
Game Logic Module for Tic Tac Toe
Handles core game mechanics, state management, and win/draw detection
"""

from typing import List, Optional, Tuple
import copy


class TicTacToeGame:
    """Core game logic for Tic Tac Toe"""
    
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.game_over = False
        self.winner = None
        self.winning_combination = None
        self.draw = False
        
    def initialize_game(self) -> None:
        """Initialize/reset the game board and state"""
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.game_over = False
        self.winner = None
        self.winning_combination = None
        self.draw = False
    
    def make_move(self, position: int, player: str) -> bool:
        """
        Make a move on the board
        
        Args:
            position: Board position (0-8)
            player: Player symbol ('X' or 'O')
            
        Returns:
            True if move was successful, False otherwise
        """
        if self.game_over:
            return False
        if position < 0 or position > 8:
            return False
        if self.board[position] != " ":
            return False
        
        self.board[position] = player
        self.current_player = "O" if player == "X" else "X"
        
        # Check for winner or draw
        self.winner, self.winning_combination = self.check_winner()
        if self.winner:
            self.game_over = True
        elif self.check_draw():
            self.draw = True
            self.game_over = True
        
        return True
    
    def check_winner(self) -> Tuple[Optional[str], Optional[List[int]]]:
        """
        Check if there's a winner
        
        Returns:
            Tuple of (winner_symbol, winning_combination) or (None, None)
        """
        # All possible winning combinations
        winning_combinations = [
            [0, 1, 2],  # Top row
            [3, 4, 5],  # Middle row
            [6, 7, 8],  # Bottom row
            [0, 3, 6],  # Left column
            [1, 4, 7],  # Middle column
            [2, 5, 8],  # Right column
            [0, 4, 8],  # Diagonal top-left to bottom-right
            [2, 4, 6],  # Diagonal top-right to bottom-left
        ]
        
        for combination in winning_combinations:
            if (self.board[combination[0]] == self.board[combination[1]] == 
                self.board[combination[2]] != " "):
                return self.board[combination[0]], combination
        
        return None, None
    
    def check_draw(self) -> bool:
        """
        Check if the game is a draw
        
        Returns:
            True if draw, False otherwise
        """
        return " " not in self.board and self.winner is None
    
    def get_available_moves(self) -> List[int]:
        """
        Get list of available moves
        
        Returns:
            List of available positions (0-8)
        """
        return [i for i, cell in enumerate(self.board) if cell == " "]
    
    def is_valid_move(self, position: int) -> bool:
        """
        Check if a move is valid
        
        Args:
            position: Board position (0-8)
            
        Returns:
            True if move is valid, False otherwise
        """
        return (0 <= position <= 8 and 
                self.board[position] == " " and 
                not self.game_over)
    
    def get_board_copy(self) -> List[str]:
        """
        Get a copy of the current board
        
        Returns:
            Copy of the board
        """
        return copy.deepcopy(self.board)
    
    def get_game_state(self) -> dict:
        """
        Get current game state
        
        Returns:
            Dictionary containing game state information
        """
        return {
            "board": self.board,
            "current_player": self.current_player,
            "game_over": self.game_over,
            "winner": self.winner,
            "winning_combination": self.winning_combination,
            "draw": self.draw
        }


class Scoreboard:
    """Scoreboard management for game statistics"""
    
    def __init__(self):
        self.scores = {
            "X": 0,
            "O": 0,
            "Computer": 0,
            "Draw": 0,
            "Total": 0
        }
        self.history = []
    
    def update_score(self, winner: str, is_draw: bool = False) -> None:
        """
        Update scoreboard after a game
        
        Args:
            winner: Winner symbol ('X', 'O', 'Computer')
            is_draw: Whether the game was a draw
        """
        self.scores["Total"] += 1
        
        if is_draw:
            self.scores["Draw"] += 1
            self.history.append({
                "match": self.scores["Total"],
                "result": "Draw",
                "winner": None
            })
        else:
            self.scores[winner] += 1
            self.history.append({
                "match": self.scores["Total"],
                "result": "Win",
                "winner": winner
            })
    
    def get_scores(self) -> dict:
        """
        Get current scores
        
        Returns:
            Dictionary of scores
        """
        return self.scores
    
    def get_history(self) -> List[dict]:
        """
        Get game history
        
        Returns:
            List of match results
        """
        return self.history
    
    def reset_scores(self) -> None:
        """Reset all scores and history"""
        self.scores = {
            "X": 0,
            "O": 0,
            "Computer": 0,
            "Draw": 0,
            "Total": 0
        }
        self.history = []
