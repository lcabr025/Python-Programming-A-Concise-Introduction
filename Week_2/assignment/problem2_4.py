"""
Problem 2_4:
random.random() generates pseudo-random real numbers between 0 and 1. But what
if you needed other random reals? Write a program to use only random.random()  
to generate a list of random reals between 30 and 35. This is a simple matter
of multiplication and addition. By multiplying you can spread the random numbers
out to cover the range 0 to 5. By adding you can shift these numbers up to the 
required range from 30 to 35.  Set the seed in this function to 70 so that 
everyone generates the same random numbers and will agree with the grader's 
list of random numbers. Print out the list (in list form).
"""
#%%
import random

def problem2_4():

    # Set the seed of the 'random' library in this function to '70'
    random.seed(70)
    
    # Initialize an empty list to store the randoms we generate later
    my_list = []
    
    # loop 10 times
    for i in range(0,10):
        # generate a list of random reals between 30 and 35 only using random.random() 
        # (note: random.randint(30,35) does the same thing but we can's use it!)
        rand_num = (random.random() * 5) + 30

        # Append to the list!
        my_list.append(rand_num)

    #print out the list in list form
    print(my_list)


