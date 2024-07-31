'''
Hi James, I have a task for you. I need you to write a function that will take a list of numbers (array) and a number (num). The function will return the number of times the number appears in the list.

So, for example, when the function is called like this:
count_occurrences([1, 2, 3, 4, 5, 2, 2], 2)

The function will return:

3

This is because the number 2 (the second parameter) appears 3 times in the list [1, 2, 3, 4, 5, 2, 2] (the first parameter).
'''



def inputs(x,MAX,i,n):
    array = []
    while x < MAX:
        i = input('Enter a number:')
        if i == 'q':
            break
        else:
            array.append(int(i))
            x += 1
    return array.count(n)
n = int(input('which number do you want to check the array for?: '))
i = input('Enter a number:')
x = 0
MAX = 10
end = inputs(x,MAX,i,n)
print(end)
#The only problem is that whne you input the first number, it is not taken into consideration
#By this I mean:
#-assume we are checking for 2
# 2223 would output 2 2's found
# 3222 would output 3 2's found