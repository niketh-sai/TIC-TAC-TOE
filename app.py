"""
Tic Tac Toe - Premium Gaming Experience
A modern, visually appealing Tic Tac Toe game with multiple game modes and AI difficulty levels
"""

import streamlit as st
import numpy as np
from game_logic import TicTacToeGame, Scoreboard
from ai_engine import AIEngine
import time


# Page configuration
st.set_page_config(
    page_title="Tic Tac Toe - Premium Gaming",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    with open("styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()


# Initialize session state
def initialize_session_state():
    """Initialize all session state variables"""
    if 'game_started' not in st.session_state:
        st.session_state.game_started = False
    if 'game_mode' not in st.session_state:
        st.session_state.game_mode = 'pvp'
    if 'difficulty' not in st.session_state:
        st.session_state.difficulty = 'medium'
    if 'player_symbol' not in st.session_state:
        st.session_state.player_symbol = 'X'
    if 'computer_symbol' not in st.session_state:
        st.session_state.computer_symbol = 'O'
    if 'sound_enabled' not in st.session_state:
        st.session_state.sound_enabled = True
    if 'game' not in st.session_state:
        st.session_state.game = TicTacToeGame()
    if 'scoreboard' not in st.session_state:
        st.session_state.scoreboard = Scoreboard()
    if 'show_landing' not in st.session_state:
        st.session_state.show_landing = True


initialize_session_state()


# Landing Page
def render_landing_page():
    """Render the landing/start page"""
    st.markdown("""
        <div class="landing-container fade-in">
            <div class="landing-logo">TIC TAC TOE</div>
            <div class="landing-subtitle">The Ultimate Strategy Challenge</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Game Mode Selection
        st.markdown('<h3 style="font-family: Orbitron; color: var(--accent-cyan); margin-bottom: 1rem;">SELECT GAME MODE</h3>', 
                   unsafe_allow_html=True)
        
        game_mode = st.radio(
            "Game Mode",
            ["Player vs Player", "Player vs Computer"],
            label_visibility="collapsed",
            key="landing_game_mode"
        )
        
        # Difficulty Selection (only for PvC)
        if game_mode == "Player vs Computer":
            st.markdown('<h3 style="font-family: Orbitron; color: var(--accent-cyan); margin-top: 1.5rem; margin-bottom: 1rem;">SELECT DIFFICULTY</h3>', 
                       unsafe_allow_html=True)
            
            difficulty = st.selectbox(
                "Difficulty",
                ["Easy", "Medium", "Hard"],
                label_visibility="collapsed",
                key="landing_difficulty"
            )
            
            # Player Symbol Selection
            st.markdown('<h3 style="font-family: Orbitron; color: var(--accent-cyan); margin-top: 1.5rem; margin-bottom: 1rem;">CHOOSE YOUR SYMBOL</h3>', 
                       unsafe_allow_html=True)
            
            player_symbol = st.radio(
                "Symbol",
                ["X", "O"],
                label_visibility="collapsed",
                key="landing_symbol"
            )
        else:
            difficulty = "medium"
            player_symbol = "X"
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Start Button
        if st.button("START GAME", key="start_button", use_container_width=True):
            st.session_state.game_mode = 'pvp' if game_mode == "Player vs Player" else 'pvc'
            st.session_state.difficulty = difficulty.lower()
            st.session_state.player_symbol = player_symbol
            st.session_state.computer_symbol = 'O' if player_symbol == 'X' else 'X'
            st.session_state.game_started = True
            st.session_state.show_landing = False
            st.session_state.game.initialize_game()
            st.rerun()


# Game Board Rendering
def render_board():
    """Render the interactive game board"""
    game = st.session_state.game
    board = game.board
    
    # Center the board with columns
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Create 3 rows, each with 3 columns
        for row in range(3):
            cols = st.columns([1, 1, 1], gap="small")
            
            for col_idx in range(3):
                cell_idx = row * 3 + col_idx
                cell_content = board[cell_idx] if board[cell_idx] != " " else ""
                
                with cols[col_idx]:
                    # Use a unique key for each button
                    button_key = f"cell_{cell_idx}"
                    
                    # Wrap button in a div for styling
                    cell_color = "#00d4ff" if board[cell_idx] == "X" else "#a855f7" if board[cell_idx] == "O" else "var(--text-primary)"
                    text_shadow = "0 0 20px rgba(0, 212, 255, 0.8)" if board[cell_idx] == "X" else "0 0 20px rgba(168, 85, 247, 0.8)" if board[cell_idx] == "O" else "none"
                    
                    st.markdown(
                        f'''
                        <style>
                        div[data-testid="stVerticalBlock"] > div > div > div > button[data-testid="baseButton-primary"][key="{button_key}"] {{
                            aspect-ratio: 1 !important;
                            min-height: 120px !important;
                            height: 120px !important;
                            max-height: 120px !important;
                            background: rgba(17, 24, 39, 0.6) !important;
                            border: 2px solid var(--glass-border) !important;
                            border-radius: 15px !important;
                            font-family: 'Orbitron', sans-serif !important;
                            font-size: 3rem !important;
                            font-weight: 700 !important;
                            color: {cell_color} !important;
                            text-shadow: {text_shadow} !important;
                            line-height: 1 !important;
                            padding: 0 !important;
                            transition: all 0.3s ease !important;
                            display: flex !important;
                            align-items: center !important;
                            justify-content: center !important;
                            white-space: nowrap !important;
                        }}
                        div[data-testid="stVerticalBlock"] > div > div > div > button[data-testid="baseButton-primary"][key="{button_key}"]:hover:not(:disabled) {{
                            background: rgba(0, 212, 255, 0.1) !important;
                            border-color: var(--accent-blue) !important;
                            box-shadow: var(--glow-blue) !important;
                            transform: scale(1.02) !important;
                        }}
                        </style>
                        ''',
                        unsafe_allow_html=True
                    )
                    
                    if st.button(
                        cell_content,
                        key=button_key,
                        use_container_width=True,
                        disabled=board[cell_idx] != " " or game.game_over
                    ):
                        handle_cell_click(cell_idx)


# Handle Cell Click
def handle_cell_click(position):
    """Handle player's move"""
    game = st.session_state.game
    
    if not game.is_valid_move(position):
        return
    
    # Player's move
    current_player = game.current_player
    
    # In PvC mode, ensure human player is making the move
    if st.session_state.game_mode == 'pvc':
        if current_player != st.session_state.player_symbol:
            return
    
    game.make_move(position, current_player)
    
    # Check if game ended
    if game.game_over:
        update_scoreboard()
        return
    
    # Computer's move in PvC mode
    if st.session_state.game_mode == 'pvc' and not game.game_over:
        if game.current_player == st.session_state.computer_symbol:
            st.rerun()


# Computer Move
def make_computer_move():
    """Make computer's move in PvC mode"""
    game = st.session_state.game
    
    if game.game_over:
        return
    
    if game.current_player != st.session_state.computer_symbol:
        return
    
    ai = AIEngine(st.session_state.difficulty)
    position = ai.make_move(game.board, st.session_state.computer_symbol)
    
    if position != -1:
        game.make_move(position, st.session_state.computer_symbol)
        
        if game.game_over:
            update_scoreboard()


# Update Scoreboard
def update_scoreboard():
    """Update scoreboard after game ends"""
    game = st.session_state.game
    scoreboard = st.session_state.scoreboard
    
    if game.winner:
        if st.session_state.game_mode == 'pvc':
            winner = "Computer" if game.winner == st.session_state.computer_symbol else game.winner
        else:
            winner = game.winner
        scoreboard.update_score(winner)
    elif game.draw:
        scoreboard.update_score("Draw", is_draw=True)


# Render Dashboard/Scoreboard
def render_dashboard():
    """Render the scoreboard dashboard"""
    scoreboard = st.session_state.scoreboard
    scores = scoreboard.get_scores()
    
    st.markdown('<h2 style="font-family: Orbitron; color: var(--accent-cyan); text-align: center; margin-bottom: 1.5rem;">SCOREBOARD</h2>', 
               unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f"""
            <div class="dashboard-card">
                <div class="score-value">{scores['X']}</div>
                <div class="score-label">Player X</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="dashboard-card">
                <div class="score-value">{scores['O']}</div>
                <div class="score-label">Player O</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if st.session_state.game_mode == 'pvc':
            st.markdown(f"""
                <div class="dashboard-card">
                    <div class="score-value">{scores['Computer']}</div>
                    <div class="score-label">Computer</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="dashboard-card">
                    <div class="score-value">-</div>
                    <div class="score-label">Computer</div>
                </div>
            """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
            <div class="dashboard-card">
                <div class="score-value">{scores['Draw']}</div>
                <div class="score-label">Draws</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown(f"""
            <div class="dashboard-card">
                <div class="score-value">{scores['Total']}</div>
                <div class="score-label">Total</div>
            </div>
        """, unsafe_allow_html=True)


# Render Game History
def render_history():
    """Render game history"""
    scoreboard = st.session_state.scoreboard
    history = scoreboard.get_history()
    
    if not history:
        return
    
    st.markdown('<h3 style="font-family: Orbitron; color: var(--accent-cyan); margin-top: 2rem; margin-bottom: 1rem;">GAME HISTORY</h3>', 
               unsafe_allow_html=True)
    
    for match in reversed(history[-10:]):  # Show last 10 matches
        winner_class = ""
        if match['winner']:
            winner_class = f"winner-{match['winner'].lower()}"
        else:
            winner_class = "winner-draw"
        
        st.markdown(f"""
            <div class="history-item">
                <span class="history-match">Match #{match['match']}</span>
                <span class="history-result">{match['result']}</span>
                <span class="history-winner {winner_class}">{match['winner'] if match['winner'] else 'Draw'}</span>
            </div>
        """, unsafe_allow_html=True)


# Render Settings Panel
def render_settings():
    """Render settings panel in sidebar"""
    st.markdown('<div class="settings-panel">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">SETTINGS</div>', unsafe_allow_html=True)
    
    # Sound Toggle
    st.session_state.sound_enabled = st.checkbox(
        "Sound Effects",
        value=st.session_state.sound_enabled,
        key="sound_toggle"
    )
    
    # Game Mode Change
    new_mode = st.selectbox(
        "Game Mode",
        ["Player vs Player", "Player vs Computer"],
        index=0 if st.session_state.game_mode == 'pvp' else 1
    )
    
    if new_mode != ("Player vs Player" if st.session_state.game_mode == 'pvp' else "Player vs Computer"):
        st.session_state.game_mode = 'pvp' if new_mode == "Player vs Player" else 'pvc'
        st.session_state.game.initialize_game()
        st.rerun()
    
    # Difficulty Change (only for PvC)
    if st.session_state.game_mode == 'pvc':
        new_difficulty = st.selectbox(
            "AI Difficulty",
            ["Easy", "Medium", "Hard"],
            index=["easy", "medium", "hard"].index(st.session_state.difficulty)
        )
        
        if new_difficulty.lower() != st.session_state.difficulty:
            st.session_state.difficulty = new_difficulty.lower()
            st.session_state.game.initialize_game()
            st.rerun()
        
        # Player Symbol Change
        new_symbol = st.selectbox(
            "Your Symbol",
            ["X", "O"],
            index=0 if st.session_state.player_symbol == 'X' else 1
        )
        
        if new_symbol != st.session_state.player_symbol:
            st.session_state.player_symbol = new_symbol
            st.session_state.computer_symbol = 'O' if new_symbol == 'X' else 'X'
            st.session_state.game.initialize_game()
            st.rerun()
    
    # Reset Scores
    if st.button("Reset Scores", use_container_width=True):
        st.session_state.scoreboard.reset_scores()
        st.rerun()
    
    # Back to Landing
    if st.button("Back to Menu", use_container_width=True):
        st.session_state.show_landing = True
        st.session_state.game_started = False
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)


# Main Game Page
def render_game_page():
    """Render the main game page"""
    game = st.session_state.game
    
    # Title
    st.markdown("""
        <div class="game-title">TIC TAC TOE</div>
        <div class="game-subtitle">The Ultimate Strategy Challenge</div>
    """, unsafe_allow_html=True)
    
    # Turn Indicator
    if not game.game_over:
        turn_class = f"turn-{game.current_player.lower()}"
        mode_text = "Player" if st.session_state.game_mode == 'pvp' else "Your"
        if st.session_state.game_mode == 'pvc' and game.current_player == st.session_state.computer_symbol:
            mode_text = "Computer's"
        
        st.markdown(f"""
            <div class="turn-indicator {turn_class}">
                {mode_text} Turn ({game.current_player})
            </div>
        """, unsafe_allow_html=True)
    
    # Game Board
    render_board()
    
    # Computer Move (if it's computer's turn)
    if st.session_state.game_mode == 'pvc' and not game.game_over:
        if game.current_player == st.session_state.computer_symbol:
            time.sleep(0.5)  # Small delay for realism
            make_computer_move()
            st.rerun()
    
    # Game Over Message
    if game.game_over:
        if game.winner:
            winner_text = game.winner
            if st.session_state.game_mode == 'pvc':
                if game.winner == st.session_state.computer_symbol:
                    winner_text = "Computer"
                else:
                    winner_text = "You"
            
            st.markdown(f"""
                <div class="status-message status-win victory-animation">
                    🎉 {winner_text} Win! 🎉
                </div>
            """, unsafe_allow_html=True)
        elif game.draw:
            st.markdown(f"""
                <div class="status-message status-draw">
                    🤝 It's a Draw! 🤝
                </div>
            """, unsafe_allow_html=True)
        
        # Action Buttons
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("PLAY AGAIN", key="play_again", use_container_width=True):
                game.initialize_game()
                st.rerun()
            
            if st.button("NEW GAME", key="new_game", use_container_width=True):
                st.session_state.game.initialize_game()
                st.session_state.scoreboard.reset_scores()
                st.rerun()
    
    # Dashboard
    render_dashboard()
    
    # History
    render_history()


# Sidebar
def render_sidebar():
    """Render sidebar with settings"""
    with st.sidebar:
        render_settings()


# Main App
def main():
    """Main application logic"""
    
    # Render sidebar
    render_sidebar()
    
    # Render landing page or game page
    if st.session_state.show_landing:
        render_landing_page()
    else:
        render_game_page()


if __name__ == "__main__":
    main()
