import random
print("----- Number Guessing Game -----")
print("Select Difficulty Level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")
choice = int(input("Enter your choice: "))
if choice == 1:
    start = 1
    end = 10
    attempts = 5
elif choice == 2:
    start = 1
    end = 50
    attempts = 7
elif choice == 3:
    start = 1
    end = 100
    attempts = 5
else:
    print("Invalid choice!")
    exit()
number = random.randint(start, end)
print(f"\nGuess the number between {start} and {end}")
while attempts > 0:
    print("Attempts left:", attempts)
    guess = int(input("Enter your guess: "))
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        score = attempts * 20
        print("Correct! You guessed the number.")
        print("Your Score:", score)
        break
    attempts -= 1
if attempts == 0:
    print("Game Over! The number was:", number)
