# Hello James, your first homework for today is to create a python function can given a parameter
# return True, if the parameter is even and False if the parameter is odd.
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
x = int(input("Enter a number of choice:"))    
print(is_even(x))
