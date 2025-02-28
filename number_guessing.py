import random
import os
import time

answer = random.randrange(1, 100)
tries = 0

os.system("cls" if os.name == "nt" else "clear")

while True:

    guess = int(input("\nGuess a number between 1 and 100: "))
    time.sleep(1)
    if guess == answer:
        break
    elif guess > answer:
        print("\n   Your guess was too high - try again.")
    elif guess < answer:
        print("\n   Your guess was too low - try again.")

    tries += 1

print(f"You guessed correctly in {tries} attempts!")
