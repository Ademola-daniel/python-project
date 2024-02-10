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
