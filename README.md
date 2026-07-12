# Tic-Tac-Toe Game

A classic Tic-Tac-Toe game implementation in Python featuring both a standard command-line interface and a modern, premium Tkinter desktop GUI.

---

## Game Versions

### 1. Tkinter GUI Version (`TicTacToeTkinter.py`)
A feature-rich desktop application built with a modern dark theme and custom animations/layouts.

- **Vibrant Aesthetics**: Custom slate/navy palette (`#1E1E2E`) with distinct colors for Player symbols (`X` is neon blue, `O` is coral red).
- **Play Modes**: 
  - **2 Players (Local)**: Local turn-based multiplayer.
  - **Play vs Bot**: Play against an AI opponent utilizing a random slot picker loop.
- **Smart Menubar**: Embedded links that dynamically open external URLs:
  - **GitHub Repository**
  - **Developer Portfolio**
- **Intuitive Restart & Game Loop**: Prompts you automatically when the game ends to start a new round or lets you reset anytime via the restart button.
- **Wasted Turn mechanic**: Faithfully preserves the original CLI rule where selecting an occupied square wastes the current player's turn.

### 2. CLI Version (`TicTacToe.py`)
A classic command-line implementation for terminal gameplay.

- Two-player turn-based gameplay.
- Input validation and exception handling for cell selections.

---

## Requirements

- Python 3.6 or higher
- Tkinter library (typically bundled standard with Python installations)

---

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AS-Developer-17/Tic-Tac-Toe-Game.git
   cd Tic-Tac-Toe-Game
   ```

2. **Run your preferred version**:

   - **For GUI Version**:
     ```bash
     python TicTacToeTkinter.py
     ```

   - **For CLI Version**:
     ```bash
     python TicTacToe.py
     ```

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
