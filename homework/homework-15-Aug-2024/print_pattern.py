'''
Hello James, I have a new task for you. I need you to write a function that will take a 2 parameters (remember only 2 parameters) the 2 parameters are row and height.
The function should do this:

- pattern_printer(3, 4)
XXX
XXX
XXX
XXX

- pattern_printer(5, 2)
XXXXX
XXXXX

- pattern_printer(1, 1)
X

Basically, pattern printer should print a pattern of X's based on the row and height given.
To help you out here is a hint:
- you need to use a loop
- remember string multiplication works.... so "X" * 3 will give you "XXX" (this is very important)
- you need to use the print() function to print the pattern
- the function doesn't return anything, it just prints the pattern

I am helping you out with the function signature below:
'''

def pattern_printer(heigh, row):
    a = 0
    while a < heigh:
            print("X"*row)
            a += 1

row = int(input('How many units wide do you want:'))
heigh = int(input('How many units high do you want: '))
pattern_printer(heigh, row)

#I tried to make the code as efficient as possible with a few lines as I could