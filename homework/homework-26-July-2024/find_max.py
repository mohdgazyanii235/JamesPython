'''
Hi James! I have a task for you. I need you to write a function that will take a list of numbers and return the maximum number in the list.

So when the function is called like this:
find_max([1, 2, 3, 4, 5])

The function will return:

5
'''
def find_max(array_1):
    current = array_1[0]
    for i in array_1:
        if i > current:
            current = i
    return current

array_1 = [23,65,22,5579,43,56,7,34]
answer = find_max(array_1)
print(answer)

'''
How many arguments/parameters did the question ask you to take?
What is the function supposed to return?
What if I say you are not allowed to use array.sort()? How would you solve this problem?
'''

