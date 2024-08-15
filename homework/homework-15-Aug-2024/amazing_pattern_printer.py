'''
Hi James, I have a task for you. I need you to write a a detailed explation between the comment section below about what my code is doing...

Your explanation should obviously be in english but should be able to explain to a 3 year old what the code is doing.
You might need to run the function with different parameters to understand what the function is doing. feel free to play around with the code to understand what it is doing.


Basically you need to answer the following questions in your essay:
- What is the function returning?
- What can this function be used to do?
- How is the function working?
- How many parameters does the function take?
- How do you call this function?
'''

def amazing_pattern_printer(size):
    i = 0
    j = 0
    while i < size:
        while j < size:
            if i == j:
                print("O", end="")
            else:
                print("X", end="")
            j += 1
        print()
        i += 1
        j = 0

amazing_pattern_printer(5)
#The function amazing pattern printer takes the parameter '5' which is definedd when the function is called on line 30
# i and j are both equated to the values 0
# On line 19, a while loop is used, the algorithm will enter the loop until i is not less than 5
# To carry on in this loop, another while loop is created which allows you to continue if j is less then 5
# On line 21, if i and j are the same values, '0' is printed and the rest of the values are 'X'
# If i and j are not equal, the algorithm moves to the else statement on line 23 and prints 'x' until i and j are equal in which it prints '0'and then prints 'X' for the rest of the slots
# Once the algorithm has either entered the if/else statement it then increments j by 1 
# After j has been incramented, the output (0 or X) is printed to the user
# i is then incremented and j is equated to 0 
# The function is then called outside the loop with the parameter inside the brackets which is 'size'
# QUESTIONS
# - I am not sure what 'end=' does. I tried to base my answer around what I understood and what I gathered from running the code a few times
# - I am not sure why j is increented and then equated to 0 
'''
Write your explanation below this:

----- START ----
#

---- END ----

'''