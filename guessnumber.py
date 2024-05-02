import random

def guess_the_number():
    number = random.randint(1, 100)  # Computer selects a number between 1 and 100
    attempts = 0
    print("Guess the number I'm thinking of! It's between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("Too low, try again.")
            elif guess > number:
                print("Too high, try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guess_the_number()
