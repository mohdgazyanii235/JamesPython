'''
Hi James, I have a task for you. I need you to write a function that will take a list of numbers (array) and a number (num). The function will return the number of times the number appears in the list.

So, for example, when the function is called like this:
count_occurrences([1, 2, 3, 4, 5, 2, 2], 2)

The function will return:

3

This is because the number 2 (the second parameter) appears 3 times in the list [1, 2, 3, 4, 5, 2, 2] (the first parameter).
'''

def inputs(array):
    while True:
        x = input('Enter a number: ')
        if x == 'q':
            break
        else:
            array.append(int(x))
    return array

array = []
answer = inputs(array)


def check_array(num):
    appearances = 0
    for i in answer:
        if i == num:
            appearances += 1
    return appearances

num = int(input('What number do you want to check the array for: '))
new_answer = check_array(num)
print(new_answer)




