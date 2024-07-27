'''
Hi James! I have a task for you. I need you to write a function that will take a number n and return the sum of all numbers from 1 to n.

So when the function is called like this:
sum_of_numbers(5)

The function will return:
1 + 2 + 3 + 4 + 5 = 15
'''
def sum_of(n):
    array = []
    for i in range(0,n+1):
        array.append(i)
    return sum(array)
n = int(input('Enter a number of choice: '))
summary = sum_of(n)
print(summary)

#I am not sure how to print out '1 + 2 + 3' etc
