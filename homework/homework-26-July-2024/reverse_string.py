'''
Hi James, I have a task for you. I need you to write a function that will take a string and return the reverse of the string.

So when the function is called like this:
reverse_string("hello")

The function will return:

"olleh"
'''
def reverse(n):
    return n[::-1]
            
n = input('Enter a word of choice:')
new = reverse(n)
print(new)

#I used the internet to find out he '[::-1]'

'''
Well done James, I like your solution and this is infact the best way to solve this problem.
However, this is not the algorithmic way to solve this problem. I want you think about the problem and how you would solve it without using the [::-1] method.
Perhaps you could use a for loop to solve this problem?
'''