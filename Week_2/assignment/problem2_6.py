"""
Problem 2_6:
Let's continue with our simulation of dice by rolling two of them. This time
each die can come up with a number from 1 to 6, but you have two of them. The
result or outcome is taken to be the sum of the pips on the two dice. Write a 
program that will roll 2 dice and produce the outcome. This time let's roll 
the two dice 100 times. Print the outcomes one outcome per line.
"""
#%%
import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.

    random.seed(431)  # don't remove when you submit for grading

    # loop 100 times
    for i in range(0,100):
        #roll die 1
        roll_1 = random.randint(1,6)

        #roll die 2
        roll_2 = random.randint(1,6)

        #print result of the sum of both dice
        print(roll_1 + roll_2)

