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



'''
Write your explanation below this:

----- START ----


---- END ----

'''