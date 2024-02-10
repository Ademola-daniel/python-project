import tkinter as tk
from tkinter import messagebox
import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "science", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def guess_letter():
    guess = entry.get().lower()
    entry.delete(0, 'end')

    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    if guess in guessed_letters:
        messagebox.showwarning("Duplicate Guess", "You've already guessed that letter. Try again.")
        return

    guessed_letters.append(guess)

    if guess not in word_to_guess:
        print("Wrong guess")
        attempts_left_label.config(text=f"Attempts Left: {attempts_left}")
        if attempts_left == 0:
            messagebox.showinfo("Game Over", f"Sorry, you're out of attempts. The word was: {word_to_guess}")
            reset_game()
        return

current_display = display_word(word_to_guess, guessed_letters)
    word_label.config(text=f"Word: {current_display}")
    if all(letter in guessed_letters for letter in word_to_guess):
        messagebox.showinfo("Congratulations", f"Congratulations! You've guessed the word: {word_to_guess}")
        reset_game()

def reset_game():
    global guessed_letters, attempts_left, word_to_guess
    guessed_letters = []
    attempts_left = max_attempts
    word_to_guess = choose_word()
    current_display = display_word(word_to_guess, guessed_letters)
    word_label.config(text=f"Word: {current_display}")
    attempts_left_label.config(text=f"Attempts Left: {attempts_left}")

# GUI setup
root = tk.Tk()
root.title("Hangman")

word_to_guess = choose_word()
max_attempts = 6
guessed_letters = []
attempts_left = max_attempts

word_label = tk.Label(root, text=f"Word: {display_word(word_to_guess, guessed_letters)}")
word_label.pack()

attempts_left_label = tk.Label(root, text=f"Attempts Left: {attempts_left}")
attempts_left_label.pack()

entry = tk.Entry(root, width=10)
entry.pack()

guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.pack()

root.mainloop()

