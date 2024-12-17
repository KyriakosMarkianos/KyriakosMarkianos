import random
import time

class HangmanGame:
    """
    A class to manage the Hangman game logic and state.
    
    Attributes:
        words_to_guess (list): A predefined list of words to choose from.
        max_attempts (int): Maximum number of incorrect guesses allowed.
    """
    
    def __init__(self, words=None, max_attempts=5):
        """
        Initialize the Hangman game.
        
        Args:
            words (list, optional): Custom list of words. Defaults to a predefined list.
            max_attempts (int, optional): Maximum number of incorrect guesses. Defaults to 5.
        """
        # Use a default word list if none is provided
        self.words_to_guess = words or [
            "january", "border", "image", "film", "promise", 
            "kids", "lungs", "doll", "rhyme", "damage", "plants"
        ]
        self.max_attempts = max_attempts
        
        # Game state variables
        self.word = ""
        self.display_word = ""
        self.already_guessed = []
        self.count = 0

    def start_new_game(self):
        """
        Reset the game state and choose a new word to guess.
        """
        # Choose a random word
        self.word = random.choice(self.words_to_guess)
        
        # Create initial display with underscores
        self.display_word = '_' * len(self.word)
        
        # Reset game state
        self.already_guessed = []
        self.count = 0

    def display_hangman(self):
        """
        Display the Hangman ASCII art based on incorrect guesses.
        Mimics the original implementation's visual style.
        """
        hangman_stages = [
            ("""   _____ 
  |      
  |      
  |      
  |      
  |      
  |      
__|__\n""", 1),
            ("""   _____ 
  |     | 
  |     |
  |      
  |      
  |      
  |      
__|__\n""", 2),
            ("""   _____ 
  |     | 
  |     |
  |     | 
  |      
  |      
  |      
__|__\n""", 3),
            ("""   _____ 
  |     | 
  |     |
  |     | 
  |     O 
  |      
  |      
__|__\n""", 4),
            ("""   _____ 
  |     | 
  |     |
  |     | 
  |     O 
  |    /|\ 
  |    / \ 
__|__\n""", 5)
        ]

        if 0 < self.count <= self.max_attempts:
            art, stage = hangman_stages[self.count - 1]
            print(art)
            print("Wrong guess. " + str(self.max_attempts - self.count) + " guesses remaining\n")

    def make_guess(self, guess):
        """
        Process a player's letter guess.
        
        Args:
            guess (str): A single letter guessed by the player.
        
        Returns:
            str: Status of the guess ('valid', 'repeat', 'correct', 'incorrect', 'win', 'lose')
        """
        # Validate input
        if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or not guess.isalpha():
            return 'invalid'

        # Check if letter was already guessed
        if guess in self.already_guessed:
            return 'repeat'

        self.already_guessed.append(guess)

        # Check if guess is in the word
        if guess in self.word:
            # Update display word
            new_display = list(self.display_word)
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    new_display[i] = guess
            self.display_word = ''.join(new_display)

            # Check for win condition
            if '_' not in self.display_word:
                return 'win'
            
            return 'correct'
        
        # Incorrect guess
        self.count += 1
        
        # Check for lose condition
        if self.count >= self.max_attempts:
            return 'lose'
        
        return 'incorrect'

def play_hangman():
    """
    Main game loop for playing Hangman.
    Handles user interaction and game flow.
    """
    print("\nWelcome to Hangman game by Kyriakos Markianos\n")
    name = input("Enter your name: ")
    print("Hello " + name + "! Best of Luck!")
    time.sleep(2)
    print("The game is about to start!\n Let's play Hangman!")
    time.sleep(3)
    
    game = HangmanGame()
    
    while True:
        # Start a new game
        game.start_new_game()
        
        while True:
            # Display current game state
            print("This is the Hangman Word: " + game.display_word)
            
            # Get player's guess
            guess = input("Enter your guess: ")
            
            # Process the guess
            status = game.make_guess(guess)
            
            # Handle different guess outcomes
            if status == 'invalid':
                print("Invalid Input, Try a letter\n")
                continue
            elif status == 'repeat':
                print("Try another letter.\n")
                continue
            elif status == 'correct':
                print(game.display_word + "\n")
            elif status == 'incorrect':
                game.display_hangman()
            elif status == 'win':
                print("Congrats! You have guessed the word correctly!")
                break
            elif status == 'lose':
                print("Wrong guess. You are hanged!!!")
                print("The word was:", game.word)
                break
        
        # Ask to play again
        play_again = input("Do You want to play again? y = yes, n = no \n").lower()
        if play_again not in ['y', 'yes']:
            print("Thanks For Playing! We expect you back again!")
            break

# Run the game
if __name__ == "__main__":
    play_hangman()