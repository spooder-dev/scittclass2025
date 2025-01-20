## Graded Assignment 01: Number Guessing Game 

## Due Date: 31/01/2025

## The Objective of the assignment:

Create a simple game where the user is asked to guess a pre-defined number. The program will give feedback on whether the guess is too high or too low until the user guesses the correct number.

## Here are the instructions for you to follow:

Game Overview:

* The program will choose a number between 1 and 10. You should tell the user this.
* The user has to guess the number.
* If the guess is too low, the program will print "Too low! Try again."
* If the guess is too high, the program will print "Too high! Try again."
* When the user guesses correctly, the program will print "Congratulations! You guessed the number."

##  Control Flow

* Use an if/else statement to check if the guess is correct, too low, or too high.
* Use a loop to keep asking the user for their guess until they get it right.

## User Input

* Make sure the user enters an integer.
* If the user enters something that is not a number (like a letter), ask them to enter a valid number.
  
## Ending the Game:

* After the user guesses the number, print the number of attempts they took.
* You can then ask if they want to play again, or just end the game.

## Key Concepts 

* Control flow: Using if, elif, and else to compare the user's guess to the secret number.

* Loops: Using a while loop to repeatedly ask the user for a guess until the correct one is entered.

* User input: Making sure the input is valid (checking if the input is a number using .isdigit()).

## Evaluation Criteria

* Correct use of if, elif, and else statements to check the user’s guess.
* Use of loops to repeat the process until the correct number is guessed.
* Input validation to ensure the user only enters numbers.
* Clear and user-friendly output (messages).
