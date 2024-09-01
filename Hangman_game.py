import random

def get_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']
    return random.choice(words)

def display_hangman(tries):
    stages = [  
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
               |
               |
               |
               |
        =========
        '''
    ]
    return stages[tries]

def hangman():
    word = get_word()
    guessed_word = ['_'] * len(word)
    guessed_letters = set()
    tries = 6
    
    print("Welcome to Hangman!")
    
    while tries > 0:
        print(display_hangman(tries))
        print(" ".join(guessed_word))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            tries -= 1
        
        if '_' not in guessed_word:
            print("Congratulations! You guessed the word:", word)
            break
    else:
        print(display_hangman(tries))
        print("Game over! The word was:", word)

if __name__ == "__main__":
    hangman()