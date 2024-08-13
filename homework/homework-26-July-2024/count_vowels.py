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

<<<<<<< HEAD
#I used the internet for help and I still could not do this one 
#Hint: How many parameters does the question ask you to have in the function?
#Hint: What is the function supposed to return?
#Hint: Is your function returning anything?
=======
    elif E or e in stri:
        e_count = e_count + 1
    
    elif I or i in stri:
        i_count = i_count + 1

    elif O or o in stri:
        o_count = o_count + 1
    
    elif U or u in stri:
        u_count = u_count + 1

    print(a_count, e_count, i_count, o_count, u_count)
    
n = input('Enter a word: ')
a = "a"
A = "A"
e = "e"
E = "E"
i = "i"
I = "I"
o = "o"
O = "O"
u = "u"
U = "U"
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
vowels(n,a,A,e,E,i,I,o,O,u,U,a_count,e_count,i_count,o_count,u_count)

'''
Well done James, I like your solution and the way you have thought through this problem, but this solution is incorrect.

I want you to read the question again and understand what it is asking you to do.

You need to write a function that will take a string and return the number of vowels in the string.

Hint: How many parameters does the question ask you to have in the function?
Hint: What is the function supposed to return?
Hint: Is your function returning anything?
'''
>>>>>>> 2e30c7ff4dcdaf94b8209429a99c2324a63d7952
