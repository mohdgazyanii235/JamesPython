'''
Hi James! I have a task for you. I need you to write a function that will take a number n and return the nth number in the Fibonacci sequence.

So when the function is called like this:
fibonacci(5)

The function will return:

5

Because the 5th number in the Fibonacci sequence is 5 as seen below.
1, 1, 2, 3, 5...
'''
def fibonacci(n,old_num,new_num,Temporary):
    print(new_num)
    for i  in range(0,n-1):
        Temporary = old_num + new_num
        old_num = new_num
        new_num = Temporary
        print(Temporary)

n = int(input('Enter a number of choice'))
old_num = 0
new_num = 1
Temporary  = old_num + new_num
hello = fibonacci(n,old_num,new_num,Temporary)
print(hello)
# When I run the fibonacci sequence, it doesn't print the first '1'
# To resolve this I just printed '1' at the start ut this causes there
# to be one more number hen intended
#E.g. If you input 5, it will print: 1 ,1, 2, 3, 5, 8


'''
Think again James, what is the question asking? Do you need the function to print anything? or return?
What is the function supposed to return?
Is the function asking you to print the entire fibnacci sequence or just the nth number in the sequence?
'''