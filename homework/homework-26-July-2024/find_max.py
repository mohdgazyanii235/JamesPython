'''
Hi James! I have a task for you. I need you to write a function that will take a list of numbers and return the maximum number in the list.

So when the function is called like this:
find_max([1, 2, 3, 4, 5])

The function will return:

5
'''
def find_max(num, x, MAX):
    array = []
    while x < MAX:
        num = input('Enter a number of choice:')
        if num == 'q':
            break
        else:
            array.append(num)
    array.sort()
    return array[-1]
num = input('Enter a number of choice:')
x = 0
MAX = 10
overall_max =  find_max(num,x,MAX)
print(overall_max)


#I am not sure why I need t define num twice but that is the only way it works
#For some reason it only works for some numbers and not others 
#I am not sure why it says '0 arguments given'

'''
How many arguments/parameters did the question ask you to take?
What is the function supposed to return?
What if I say you are not allowed to use array.sort()? How would you solve this problem?
'''

