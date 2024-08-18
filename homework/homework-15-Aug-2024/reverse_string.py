'''
Let's see if you can do this again!

Hi James, I have a task for you. I need you to write a function that will take a string and return the reverse of the string.

So when the function is called like this:
reverse_string("hello")

remove line 16 (pass) and write your code there

The function will return:

"olleh"
'''



def new_reverse(sentence):
    reverse = ""
    i = len(sentence) -1
    while  i > -1:
        a = sentence[i]
        reverse += a 
        i -= 1

    return reverse
sentence = input("Enter a sentence: ")
answer = new_reverse(sentence)
print(answer)
