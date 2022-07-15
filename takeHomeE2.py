'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit E take-home assignment
'''
import random

#---------- Second Script - Guessing Game ------------

#this generates a random int from 1-100, inclusive
secretNum = random.randint(1,100)
print("Welcome to the guessing game. \nYou need to guess a number from 1 to 100.")

#initialize the input number of user and guess times
num = -1
guess = 0

#Keep track when user input is different with the secret number
# , and count how many times until user win
while num != secretNum:
    num = int(input("What is your guess? "))
    guess += 1
    if num < secretNum:
        print("Guess is too low.")
    else:
        print("Guess is too high.")

#congratulate the user, tell how many guesses user took
print(f"Congratulations! \nYou guessed the secret number in {guess} guesses!")

'''
Execution result:
Welcome to the guessing game. 
You need to guess a number from 1 to 100.
What is your guess? 50
Guess is too high.
What is your guess? 25
Guess is too high.
What is your guess? 12
Guess is too high.
What is your guess? 6
Guess is too low.
What is your guess? 9
Guess is too high.
What is your guess? 8
Guess is too high.
Congratulations! 
You guessed the secret number in 6 guesses!

Process finished with exit code 0

'''