"""
Problem 2_1:
Write a function 'problem2_1()' that sets a variable lis = list(range(20,30)) and
does all of the following, each on a separate line: 
(a) print the element of lis with the index 3
(b) print lis itself
(c) write a 'for' loop that prints out every element of lis. Recall- that 
    len() will give you the length of such a data collection if you need that.
    Use end=" " to put one space between the elements of the list lis.  Allow
    the extra space at the end of the list to stand, don't make a special case
    of it.
"""  
#%%      
def problem2_1():

    # Here we dynamically create a list using the list() function and the range() function
    lis = list(range(20,30))

    # (a) Print the element of lis with the index 3
    print(lis[3])

    # (b) print lis itself
    print(lis)

    # (c) Write a 'for' loop that prints out every element of lis.
    for num in lis:
        print(num, end=' ')
    #print()
