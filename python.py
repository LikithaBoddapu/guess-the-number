import random

min_number = 1
max_number = 100
attempts = 0
max_attempts = 10

target_number = random.randint(min_number, max_number)
print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {min_number} and {max_number}.")
print(f"You have {max_attempts} attempts to guess it.")

while attempts < max_attempts:
    try:  
        guess = int(input("Enter your guess: "))
        
        if guess < min_number or guess > max_number:
            print(f"Please enter a number between {min_number} and {max_number}.")
            continue
        
        attempts += 1
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly in {attempts} attempts.")
            break
        
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempts remaining.")
        else:
            print(f"Sorry, you've used all your attempts. The number was {target_number}.")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print("Game over.")
