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