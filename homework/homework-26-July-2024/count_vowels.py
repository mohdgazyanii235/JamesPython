'''
Hi James! I have a task for you. I need you to write a function that will take a string and return the number of vowels in the string.

So when the function is called like this:
count_vowels("hello")

The function will return:

2

Because the string "hello" has 2 vowels (e and o).
'''
def vowels(n,a,A,e,E,i,I,o,O,u,U,a_count,e_count,i_count,o_count,u_count):
    
    if A or a in stri:
        a_count = a_count + 1

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