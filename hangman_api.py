import tkinter as tk
from tkinter import messagebox
import requests
import random

# Function to get a random word from an API
def get_random_word():
    url = "https://random-word-api.herokuapp.com/word?number=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0].upper()
    else:
        messagebox.showerror("Error", "Unable to fetch word from API")
        return None

# Function to display the hangman stages
def display_hangman(tries):
    stages = [
        "----\n|  |\n|  O\n| /|\\\n| / \\\n|_____",
        "----\n|  |\n|  O\n| /|\\\n| / \n|_____",
        "----\n|  |\n|  O\n| /|\\\n|   \n|_____",
        "----\n|  |\n|  O\n| /|\n|   \n|_____",
        "----\n|  |\n|  O\n|  |\n|   \n|_____",
        "----\n|  |\n|  O\n|   \n|   \n|_____",
        "----\n|  |\n|   \n|   \n|   \n|_____"
    ]
    return stages[tries]

# Function to update the GUI
def update_display():
    global word_completion, tries
    hangman_label.config(text=display_hangman(tries))
    word_label.config(text=" ".join(word_completion))
    tries_label.config(text=f"Tries Left: {tries}")

# Function to handle the player's guess
def make_guess():
    global word_completion, tries, guessed_letters, guessed_words, guessed

    guess = guess_entry.get().upper()
    guess_entry.delete(0, tk.END)

    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            messagebox.showinfo("Hangman", f"You already guessed the letter {guess}")
        elif guess not in word:
            messagebox.showinfo("Hangman", f"{guess} is not in the word.")
            tries -= 1
            guessed_letters.append(guess)
        else:
            messagebox.showinfo("Hangman", f"Good job! {guess} is in the word!")
            guessed_letters.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if "_" not in word_completion:
                guessed = True
    elif len(guess) == len(word) and guess.isalpha():
        if guess in guessed_words:
            messagebox.showinfo("Hangman", f"You already guessed the word {guess}")
        elif guess != word:
            messagebox.showinfo("Hangman", f"{guess} is not the word.")
            tries -= 1
            guessed_words.append(guess)
        else:
            guessed = True
            word_completion = word
    else:
        messagebox.showwarning("Hangman", "Not a valid guess.")

    update_display()

    if guessed:
        messagebox.showinfo("Hangman", "Congratulations, you guessed the word!")
        reset_game()
    elif tries == 0:
        messagebox.showinfo("Hangman", f"Sorry, you ran out of tries. The word was {word}.")
        reset_game()

# Function to reset the game
def reset_game():
    global word, word_completion, guessed, guessed_letters, guessed_words, tries
    word = get_random_word()
    if word:
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        update_display()

# Initialize the game state
word = None
word_completion = None
guessed = False
guessed_letters = []
guessed_words = []
tries = 6

# Initialize the GUI application
app = tk.Tk()
app.title("Hangman Game")

hangman_label = tk.Label(app, text="", font=("Helvetica", 18))
hangman_label.pack()

word_label = tk.Label(app, text="", font=("Helvetica", 24))
word_label.pack()

tries_label = tk.Label(app, text=f"Tries Left: {tries}", font=("Helvetica", 14))
tries_label.pack()

guess_entry = tk.Entry(app, font=("Helvetica", 14))
guess_entry.pack()

guess_button = tk.Button(app, text="Guess", command=make_guess, font=("Helvetica", 14))
guess_button.pack()

# Start the game
reset_game()

# Start the GUI event loop
app.mainloop()
