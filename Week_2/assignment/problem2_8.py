""" 
Problem 2_8:
The following list gives the hourly temperature during a 24 hour day. Please
write a function, that will take such a list and compute 3 things: average
temperature, high (maximum temperature), and low (minimum temperature) for the
day.  I will test with a different set of temperatures, so don't pick out
the low or the high and code it into your program. This should work for
other hourly_temp lists as well. This can be done by looping (interating)
through the list. I suggest you not write it all at once. You might write
a function that computes just one of these, say average, then improve it
to handle another, say maximum, etc. Note that there are Python functions
called max() and min() that could also be used to do part of the jobs.
"""
#%%
hourly_temp = [40.0, 39.0, 37.0, 34.0, 33.0, 34.0, 36.0, 37.0, 38.0, 39.0, \
               40.0, 41.0, 44.0, 45.0, 47.0, 48.0, 45.0, 42.0, 39.0, 37.0, \
               36.0, 35.0, 33.0, 32.0]
#%%
def problem2_8(temp_list):
    #Create a place to store the running total.
    my_sum = 0
    
    #add all items in the list together one at a time.
    for item in temp_list:
        my_sum = my_sum + item

    #Calculate the statistics for avg, max and min
    Avg_temp = my_sum / len(temp_list)
    High_temp = max(temp_list)
    Low_temp = min(temp_list)
    
    #Print result of statistics 
    print("Average: {}".format(Avg_temp))
    print("High: {}".format(High_temp)) 
    print("Low: {}".format(Low_temp))

