'''
Hi James! I have a task for you. I need you to write a function that will take a string and return the number of vowels in the string.

So when the function is called like this:
count_vowels("hello")

The function will return:

2

Because the string "hello" has 2 vowels (e and o).
'''
def vowels(string):
    if 'a' or 'A' in string:
        print('1 a/A')
    if 'e' or 'E' in string:
        print('1 e/E')
    if 'i' or 'I' in string:
        print('1 i/I')
    if 'o' or 'O' in string:
        print('1 o/O')
    if 'u' or 'U' in string:
        print('1 u/U')
string = input('Enter a word: ')
vowels(string)

#I used the internet for help and I still could not do this one 
#Hint: How many parameters does the question ask you to have in the function?
#Hint: What is the function supposed to return?
#Hint: Is your function returning anything?