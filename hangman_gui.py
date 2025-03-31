import random
import tkinter as tk
from tkinter import messagebox

# Word list
WORDS = ["python", "developer", "hangman", "programming", "challenge", "computer", "artificial", "machine",
         "learning", "intelligence", "network", "security", "database", "cybersecurity", "framework", "software"]

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
    =========
    """
]


class HangmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game 🎭")
        self.root.geometry("600x600")
        self.root.config(bg="#f7f7f7")

        # Initialize game variables
        self.word = ""
        self.word_display = []
        self.attempts = 0
        self.guessed_letters = set()
        self.players = ["Player 1", "Player 2"]
        self.current_player = 0

        # Mode Selection
        self.mode = tk.StringVar()
        self.mode.set("single_attempts")

        self.create_welcome_screen()

    def create_welcome_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Welcome to Hangman!", font=("Arial", 20, "bold"), fg="#3b5998", bg="#f7f7f7").pack(
            pady=10)

        tk.Radiobutton(self.root, text="Multiplayer - 2 Players (6 Attempts Each)", variable=self.mode,
                       value="multiplayer", bg="#f7f7f7").pack()
        tk.Radiobutton(self.root, text="Single Player - 6 Attempts", variable=self.mode, value="single_attempts",
                       bg="#f7f7f7").pack()
        tk.Radiobutton(self.root, text="Single Player - Unlimited Attempts", variable=self.mode,
                       value="single_no_attempts", bg="#f7f7f7").pack()

        tk.Button(self.root, text="Start Game", font=("Arial", 14), bg="#a8d5e2", fg="#333", padx=20, pady=5,
                  command=self.start_game).pack(pady=20)

    def start_game(self):
        self.new_game()

    def new_game(self):
        self.word = random.choice(WORDS).lower()
        self.word_display = ["_"] * len(self.word)
        self.attempts = 6 if self.mode.get() in ["single_attempts", "multiplayer"] else float("inf")
        self.guessed_letters = set()
        self.current_player = 0  # Reset to Player 1
        self.create_game_ui()

    def create_game_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"{self.players[self.current_player]}'s Turn", font=("Arial", 14, "bold"),
                 bg="#f7f7f7").pack(pady=10)

        self.hangman_label = tk.Label(self.root,
                                      text=HANGMAN_STAGES[min(6, 6 - self.attempts)] if self.attempts != float(
                                          "inf") else HANGMAN_STAGES[0], font=("Courier", 14), bg="#f7f7f7")
        self.hangman_label.pack()

        self.word_label = tk.Label(self.root, text=" ".join(self.word_display), font=("Arial", 24, "bold"),
                                   bg="#f7f7f7")
        self.word_label.pack()

        self.attempts_label = tk.Label(self.root, text=f"Attempts left: {self.attempts}" if self.attempts != float(
            "inf") else "Unlimited Attempts", font=("Arial", 12), bg="#f7f7f7")
        self.attempts_label.pack()

        self.keyboard_frame = tk.Frame(self.root, bg="#f7f7f7")
        self.keyboard_frame.pack()

        self.create_keyboard()

        tk.Button(self.root, text="New Game", font=("Arial", 12), bg="#ffcccb", command=self.new_game).pack(pady=10)

    def create_keyboard(self):
        keys = "abcdefghijklmnopqrstuvwxyz"
        for i, letter in enumerate(keys):
            tk.Button(self.keyboard_frame, text=letter.upper(), font=("Arial", 10), width=3, height=1,
                      command=lambda l=letter: self.guess_letter(l)).grid(row=i // 9, column=i % 9)

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return

        self.guessed_letters.add(letter)
        if letter in self.word:
            for i, l in enumerate(self.word):
                if l == letter:
                    self.word_display[i] = letter
        else:
            if self.attempts != float("inf"):  # Only decrease attempts if not unlimited mode
                self.attempts -= 1

        self.update_ui()

        if "_" not in self.word_display:
            messagebox.showinfo("Game Over", f"{self.players[self.current_player]} wins!")
            self.create_welcome_screen()
        elif self.attempts == 0:
            messagebox.showinfo("Game Over", f"No more attempts! The word was: {self.word}")
            self.create_welcome_screen()
        else:
            if self.mode.get() == "multiplayer":
                self.current_player = 1 - self.current_player
            self.create_game_ui()

    def update_ui(self):
        self.word_label.config(text=" ".join(self.word_display))
        self.attempts_label.config(
            text=f"Attempts left: {self.attempts}" if self.attempts != float("inf") else "Unlimited Attempts")
        self.hangman_label.config(
            text=HANGMAN_STAGES[min(6, 6 - self.attempts)] if self.attempts != float("inf") else HANGMAN_STAGES[0])


if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
