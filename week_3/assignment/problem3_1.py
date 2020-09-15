"""
Problem 3_1:
Write a function that reads a text file and counts the number of characters in 
it.  Print both the text file and the number of characters. Do this so that the 
printout isn't doubled space (use an end=""  argument in the print statement). 
Also, skip a line before printing the count. Note that it is easy to get the 
number of characters in each line using the len() function.
Here is my run for HumptyDumpty.txt.  Let me point out one thing that is not
visible here and is a bit technical.  At the end of each of the first three
lines there is a <newline> character.  These are invisible.  If you do the count
by eye, you are likely to come up short by these three characters, but they
are visible to len() and you should count them -- they are part of the 141
"letters" in the humptydumpty.txt file.  Counting them makes this an easier 
function for you to write.

Your output should look just like this for the autograder:

problem3_1("humptydumpty.txt")
Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the king's horses and all the king's men
Couldn't put Humpty together again.

There are 141 letters in the file.

"""

#%%
import sys

def problem3_1(txtfilename):    #defining the function
    f = open(txtfilename)   #open the file for reading

    count = 0   #set count to 0
    for line in f.readlines():  #step through each line in the text file
        print(line, end="" )    #print
        count = count +len(line)    #to get the number of characters in the text file
    print()   #calling this after using end="" to add a final new line

    print("\nThere are {} letters in the file.".format(count))