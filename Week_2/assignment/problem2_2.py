"""
Test run:

problem2_1()
23
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
20 21 22 23 24 25 26 27 28 29 

"""
"""
Problem 2_2:
Write a function 'problem2_2()' that takes a list and does the following to it.
Actually, I've started the function for you below. Your function should do all 
of the following, each on a separate line. Recall that lists start numbering 
with 0.
0) print the whole list (this doesn't require a while or for loop)
1) print the item with index 0
2) print the last item in the list
3) print the items with indexes 3 through 5 but not including 5
4) print the items up to the one with index 3 but not including item 3
5) print the items starting at index 3 and going through the end.
6) print the length of the list ( use len() )
7) Use the append() method of a list to append the letter "z" onto a list.
   Print the list with z appended.

Make sure that your function also works with blist below.  For this to work, 
you cannot use alist as a variable inside your function.  
"""  
#%%  

alist = ["a","e","i","o","u","y"]
blist = ["alpha", "beta", "gamma", "delta", "epsilon", "eta", "theta"] 

def problem2_2(my_list):
    
    # 0) print the whole list
    print(my_list)

    # 1) print item with index 0
    print(my_list[0])

    # 2) print last item in the list
    print(my_list[len(my_list)-1])

    # 3) print items with index 3-5 not including 5
    print(my_list[3:5])

    # 4) print items up to index 3 but not including item 3
    print(my_list[:3])

    # 5) print items starting at index 3 to end
    print(my_list[3:])

    # 6) print the length of the list
    print(len(my_list))

    # 7) use append() of a list to append the letter "z" onto a list
    my_list.append("z")
    print(my_list)

