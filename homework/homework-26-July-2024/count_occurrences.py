'''
Hi James, I have a task for you. I need you to write a function that will take a list of numbers (array) and a number (num). The function will return the number of times the number appears in the list.

So, for example, when the function is called like this:
count_occurrences([1, 2, 3, 4, 5, 2, 2], 2)

The function will return:

3

This is because the number 2 (the second parameter) appears 3 times in the list [1, 2, 3, 4, 5, 2, 2] (the first parameter).
'''



def inputs():
    array = []
    while True:
        x = input('Enter a number: ')
        if x == 'q':
            break
        else:
            array.append(int(x))
    return array,2
end = inputs()
print(end)
#Everything works apart from printing the number of 2s


'''
This solution is incorrect, I want you read the question again and understand what it is asking you to do.
Hint: What is the name of the function you are supposed to write?
Hint: How many parameters did the question ask you to have in the function?
Hint: What are the parameters supposed to be?
Hint: What is the function supposed to return?
Hint: When are you supposed to take the input from the user? Inside the function or outside?

Try doing this again and we will discuss it in the next class. Solve it below in new function called count_occurrences_v2(array, num) and print the result.
'''