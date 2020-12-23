"""
Task 4

The math quiz program

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.
"""
import random
number1 = random.randint(1, 20)
number2 = random.randint(1, 20)
result = input(f'{number1} + {number2} = ' )
if int(result) == number1+number2:
    print('Yes! You`re right!')
else:
    print('No! It`s incorect!')