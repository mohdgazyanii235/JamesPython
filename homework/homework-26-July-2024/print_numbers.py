'''
Hi, James! I have a task for you. I need you to write a function that will print numbers from 1 to n. n is a parameter that the function will take.

so when the function is called like this:
print_numbers(5)

I want the function to prsint:
1
2
3
4
5
'''
def numbers(n):
    for i in range(0,n+1):
        print(i)
n = int(input('Enter a number of choice: '))
numbers(n)