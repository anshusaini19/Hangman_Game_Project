import random
import time

hangman_images = [
    '''
     ___
    |       |
    |       
    |       
    |      
    |        
    |___
    ''',
    '''
     ___
    |       |
    |       O
    |       
    |       
    |        
    |___
    ''',
    '''
     ___
    |       |
    |       O
    |       |
    |       
    |        
    |___
    ''',
    '''
     ___
    |       |
    |       O
    |      /|
    |       
    |        
    |___
    ''',
    '''
     ___
    |       |
    |       O
    |      /|\\
    |       
    |        
    |___
    ''',
    '''
     ___
    |       |
    |       O
    |      /|\\
    |      / 
    |        
    |___
    ''',
    '''
     ___
    |       |
    |       O
    |      /|\\
    |      / \\
    |        
    |___
    '''
]

words_easy = ['PYTHON', 'JAVA', 'HTML', 'CSS', 'RUBY']
words_medium = ['JAVASCRIPT', 'PHP', 'SWIFT', 'GO']
words_difficult = ['CPLUSPLUS', 'RUST', 'SCALA']

def select_word(difficulty):
    if difficulty == '1':
        return random.choice(words_easy)
    elif difficulty == '2':
        return random.choice(words_medium)
    elif difficulty == '3':
        return random.choice(words_difficult)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def main():
    print("Welcome to Hangman!")
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Difficult")
    
    difficulty = input("Enter the number for your choice: ")

    if difficulty not in ['1', '2', '3']:
        print("Invalid choice!")
        return

    word = select_word(difficulty)
    guessed_letters = set()
    incorrect_guesses = 0
    start_time = time.time()

    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            incorrect_guesses += 1
            print(hangman_images[incorrect_guesses - 1])
            print("Incorrect guess!")

            if incorrect_guesses == len(hangman_images):
                print("You've been hanged! The word was:", word)
                break
        else:
            print("Correct guess!")

        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Congratulations! You've guessed the word:", word)
            print("Elapsed time:", round(elapsed_time, 2), "seconds")
            break

if name == "main":
    main()
