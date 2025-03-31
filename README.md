Hangman Game is a GUI-based word-guessing game built with Tkinter in Python. Here’s a breakdown of how it works:

🛠 Key Features
✅ Multiple Game Modes

Multiplayer (2 Players, 6 Attempts Each)

Single Player (6 Attempts Mode)

Single Player (Unlimited Attempts Mode)

✅ Graphical User Interface (GUI)

Uses Tkinter for a user-friendly interactive design

A welcome screen to select game modes

Displays Hangman drawing stages dynamically

✅ Game Mechanics

Random word selection from a predefined list

Players guess letters using a virtual keyboard

Keeps track of attempts, guessed letters, and turns

Automatic turn switching for multiplayer mode

Win/Lose conditions displayed via message boxes

🔍 How It Works
1️⃣ Welcome Screen – Players choose a game mode
2️⃣ Game Starts – A random word is selected and displayed as _ _ _
3️⃣ Player Guesses a Letter – The game checks if it's correct
4️⃣ Correct Guess? – The letter fills in the word
5️⃣ Wrong Guess? – Attempts decrease, and Hangman drawing updates
6️⃣ Win/Loss Conditions

If all letters are guessed ✅ → Player Wins!

If attempts reach zero ❌ → Game Over
