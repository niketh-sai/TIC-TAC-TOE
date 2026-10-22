# 🎮 Tic Tac Toe - Premium Gaming Experience

A modern, visually stunning Tic Tac Toe game built with Python and Streamlit. Featuring multiple game modes, AI opponents with varying difficulty levels, and a premium gaming interface with glassmorphism design.

![Tic Tac Toe](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

### 🎯 Game Modes
- **Player vs Player**: Two players compete on the same device
- **Player vs Computer**: Challenge an AI opponent with three difficulty levels

### 🤖 AI Difficulty Levels
- **Easy**: Computer makes random valid moves
- **Medium**: Computer uses basic strategy (blocks wins, attempts winning moves)
- **Hard**: Computer uses the Minimax algorithm for optimal, unbeatable play

### 🎨 Premium UI/UX
- Dark gaming theme with deep navy background
- Neon accent colors (electric blue, purple, cyan)
- Glassmorphism cards with blur effects
- Smooth animations and transitions
- Responsive design for all devices
- Custom typography with Orbitron and Rajdhani fonts

### 📊 Game Features
- Real-time scoreboard tracking
- Game history with match results
- Winning combination highlighting
- Draw detection
- Turn indicators
- Play again and new game options
- Settings panel for customization

### 🔧 Technical Features
- Modular architecture with separate game logic and AI engine
- Clean, maintainable Python code
- Streamlit session state management
- Custom CSS3 styling
- Minimax algorithm implementation

## 📁 Project Structure

```
tic_tac_toe/
│
├── app.py                 # Main Streamlit application
├── game_logic.py          # Core game logic and state management
├── ai_engine.py           # AI opponent with Minimax algorithm
├── styles.css             # Custom CSS styling
├── requirements.txt       # Python dependencies
├── README.md             # This file
│
├── assets/
│   ├── sounds/           # Sound effects directory
│   └── images/           # Image assets directory
```

## 🚀 Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Steps

1. **Clone or download the project**
   ```bash
   cd TIC-TAC-TOE
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Running the Application

### Start the game
```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

### Controls
- Click on cells to make moves
- Use the sidebar to change settings
- Select game mode and difficulty from the landing page
- Use "Play Again" to restart with current scores
- Use "New Game" to reset everything

## 🧠 Minimax AI Implementation

### Overview
The Minimax algorithm is a recursive decision-making algorithm used in two-player games. It explores all possible game states to determine the optimal move.

### How It Works

1. **Game Tree Exploration**: The algorithm builds a tree of all possible moves and counter-moves
2. **Scoring System**: 
   - AI wins: +10 (minus depth to prefer faster wins)
   - Opponent wins: -10 (plus depth to delay losses)
   - Draw: 0

3. **Maximizing and Minimizing**:
   - **Maximizing player (AI)**: Chooses moves with the highest score
   - **Minimizing player (Opponent)**: Chooses moves with the lowest score

4. **Depth Factor**: The depth parameter helps the AI prefer winning sooner and losing later

### Implementation Details

```python
def _minimax(self, board: List[str], depth: int, is_maximizing: bool,
            ai_symbol: str, opponent_symbol: str) -> int:
    """
    Recursive minimax implementation
    - Explores all possible game states
    - Returns optimal score for current position
    """
    winner = self._check_winner(board)
    
    # Terminal states
    if winner == ai_symbol:
        return 10 - depth  # Prefer faster wins
    if winner == opponent_symbol:
        return depth - 10  # Prefer slower losses
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
```

### Why Minimax is Unbeatable
- Explores all possible game states
- Assumes optimal play from both players
- Tic Tac Toe has a small state space (only 9 cells)
- With perfect play, the best the opponent can achieve is a draw

### Optimization Notes
- The current implementation is sufficient for Tic Tac Toe due to the small board size
- For larger games, alpha-beta pruning would be added to reduce the search space
- Position evaluation heuristics could be added for more complex games

## 🎨 Customization

### Changing Colors
Edit `styles.css` and modify the CSS variables in the `:root` section:
```css
:root {
    --bg-primary: #0a0e1a;
    --accent-blue: #00d4ff;
    --accent-purple: #a855f7;
    --accent-cyan: #22d3ee;
    /* ... */
}
```

### Adding Sound Effects
Place your audio files in the `assets/sounds/` directory:
- `click.mp3` - Button click sound
- `move.mp3` - Move placement sound
- `win.mp3` - Victory sound
- `draw.mp3` - Draw notification sound

### Modifying AI Behavior
Edit `ai_engine.py` to adjust:
- Easy mode randomness
- Medium mode strategy percentages
- Hard mode (already optimal with Minimax)

## 🧪 Testing

### Manual Testing Checklist
- [ ] Player vs Player mode works correctly
- [ ] Player vs Computer Easy mode makes random moves
- [ ] Player vs Computer Medium mode uses strategy
- [ ] Player vs Computer Hard mode is unbeatable
- [ ] Win detection works for all combinations
- [ ] Draw detection works correctly
- [ ] Scoreboard updates accurately
- [ ] Game history displays correctly
- [ ] Reset functionality works
- [ ] Responsive design on mobile/tablet/desktop

### Test Scenarios
1. **Win Conditions**: Test all 8 winning combinations
2. **Draw Condition**: Fill board without a winner
3. **AI Behavior**: Test each difficulty level
4. **Score Persistence**: Verify scores persist across games
5. **Settings Changes**: Test changing modes and difficulty mid-game

## 📝 Code Architecture

### game_logic.py
- `TicTacToeGame`: Core game state management
- `Scoreboard`: Score tracking and history management

### ai_engine.py
- `AIEngine`: AI opponent with multiple difficulty levels
- Minimax algorithm implementation
- Strategic move evaluation

### app.py
- Streamlit application setup
- UI rendering functions
- Session state management
- Event handling

### styles.css
- Custom styling for all UI elements
- Animations and transitions
- Responsive design rules
- Glassmorphism effects

## 🐛 Troubleshooting

### Application won't start
- Ensure Python 3.11+ is installed
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check that you're in the correct directory

### Styling not appearing
- Ensure `styles.css` is in the same directory as `app.py`
- Clear browser cache
- Restart the Streamlit server

### AI not responding
- Check that `ai_engine.py` is present
- Verify difficulty setting in sidebar
- Try restarting the game

## 🚀 Future Enhancements

Potential features for future versions:
- Multiplayer online mode
- Leaderboard system
- Additional board sizes (4x4, 5x5)
- Tournament mode
- Achievement system
- Sound effects integration
- Animated winning line
- Player profiles
- Game replay system

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📧 Contact

For questions or feedback, please open an issue on the repository.

---

**Built with ❤️ using Python and Streamlit**

Enjoy the ultimate Tic Tac Toe gaming experience! 🎮✨
