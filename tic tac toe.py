import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        self.player = "X"
        self.ai = "O"
        self.board = [""] * 9
        self.buttons = []

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Tic Tac Toe", font=("Arial", 24))
        title.grid(row=0, column=0, columnspan=3, pady=10)

        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2,
                               command=lambda idx=i: self.player_move(idx))
            button.grid(row=(i // 3) + 1, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

    def player_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.check_winner(self.player):
                messagebox.showinfo("Game Over", "You Win!")
                self.reset_game()
            else:
                if "" not in self.board:
                    messagebox.showinfo("Game Over", "It's a Draw!")
                    self.reset_game()
                else:
                    self.ai_move()

    def ai_move(self):
        move = self.best_move()
        self.board[move] = self.ai
        self.buttons[move].config(text=self.ai)
        if self.check_winner(self.ai):
            messagebox.showinfo("Game Over", "AI Wins!")
            self.reset_game()
        elif "" not in self.board:
            messagebox.showinfo("Game Over", "It's a Draw!")
            self.reset_game()

    def best_move(self):
        # Check for winning move
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.ai
                if self.check_winner(self.ai):
                    return i
                self.board[i] = ""

        # Check for blocking move
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.player
                if self.check_winner(self.player):
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        # Choose a random corner if available
        corners = [0, 2, 6, 8]
        available_corners = [i for i in corners if self.board[i] == ""]
        if available_corners:
            return available_corners[0]

        # Choose the center if available
        if self.board[4] == "":
            return 4

        # Choose a random side if available
        sides = [1, 3, 5, 7]
        available_sides = [i for i in sides if self.board[i] == ""]
        if available_sides:
            return available_sides[0]

        # Fallback to a random move
        return self.random_move()

    def random_move(self):
        available_moves = [i for i in range(9) if self.board[i] == ""]
        return available_moves[0] if available_moves else None

    def check_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        return any(all(self.board[i] == player for i in combo) for combo in winning_combinations)

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
