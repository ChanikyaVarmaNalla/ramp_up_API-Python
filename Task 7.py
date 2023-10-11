import random

def main():
    print("Welcome to the Number Guessing Game!")
    high_score = None

    while True:
        lower_bound, upper_bound = get_range()
        secret_number = random.randint(lower_bound, upper_bound)
        attempts = 0
        print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

        while True:
            user_guess = get_user_guess(lower_bound, upper_bound)
            attempts += 1

            if user_guess < secret_number:
                print("Try a higher number.")
            elif user_guess > secret_number:
                print("Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                if high_score is None or attempts < high_score:
                    high_score = attempts
                    print(f"New High Score: {high_score} attempts!")
                break

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("Thank You for playing the Guessing Game!")
            break

def get_range():
    while True:
        try:
            lower_bound = int(input("Enter the lower bound of the range: "))
            upper_bound = int(input("Enter the upper bound of the range: "))
            if lower_bound < upper_bound:
                return lower_bound, upper_bound
            else:
                print("Please make sure the lower bound is less than the upper bound.")
        except ValueError:
            print("Please enter valid integers for the range.")

def get_user_guess(lower_bound, upper_bound):
    while True:
        try:
            user_guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= user_guess <= upper_bound:
                return user_guess
            else:
                print(f"Please enter a number within the range {lower_bound} and {upper_bound}.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
