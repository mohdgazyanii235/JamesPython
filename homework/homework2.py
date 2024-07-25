# Hello James, next homework
# create a function called square_root(num) which takes a parameter num and returns the square root of the number. if no square root is found, return False
def square_root(num):
    for i in range(0,num):
        if i * i == num:
            return i
    return False
    
num = int(input('Enter a number: '))
print(square_root(num))