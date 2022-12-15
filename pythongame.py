# Import the necessary modules
import random

# Define the starting level and score
level = 1
score = 0

# Define the game loop
while True:
  # Generate a random number between 1 and 10
  random_number = random.randint(1, 10)

  # Prompt the user to guess the number
  user_guess = int(input("Level %d: Guess a number between 1 and 10: " % level))

  # Check if the user's guess is correct
  if user_guess == random_number:
    print("You guessed the number correctly!")
    score += 1
  else:
    print("Sorry, that's not the correct number. Please try again.")

  # Check if the user has reached the next level
  if score == level * 5:
    print("Congratulations, you have reached level %d!" % (level + 1))
    level += 1

  # Prompt the user to continue playing
  play_again = input("Would you like to play again (Y/n)? ")
  if play_again.lower() != "y":
    break
