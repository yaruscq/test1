import random

def guess_number_game():
    """
    A number guessing game where the player tries to guess
    a random number between 0 and 10.
    """
    # Generate a random number between 0 and 10
    secret_number = random.randint(0, 10)
    attempts = 0
    max_attempts = 3
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 0 and 10.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    while attempts < max_attempts:
        try:
            # Get user's guess
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            
            # Validate input range
            if guess < 0 or guess > 10:
                print("Please enter a number between 0 and 10.\n")
                continue
            
            attempts += 1
            
            # Check if guess is correct
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempt(s)!")
                print(f"The number was {secret_number}.")
                return
            
            # Provide feedback
            elif guess < secret_number:
                print("Too low! Try again.\n")
            else:
                print("Too high! Try again.\n")
                
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            continue
    
    # Player ran out of attempts
    print(f"\n😞 Game Over! You've used all {max_attempts} attempts.")
    print(f"The secret number was {secret_number}.")
    print("Better luck next time!")

if __name__ == "__main__":
    guess_number_game()



