import random
import webbrowser
import tkinter as tk
from tkinter import messagebox

# Tic Tac Toe Game original variables
symbolP1 = "X"
symbolP2 = "O"

gameMatrix = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

validVals = (1, 2, 3)

def matrixChecker(matrix):
    WinTest = []
    # Row Test
    if matrix[0][0] != " " and matrix[0][0] == matrix[0][1] and matrix[0][1] == matrix[0][2]: 
        WinTest.append(True)
    if matrix[1][0] != " " and matrix[1][0] == matrix[1][1] and matrix[1][1] == matrix[1][2]: 
        WinTest.append(True)
    if matrix[2][0] != " " and matrix[2][0] == matrix[2][1] and matrix[2][1] == matrix[2][2]:
        WinTest.append(True)
    
    # Column Test
    if matrix[0][0] != " " and matrix[0][0] == matrix[1][0] and matrix[1][0] == matrix[2][0]: 
        WinTest.append(True)
    if matrix[0][1] != " " and matrix[0][1] == matrix[1][1] and matrix[1][1] == matrix[2][1]: 
        WinTest.append(True)
    if matrix[0][2] != " " and matrix[0][2] == matrix[1][2] and matrix[1][2] == matrix[2][2]: 
        WinTest.append(True)
    
    # Diagonal Test
    if matrix[0][0] != " " and matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]: 
        WinTest.append(True)
    if matrix[2][0] != " " and matrix[2][0] == matrix[1][1] and matrix[1][1] == matrix[0][2]: 
        WinTest.append(True)
    return WinTest

# Unused original input validation functions, preserved to maintain codebase patterns
def rowInpValFunc():
    try:
        rowInp = int(input("Type the row value : "))
        if rowInp not in validVals:
            raise Exception("Type a valid value.")
    except Exception:
        print("Type a valid integer value in [1,3] ")
        rowInp = int(input("Type the row value : "))
    return rowInp

def columnInpValFunc():
    try:
        columnInp = int(input("Type the column value : "))
        if columnInp not in validVals:
            raise Exception("Type a valid value.")
    except Exception:
        print("Type a valid integer value in [1,3] ")
        columnInp = int(input("Type the column value : "))
    return columnInp

def rndRow():
    rowVal = random.randint(0, 2)
    return rowVal

def rndCol():
    colVal = random.randint(0, 2)
    return colVal

# Turn count tracker
loopCntVal = 0
game_over = False

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe Game")
        self.root.geometry("460x640")
        self.root.configure(bg="#1E1E2E")
        self.root.resizable(False, False)

        # Style colors
        self.bg_color = "#1E1E2E"
        self.grid_bg = "#11111B"
        self.btn_bg = "#313244"
        self.btn_active_bg = "#45475A"
        self.fg_color = "#CDD6F4"
        self.p1_color = "#89B4FA"  # Neon blue for X
        self.p2_color = "#F38BA8"  # Soft red/coral for O
        self.accent_color = "#A6E3A1" # Pastel Green for reset/win
        
        # Game mode variable
        self.vs_bot = tk.BooleanVar(value=False)

        # Create smart menu bar
        self.setup_menu()

        # Build UI layout
        self.create_widgets()

    def setup_menu(self):
        self.menubar = tk.Menu(self.root)
        
        # Define menu configuration structure
        menu_structure = {
            "Links": [
                ("Github", "https://github.com/AS-Developer-17/Tic-Tac-Toe-Game"),
                ("About Us", "https://as-developerportfolio.web.app/")
            ]
        }
        
        # Smartly generate menu
        for menu_title, items in menu_structure.items():
            sub_menu = tk.Menu(self.menubar, tearoff=0)
            for label, url in items:
                # Default parameter value binds the url correctly at loop execution time
                sub_menu.add_command(label=label, command=lambda u=url: webbrowser.open_new_tab(u))
            self.menubar.add_cascade(label=menu_title, menu=sub_menu)
            
        self.root.config(menu=self.menubar)

    def create_widgets(self):
        # Title Label
        title_text = "Welcome to AS.Developer's\nTic Tac Toe Game"
        self.title_label = tk.Label(
            self.root, 
            text=title_text, 
            font=("Segoe UI", 16, "bold"), 
            bg=self.bg_color, 
            fg=self.accent_color,
            justify="center",
            pady=10
        )
        self.title_label.pack(fill="x")

        # Mode Selection Frame
        self.mode_frame = tk.Frame(self.root, bg=self.bg_color)
        self.mode_frame.pack(pady=5)

        self.pvp_radio = tk.Radiobutton(
            self.mode_frame,
            text="2 Players (Local)",
            variable=self.vs_bot,
            value=False,
            font=("Segoe UI", 10, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
            selectcolor=self.bg_color,
            activebackground=self.bg_color,
            activeforeground=self.accent_color,
            command=self.reset_game
        )
        self.pvp_radio.pack(side="left", padx=15)

        self.bot_radio = tk.Radiobutton(
            self.mode_frame,
            text="Play vs Bot",
            variable=self.vs_bot,
            value=True,
            font=("Segoe UI", 10, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
            selectcolor=self.bg_color,
            activebackground=self.bg_color,
            activeforeground=self.accent_color,
            command=self.reset_game
        )
        self.bot_radio.pack(side="left", padx=15)

        # Info/Status Label
        self.status_label = tk.Label(
            self.root,
            text="Player 1 Turn (X)",
            font=("Segoe UI", 12, "bold"),
            bg=self.bg_color,
            fg=self.p1_color,
            pady=10
        )
        self.status_label.pack()

        # Grid Container
        self.grid_frame = tk.Frame(self.root, bg=self.grid_bg, padx=2, pady=2, bd=2)
        self.grid_frame.pack(padx=20, pady=10)

        # Buttons array
        self.buttons = []
        for r in range(3):
            row_buttons = []
            for c in range(3):
                btn = tk.Button(
                    self.grid_frame,
                    text=" ",
                    font=("Segoe UI", 28, "bold"),
                    width=5,
                    height=2,
                    bg=self.btn_bg,
                    fg=self.fg_color,
                    activebackground=self.btn_active_bg,
                    activeforeground=self.fg_color,
                    bd=0,
                    cursor="hand2",
                    command=lambda row=r, col=c: self.on_cell_click(row, col)
                )
                btn.grid(row=r, column=c, padx=3, pady=3)
                # Simple hover effects
                btn.bind("<Enter>", lambda e, b=btn: self.on_hover_enter(b))
                btn.bind("<Leave>", lambda e, b=btn: self.on_hover_leave(b))
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

        # Control Panel (Reset Button)
        self.reset_button = tk.Button(
            self.root,
            text="Restart Game",
            font=("Segoe UI", 12, "bold"),
            bg=self.btn_bg,
            fg=self.accent_color,
            activebackground=self.accent_color,
            activeforeground=self.bg_color,
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.reset_game
        )
        self.reset_button.pack(pady=(20, 10))

        # Bottom padding spacing
        self.bottom_padding = tk.Frame(self.root, bg=self.bg_color, height=30)
        self.bottom_padding.pack(fill="x", side="bottom")

    def on_hover_enter(self, btn):
        if btn["text"] == " " and not game_over:
            btn.configure(bg=self.btn_active_bg)

    def on_hover_leave(self, btn):
        if btn["text"] == " " and not game_over:
            btn.configure(bg=self.btn_bg)

    def on_cell_click(self, r, c):
        global loopCntVal, game_over

        if game_over:
            return

        # Player 1 or Player 2 turn coordinates setup
        # Keeps original variable names to align with command line variables
        if loopCntVal % 2 == 0:
            player1Row = r + 1
            player1Col = c + 1
            selected_row, selected_col = player1Row - 1, player1Col - 1
            current_symbol = symbolP1
        else:
            player2Row = r + 1
            player2Col = c + 1
            selected_row, selected_col = player2Row - 1, player2Col - 1
            current_symbol = symbolP2

        # Check if cell is occupied
        if gameMatrix[selected_row][selected_col] != " ":
            messagebox.showwarning(
                "Already Equipped",
                "This combination is already equipped\nYou loose your chance to play."
            )
            # Increment turn (user loses turn as per original logic)
            loopCntVal += 1
            self.check_game_state()
            if not game_over and self.vs_bot.get() and loopCntVal % 2 == 1:
                # Let bot take turn if vs Bot mode is active
                self.root.after(500, self.bot_turn)
            return

        # Set gameMatrix and update UI
        gameMatrix[selected_row][selected_col] = current_symbol
        self.update_grid_ui()

        # Increment turn count
        loopCntVal += 1

        # Check state after move
        self.check_game_state()

        # If it is now Bot's turn and vs Bot is enabled, perform Bot move
        if not game_over and self.vs_bot.get() and loopCntVal % 2 == 1:
            self.root.after(500, self.bot_turn)

    def bot_turn(self):
        global loopCntVal, game_over
        if game_over:
            return

        # Bot logic ported directly from original elif loopCntVal%2==23423421: block
        botRow = rndRow()
        botCol = rndCol()

        if gameMatrix[botRow][botCol] == " ":
            gameMatrix[botRow][botCol] = symbolP2
        else:
            while gameMatrix[botRow][botCol] != " ":
                botRow = rndRow()
                botCol = rndCol()
            gameMatrix[botRow][botCol] = symbolP2

        self.update_grid_ui()
        loopCntVal += 1
        self.check_game_state()

    def update_grid_ui(self):
        for r in range(3):
            for c in range(3):
                val = gameMatrix[r][c]
                self.buttons[r][c].configure(text=val)
                if val == symbolP1:
                    self.buttons[r][c].configure(fg=self.p1_color, disabledforeground=self.p1_color, bg=self.btn_bg)
                elif val == symbolP2:
                    self.buttons[r][c].configure(fg=self.p2_color, disabledforeground=self.p2_color, bg=self.btn_bg)
                else:
                    self.buttons[r][c].configure(fg=self.fg_color, bg=self.btn_bg)

    def check_game_state(self):
        global game_over, loopCntVal
        
        # Check winner
        winnerCheck = matrixChecker(gameMatrix)
        
        if True in winnerCheck:
            game_over = True
            # Determine who won based on whose turn just finished
            # (Note: loopCntVal was incremented after the move)
            if loopCntVal % 2 == 1:
                winner_text = "The winner is : Player 1"
                self.status_label.configure(text=winner_text, fg=self.p1_color)
                self.disable_all_cells()
                if messagebox.askyesno("Game Over", f"{winner_text}\n\nDo you want to start a new game?"):
                    self.reset_game()
            else:
                winner_text = "The winner is : Player 2"
                self.status_label.configure(text=winner_text, fg=self.p2_color)
                self.disable_all_cells()
                if messagebox.askyesno("Game Over", f"{winner_text}\n\nDo you want to start a new game?"):
                    self.reset_game()
            return

        # Check Draw
        # Corrected syntax from: " " not in gameMatrix[0] ... and True not in winnerCheck()
        is_draw = " " not in gameMatrix[0] and " " not in gameMatrix[1] and " " not in gameMatrix[2]
        if is_draw:
            game_over = True
            draw_text = "It is draw \nno one WON."
            self.status_label.configure(text=draw_text, fg=self.fg_color)
            self.disable_all_cells()
            if messagebox.askyesno("Game Over", "It is draw, no one WON.\n\nDo you want to start a new game?"):
                self.reset_game()
            return

        # Update turn status label for next turn
        if loopCntVal % 2 == 0:
            self.status_label.configure(text="Player 1 Turn (X)", fg=self.p1_color)
        else:
            self.status_label.configure(text="Player 2 Turn (O)" if not self.vs_bot.get() else "Bot's Turn (O)", fg=self.p2_color)

    def disable_all_cells(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].configure(state="disabled")

    def reset_game(self):
        global gameMatrix, loopCntVal, game_over
        gameMatrix = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
        loopCntVal = 0
        game_over = False

        # Reset button states and texts
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].configure(state="normal", text=" ", bg=self.btn_bg, fg=self.fg_color)
        
        self.status_label.configure(text="Player 1 Turn (X)", fg=self.p1_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
