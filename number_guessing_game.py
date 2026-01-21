import random

# Number guessing game with multiple attempts
secret_number = random.randint(1, 10)
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("Correct!")
        break
    else:
        print("Wrong!")
else:
    print(f"Sorry! The number was {secret_number}")
