import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time

# Replace the file paths with the paths to your PNG images
HANGMAN_PICS = [
    "C:\\Users\\Dell\\Downloads\\1.png",
    "C:\\Users\\Dell\\Downloads\\2.png",
    "C:\\Users\\Dell\\Downloads\\3.png",
    "C:\\Users\\Dell\\Downloads\\4.png",
    "C:\\Users\\Dell\\Downloads\\5.png",
    "C:\\Users\\Dell\\Downloads\\6.png",
    "C:\\Users\\Dell\\Downloads\\7.png"
]

countries = [
    ("usa", "The land of the free"),
    ("uk", "Home of Big Ben"),
    ("france", "Eiffel Tower stands tall here"),
    ("china", "The Great Wall"),
    ("brazil", "Famous for the Amazon Rainforest"),
    ("russia", "Largest country by land area"),
    ("india", "Taj Mahal resides here"),
    ("australia", "Known as the Land Down Under"),
    ("germany", "Famous for its beer and sausages"),
    ("japan", "Land of the rising sun"),
    ("canada", "Second largest country in the world"),
    ("italy", "Home to the Colosseum"),
    ("spain", "Famous for its siestas and fiestas"),
    ("mexico", "Birthplace of tacos and tequila"),
    ("argentina", "Famous for Tango and Maradona"),
    ("egypt", "Home to the Pyramids and Sphinx"),
    ("southafrica", "Known for its diverse wildlife"),
    ("southkorea", "Home of K-pop and kimchi"),
    ("greece", "Birthplace of democracy and the Olympics"),
    ("thailand", "Land of smiles and tropical beaches")
]

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.configure(bg="#E6E6FA")  # Set lavender background color
        
        self.canvas = tk.Canvas(self.master, width=400, height=500, bg="#E6E6FA")  # Set lavender background color
        self.canvas.pack()
        
        self.missed_letters_label = tk.Label(self.master, text="Missed Letters:", bg="#E6E6FA", fg="#8B0000", font=("Arial", 14))
        self.missed_letters_label.pack()
        
        self.missed_letters_var = tk.StringVar()
        self.missed_letters_display = tk.Label(self.master, textvariable=self.missed_letters_var, bg="#E6E6FA", fg="#8B0000", font=("Arial", 14))
        self.missed_letters_display.pack()
        
        self.secret_word_label = tk.Label(self.master, text="Secret Word:", bg="#E6E6FA", fg="#8B0000", font=("Arial", 14))
        self.secret_word_label.pack()
        
        self.secret_word_var = tk.StringVar()
        self.secret_word_display = tk.Label(self.master, textvariable=self.secret_word_var, bg="#E6E6FA", fg="#8B0000", font=("Arial", 14))
        self.secret_word_display.pack()
        
        self.hint_label = tk.Label(self.master, text="Hint:", bg="#E6E6FA", fg="#8B0000", font=("Arial", 14))
        self.hint_label.pack()
        
        self.hint_var = tk.StringVar()
        self.hint_display = tk.Label(self.master, textvariable=self.hint_var, bg="#E6E6FA", fg="#8B0000", font=("Arial", 14))
        self.hint_display.pack()
        
        self.guess_label = tk.Label(self.master, text="Enter a Letter:", bg="#E6E6FA", fg="#8B0000", font=("Arial", 14))
        self.guess_label.pack()
        
        self.guess_entry = tk.Entry(self.master, font=("Arial", 14))
        self.guess_entry.pack()
        
        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess, bg="#DC143C", fg="#E6E6FA", font=("Arial", 14))  # Set button color
        self.guess_button.pack()
        
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_game, bg="#DC143C", fg="#E6E6FA", font=("Arial", 14))  # Set button color
        self.reset_button.pack()
        
        self.initialize_game()
    
    def animate_correct_guess(self):
        self.secret_word_display.config(fg="green")  # Change the color of the correct letters
        # Add a short delay to the animation
        self.master.update()
        time.sleep(0.5)  # Adjust the delay time as needed

        # Reset the color back to the original color
        self.secret_word_display.config(fg="#8B0000")  # Original color of the letters

    def animate_hangman(self, missed):
        for i in range(missed + 1):
            img_path = HANGMAN_PICS[i]
            img = Image.open(img_path)
            img = img.resize((200, 200), Image.ANTIALIAS)  # Resize the image if needed
            photo = ImageTk.PhotoImage(img)
            self.canvas.image = photo  # Keep a reference to prevent garbage collection
            self.canvas.create_image(200, 200, image=photo, anchor=tk.CENTER)
        
            # Add a short delay between each frame of the animation
            self.master.update()
            time.sleep(0.5)  # Adjust the delay time as needed
        self.canvas.delete("hangman")
    



    def initialize_game(self):
        self.missed_letters = ''
        self.correct_letters = ''
        self.secret_word, self.hint = getRandomCountry(countries)
        self.update_display()

    def update_display(self):
        self.missed_letters_var.set(self.missed_letters)
        
        blanks = ''
        for letter in self.secret_word:
            if letter in self.correct_letters:
                blanks += letter + ' '
            else:
                blanks += '_ '
        self.secret_word_var.set(blanks)
        
        self.hint_var.set(self.hint)
        
        self.draw_hangman(len(self.missed_letters))
        
    def make_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Invalid Guess", "Please enter a single letter.")
            return

        if guess in self.correct_letters or guess in self.missed_letters:
            messagebox.showwarning("Duplicate Guess", "You have already guessed that letter. Choose again.")
            return

        if guess in self.secret_word:
            self.correct_letters += guess
            self.animate_correct_guess() 
            self.update_display()  # Update display after correct guess
            if self.check_win():
                messagebox.showinfo("Congratulations", f"You guessed it!\nThe secret word is '{self.secret_word}'. You win!")
                self.initialize_game()
        else:
            self.missed_letters += guess
            if len(self.missed_letters) == len(HANGMAN_PICS) - 1:
                self.update_display()
                messagebox.showinfo("Game Over", f"You have run out of guesses!\nAfter {len(self.missed_letters)} missed guesses and {len(self.correct_letters)} correct guesses, the word was '{self.secret_word}'.")
                self.initialize_game()
            else:
                self.animate_hangman(len(self.missed_letters))
                self.update_display()

    def check_win(self):
        for letter in self.secret_word:
            if letter not in self.correct_letters:
                return False
        return True
    
    

    def draw_hangman(self, missed):
        self.canvas.delete("hangman")
        
        # Load the image based on the number of missed guesses
        img_path = HANGMAN_PICS[missed]
        img = Image.open(img_path)
        img = img.resize((200, 200), Image.ANTIALIAS)  # Resize the image if needed
        photo = ImageTk.PhotoImage(img)
        
        # Create a label to display the image
        self.canvas.image = photo  # Keep a reference to prevent garbage collection
        self.canvas.create_image(200, 200, image=photo, anchor=tk.CENTER, tags="hangman")

    def reset_game(self):
        if messagebox.askyesno("Reset Game", "Are you sure you want to reset the game?"):
            self.initialize_game()

def getRandomCountry(countriesList):
    return random.choice(countriesList)

def main():
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
