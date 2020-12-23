import random

"""
Task 1
The Guessing Game.
Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement.
"""

number = random.randint(1, 10)
user_answer = input('Please, write your number ')
if number == int(user_answer):
    print('Yes, you`re right!')
else:
    print('No, it`s incorrect')