import tkinter as tk
import random
import math

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.board = [" " for _ in range(9)]  # 3x3 board
        self.difficulty = tk.StringVar(value="medium")  # Default difficulty
        self.mode = tk.StringVar(value="AI")  # Default mode (AI or Multiplayer)
        self.current_player = "X"  # Track current player in multiplayer mode
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create buttons and UI elements"""
        self.buttons = []
        
        # Mode selection
        tk.Label(self.root, text="Select Mode:").grid(row=0, column=0, columnspan=3)
        tk.Radiobutton(self.root, text="AI", variable=self.mode, value="AI").grid(row=0, column=3)
        tk.Radiobutton(self.root, text="Multiplayer", variable=self.mode, value="Multiplayer").grid(row=0, column=4)
        
        # Difficulty selection
        tk.Label(self.root, text="Select Difficulty:").grid(row=1, column=0, columnspan=3)
        for i, level in enumerate(["easy", "medium", "hard"]):
            tk.Radiobutton(self.root, text=level.capitalize(), variable=self.difficulty, value=level).grid(row=1, column=i+3)
        
        # Game Board
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text=" ", font=("Arial", 20), height=2, width=5,
                                command=lambda i=i, j=j: self.make_move(i * 3 + j))
                btn.grid(row=i+2, column=j)
                self.buttons.append(btn)
        
        # Status Label
        self.status_label = tk.Label(self.root, text="Your Turn!", font=("Arial", 12))
        self.status_label.grid(row=5, column=0, columnspan=3)
        
        # Reset Button
        tk.Button(self.root, text="Restart", font=("Arial", 12), command=self.reset_game).grid(row=5, column=3, columnspan=3)
    
    def make_move(self, index):
        """Handles player and AI moves"""
        if self.board[index] == " " and not self.is_game_over():
            if self.mode.get() == "Multiplayer":
                self.board[index] = self.current_player
                self.buttons[index].config(text=self.current_player, state=tk.DISABLED)
                if not self.check_winner():
                    self.current_player = "O" if self.current_player == "X" else "X"
                    self.status_label.config(text=f"Player {self.current_player}'s Turn")
            else:
                self.board[index] = "X"
                self.buttons[index].config(text="X", state=tk.DISABLED)
                if not self.check_winner():
                    self.ai_move()
    
    def ai_move(self):
        """Handles AI move based on selected difficulty"""
        if self.is_game_over():
            return
        
        index = self.get_best_move()
        self.board[index] = "O"
        self.buttons[index].config(text="O", state=tk.DISABLED)
        self.check_winner()
    
    def get_best_move(self):
        """AI chooses move based on difficulty"""
        empty_cells = [i for i in range(9) if self.board[i] == " "]
        
        if self.difficulty.get() == "easy":
            return random.choice(empty_cells)
        elif self.difficulty.get() == "medium":
            return random.choice(empty_cells) if random.random() < 0.5 else self.minimax_best_move()
        return self.minimax_best_move()
    
    def minimax_best_move(self):
        """Finds the best move using Minimax"""
        best_score = -math.inf
        move = -1
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    move = i
        return move
    
    def minimax(self, is_maximizing):
        """Minimax algorithm for AI decision-making"""
        if self.is_winner("O"): return 1
        if self.is_winner("X"): return -1
        if self.is_draw(): return 0
        
        best_score = -math.inf if is_maximizing else math.inf
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O" if is_maximizing else "X"
                score = self.minimax(not is_maximizing)
                self.board[i] = " "
                best_score = max(best_score, score) if is_maximizing else min(best_score, score)
        return best_score
    
    def check_winner(self):
        """Check if there is a winner or draw"""
        for player in ["X", "O"]:
            if self.is_winner(player):
                self.status_label.config(text=f"{player} Wins! 🎉")
                self.disable_buttons()
                return True
        
        if self.is_draw():
            self.status_label.config(text="It's a Draw! 😐")
            return True
        
        return False
    
    def is_winner(self, player):
        """Check if a player has won"""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(self.board[pos] == player for pos in condition) for condition in win_conditions)
    
    def is_draw(self):
        """Check if the game is a draw"""
        return " " not in self.board
    
    def is_game_over(self):
        """Check if the game is over"""
        return self.is_winner("X") or self.is_winner("O") or self.is_draw()
    
    def disable_buttons(self):
        """Disable all buttons after game over"""
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)
    
    def reset_game(self):
        """Reset the game board"""
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        for btn in self.buttons:
            btn.config(text=" ", state=tk.NORMAL)
        self.status_label.config(text="Your Turn!")
        
# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
